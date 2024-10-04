import cv2
import imutils
import mediapipe as mp
import numpy as np

mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

count = 0
position = None
feedback = ""

# Replace the filename with 0 to use your webcam
cap = cv2.VideoCapture("v1.mp4")
with mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("empty camera")
            break

        h, w, _ = image.shape
        aspect_ratio = w / h
        new_width = 500
        new_height = int(new_width / aspect_ratio)
        image = cv2.resize(image, (new_width, new_height))

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        result = pose.process(image)

        lmList = []
        if result.pose_landmarks:
            mp_draw.draw_landmarks(image, result.pose_landmarks,
                                   mp_pose.POSE_CONNECTIONS)
            for id, im in enumerate(result.pose_landmarks.landmark):
                h, w, _ = image.shape
                X, Y = int(im.x * w), int(im.y * h)
                lmList.append([id, X, Y])

        if len(lmList) != 0:
            shoulder_avg_y = (lmList[11][2] + lmList[12][2]) / 2
            hip_avg_y = (lmList[23][2] + lmList[24][2]) / 2
            knee_avg_y = (lmList[25][2] + lmList[26][2]) / 2

            if shoulder_avg_y >= hip_avg_y and hip_avg_y >= knee_avg_y:
                position = "down"
                feedback = "Good form! Keep your body straight."

            if shoulder_avg_y <= hip_avg_y and hip_avg_y <= knee_avg_y and position == "down":
                position = "up"
                count += 1
                feedback = "Great job! Keep going."
                print(count)

        cv2.putText(image, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Push-up counter", cv2.flip(image, 1))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
