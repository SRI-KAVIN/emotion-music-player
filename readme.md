# Emotion Based Music Player 

An AI-powered music player that detects human emotions using a webcam and automatically plays music based on the detected mood through YouTube.

## Features

- Real-time face emotion detection
- Webcam integration using OpenCV
- Emotion analysis using DeepFace
- Automatic music recommendation
- Opens YouTube playlists based on mood
- Live emotion display on screen

## Tech Stack

### Machine Learning / AI
- Python
- DeepFace
- TensorFlow
- OpenCV

### Other Libraries
- webbrowser
- time

## Supported Emotions

| Emotion  | Music Type         |
|----------|--------------------|
| Happy    | Happy Songs        |
| Sad      | Sad / Lofi Songs   |
| Angry    | Calming Music      |
| Neutral  | Chill Beats        |
| Surprise | Party Songs        |
| Fear     | Relaxing Music     |
| Disgust  | Instrumental Music |

---

# Project Workflow

```text
Webcam → Face Detection → Emotion Detection
       → Emotion Mapping
       → Open YouTube Playlist
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/emotion-music-player.git
```

## 2. Open Project Folder

```bash
cd emotion-music-player
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

#### PowerShell

```powershell
venv\Scripts\activate
```

#### Git Bash

```bash
source venv/Scripts/activate
```

---

# Install Dependencies

```bash
pip install opencv-python
pip install deepface
pip install tensorflow
pip install tf-keras
```

---

# Run the Project

```bash
python main.py
```

---

# How It Works

1. Webcam captures live video.
2. DeepFace analyzes facial emotion.
3. Dominant emotion is detected.
4. Matching YouTube playlist is selected.
5. Browser automatically opens music playlist.

---

# Future Improvements

- Spotify API integration
- React frontend
- Personalized recommendations
- Emotion history tracking
- Voice emotion detection
- Multi-user emotion analysis

---

# Project Structure

```text
emotion-music-player/
│
├── venv/
├── main.py
├── README.md
└── requirements.txt
```

---

# Author

S K SRI KAVIN