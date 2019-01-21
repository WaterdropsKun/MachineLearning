#coding = utf-8
import os

import cv2
import dlib
import face_recognition


# 人脸分类器
detector = dlib.get_frontal_face_detector()
# 人脸检测器
predictor = dlib.shape_predictor(
    "./Resource/config/shape_predictor_68_face_landmarks.dat"
)

total_face_name = []
total_face_encoding = []


def init():
    face_recognition_image_path = "./Resource/config/face_recognition"
    for file_name in os.listdir(face_recognition_image_path):
        print(face_recognition_image_path + "/" + file_name)

        total_face_encoding.append(
            face_recognition.face_encodings(
                face_recognition.load_image_file(face_recognition_image_path + "/" + file_name)
            )[0]
        )

        file_name = file_name[:(len(file_name) - 4)]
        total_face_name.append(file_name)


def faces_detection(imgTmp, img):
    gray = cv2.cvtColor(imgTmp, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)

    for face in faces:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        shape = predictor(imgTmp, face)
        for pt in shape.parts():
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)

    cv2.imshow("img", img)


def faces_recognition(imgTmp, img):
    face_locations = face_recognition.face_locations(imgTmp)
    face_encodings = face_recognition.face_encodings(imgTmp, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 人脸识别
        name = "Unknow"
        for i, v in enumerate(total_face_encoding):
            match = face_recognition.compare_faces(
                [v], face_encoding, tolerance=0.3
            )
            if match[0]:
                name = total_face_name[i]
                break

        # 人脸标签
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow("img", img)


if __name__ == '__main__':
    init()

    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if ret is True:
            imgTmp = img.copy()

            # faces_detection(imgTmp, img)
            faces_recognition(imgTmp, img)

            if cv2.waitKey(40) & 0xFF == ord('q'):
                cv2.imwrite("./Resource/config/face_recognition/img.jpg", imgTmp)
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
