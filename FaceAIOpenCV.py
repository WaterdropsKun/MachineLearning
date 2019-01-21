import cv2


# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier("./Resource/config/haarcascade_frontalface_default.xml")


def faces_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 识别人脸
    faceRects = classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

    # 标记人脸
    color = (0, 255, 0)
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 框出人脸
            cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
            # 左眼
            cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
            # 右眼
            cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
            # 嘴巴
            cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                          (x + 5 * w // 8, y + 7 * h // 8), color)

    return img


if __name__ == '__main__':
    # 图片
    # filepath = "./Resource/jiance-2.png"
    # img = cv2.imread(filepath)
    # img_result = faces_detection(img)
    # cv2.imshow("img_result", img_result)
    # 视频
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()

        if ret is True:
            img_result = faces_detection(img)
            cv2.imshow("img_result", img_result)

            if cv2.waitKey(40) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()