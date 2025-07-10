import os
from PIL import Image
import face_recognition
import pickle
import cv2

# --- CONFIGURATION ---
dataset_dir = "dataset"
output_file = "encodings.pickle"
image_mode = "RGB"  # "L" for 8-bit grayscale, or "RGB" for color (RECOMMENDED)

# --- STEP 1: Fix all images ---
print(f"[STEP 1] Converting all images in '{dataset_dir}/' to {image_mode}...")

supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
image_count = 0

for person in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person)
    if not os.path.isdir(person_path):
        continue

    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)

        if not image_name.lower().endswith(supported_extensions):
            print(f"[SKIP] Not an image: {img_path}")
            continue

        try:
            with Image.open(img_path) as img:
                img = img.convert(image_mode)
                img.save(img_path)
                image_count += 1
        except Exception as e:
            print(f"[ERROR] Cannot fix {img_path} - {e}")

print(f"[DONE] Converted {image_count} images to {image_mode}.\n")


# --- STEP 2: Encode Faces ---
print("[STEP 2] Starting face encoding...")

known_encodings = []
known_names = []
encoded_count = 0

for person_name in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_name)
    if not os.path.isdir(person_path):
        continue

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(image_path)
        if image is None:
            print(f"[ERROR] Cannot read image: {image_path}")
            continue

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)

        if len(encodings) == 0:
            print(f"[WARNING] No face found in {image_path}")
            continue

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)
            encoded_count += 1

# Save encodings to pickle
print(f"[INFO] Saving {encoded_count} encodings to {output_file}...")
data = {"encodings": known_encodings, "names": known_names}

with open(output_file, "wb") as f:
    f.write(pickle.dumps(data))

print(f"[SUCCESS] Encoding complete. Total encoded faces: {encoded_count}")
