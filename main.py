import cv2
from deepface import DeepFace
import webbrowser
import time

# Open webcam
cap = cv2.VideoCapture(0)

# Prevent browser from opening repeatedly
last_emotion = ""
last_open_time = 0

# Emotion → YouTube playlist mapping
emotion_music = {
    "happy": "https://www.youtube.com/results?search_query=happy+songs+playlist",
    "sad": "https://www.youtube.com/results?search_query=sad+lofi+songs",
    "angry": "https://www.youtube.com/results?search_query=calming+music",
    "neutral": "https://www.youtube.com/results?search_query=chill+beats",
    "surprise": "https://www.youtube.com/results?search_query=party+songs",
    "fear": "https://www.youtube.com/results?search_query=relaxing+music",
    "disgust": "https://www.youtube.com/results?search_query=instrumental+music"
}

print("Emotion Music Player Started")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    try:

        # Detect emotion
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )

        emotion = result[0]['dominant_emotion']

        # Face coordinates
        x = result[0]['region']['x']
        y = result[0]['region']['y']
        w = result[0]['region']['w']
        h = result[0]['region']['h']

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Show emotion text
        cv2.putText(
            frame,
            f'Emotion: {emotion}',
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        current_time = time.time()

        # Open browser only if emotion changed
        # and 10 seconds passed
        if (
            emotion != last_emotion
            and current_time - last_open_time > 10
        ):

            print(f"Detected Emotion: {emotion}")

            # Get playlist URL
            url = emotion_music.get(emotion)

            if url:
                webbrowser.open(url)

            last_emotion = emotion
            last_open_time = current_time

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion Music Player", frame)

    # ESC key to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()