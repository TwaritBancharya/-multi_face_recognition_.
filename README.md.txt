# ABOUT- Multi-Face Recognition System using Python

A real-time face recognition system built with Python, OpenCV, and the 'face_recognition' library. This project detects and identifies multiple known faces from webcam video using pre-encoded face data.

------------------------------------------------------------------------------------------------------------------------------------------

Folder Structure

Multi-face-recognition/
├── dataset/ # Folder with subfolders for each person's images
│ ├── Elon/
│ │ └── elon1.jpg
│ └── Steve/
│ └── steve1.jpg
├── fix_and_encode_faces.py # Script to convert images to RGB and encode faces
├── recognize_faces.py # Real-time face recognition using webcam
├── encodings.pickle # Generated face encodings (after encoding) Automatic generate
├── requirements.txt # Python dependencies
└── README.md # Project instructions(Read carefully for run this project)



1. Add images of each person inside separate folders under `dataset/`
2. Run the script to:
   - Convert all images to supported format (RGB)
   - Encode each face into 'encodings.pickle'
3. Run the webcam recognition to identify known faces live!

---

-> Getting Started

1. Clone or Download the Project

bash
git clone https://github.com/your-username/multi-face-recognition.git
cd multi-face-recognition
2. Install Python Dependencies

->Open this Folder in Command Prompt and Run following commands one by one
pip install -r requirements.txt(run this command)


OR 
Manually->
{
pip install face_recognition
pip install OpenCV
pip install dlib
}
3. Prepare the Dataset
Add clear color face images to:

dataset/
├── Person1/
│   └── 1.jpg
├── Person2/
│   └── 1.jpg
✅ Each folder = one person's name
✅ Use .jpg, .png, .jpeg, or .bmp only


🛠 Run the Project
Step 1: Fix and Encode Images

python fix_and_encode_faces.py (Run Command)

This will:
1.Convert all dataset images to RGB
2.Encode all faces into encodings.pickle (MAKE SURE this file generate successfully in Your project folder)

Step 2: Start Real-Time Recognition

python recognize_faces.py (Run final Command)

Press q to exit the webcam window.

🧰 Troubleshooting
❌ "Unsupported image type" → Run fix_and_encode_faces.py to convert

❌ FileNotFoundError → Check if dataset/ and images are correctly placed

❌ 0 encodings → Ensure at least one face is detected per image

