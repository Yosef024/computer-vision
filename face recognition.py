
import threading

import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

reference_img = cv2.imread("WIN_20240618_19_41_02_Pro.jpg")  # use your own image here



face_match = 0


def check_face(frame):
    global face_match
    try:
        frame_path = "temp_frame.jpg"
        cv2.imwrite(frame_path, frame)
        result = DeepFace.verify(img1_path=frame_path, img2_path="WIN_20240618_19_41_02_Pro.jpg")
        res2=DeepFace.verify(img1_path=frame_path, img2_path="WIN_20240619_13_21_34_Pro.jpg")
        res3 = DeepFace.verify(img1_path=frame_path, img2_path="WIN_20240621_20_37_22_Pro.jpg")
        res4 = DeepFace.verify(img1_path=frame_path, img2_path="WIN_20240621_20_41_32_Pro.jpg")



        if result['verified']:
            face_match = 1
        elif res2['verified']:
            face_match=2
        elif res3['verified']:
            face_match=3
        #elif res4['verified']:
            #face_match=4
        else:
            face_match = 0
    except:
        face_match = 0
        print(f"Error in face verification:")

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 50 == 0:
            try:
                check_face(frame)
            except Exception as e:
                print(f"Exception occurred: {e}")
        counter += 1
        if face_match==1:
            cv2.putText(frame, "yosef", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        elif face_match==2:
            cv2.putText(frame, "ebrahim", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 200, 0), 3)
        elif face_match==3:
            cv2.putText(frame, "ghena", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
        #elif face_match == 4:
            #cv2.putText(frame, "joman", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)
        else:
            cv2.putText(frame, "someone else", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
