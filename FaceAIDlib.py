#coding = utf-8

import cv2
import dlib

# 人脸分类器
detector = dlib.get_frontal_face_detector()
# 人脸检测器
predictor = dlib.shape_predictor(
    "./Resource/config/shape_predictor_68_face_landmarks.dat"
)

def face_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)
    for face in faces:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        shape = predictor(img, face)
        for pt in shape.parts():
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)

    cv2.imshow("img", img)


cap = cv2.VideoCapture(0)
while (1):
    ret, img = cap.read()
    face_detection(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
