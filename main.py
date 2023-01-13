import cv2
import imutils
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

count = 0
position = None
# Replace the filename with 0 to use your webcam
cap=cv2.VideoCapture("v1.mp4")
with mp_pose.Pose(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7) as pose:
    while cap.isOpened():
        success, image=cap.read()
        if not success:
            print("empty camera")
            break
        image = imutils.resize(image, width=500)
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        result = pose.process(image)

        lmList = []
        if result.pose_landmarks:
            mp_draw.draw_landmarks(image, result.pose_landmarks,
                                       mp_pose.POSE_CONNECTIONS)
            for id, im in enumerate(result.pose_landmarks.landmark):

                h, w, _ = image.shape

                X, Y = int(im.x*w), int(im.y*h)

                lmList.append([id, X, Y])
        if len(lmList) != 0:
            if (lmList[12][2] and lmList[11][2] >= lmList[14][2] and lmList[13][2]):
                position = "down"

            if (lmList[12][2] and lmList[11][2] <= lmList[14][2] and lmList[13][
                2]) and position == "down":
                 position = "up"
                 count +=1
                 print(count)

        cv2.imshow("Push-up counter",cv2.flip(image,1))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
cap.release()