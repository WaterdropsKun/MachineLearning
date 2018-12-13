import tensorflow as tf
import Resource.config.align.detect_face as detect_face

import numpy as np

import cv2 as cv


with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = detect_face.create_mtcnn(sess, None)


def detection(image):
    minsize = 20  # minimum size of face
    threshold = [0.6, 0.7, 0.7]  # three steps's threshold
    factor = 0.709  # scale factor

    margin = 0

    # detect with RGB image
    h, w = image.shape[:2]
    bounding_boxes, _ = detect_face.detect_face(image, minsize, pnet, rnet, onet, threshold, factor)
    if len(bounding_boxes) < 1:
        print("Can't detect face in the frame")
        return None
    print("Num %d faces detected"% len(bounding_boxes))

    bgr = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    for i in range(len(bounding_boxes)):
        det = np.squeeze(bounding_boxes[i, 0:4])
        bb = np.zeros(4, dtype=np.int32)
        # x1, y1, x2, y2
        bb[0] = np.maximum(det[0] - margin / 2, 0)
        bb[1] = np.maximum(det[1] - margin / 2, 0)
        bb[2] = np.minimum(det[2] + margin / 2, w)
        bb[3] = np.minimum(det[3] + margin / 2, h)
        cv.rectangle(bgr, (bb[0], bb[1]), (bb[2], bb[3]), (0, 0, 255), 2, 8, 0)
    cv.imshow("detected faces", bgr)
    return bgr


capture = cv.VideoCapture(0)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
out = cv.VideoWriter("./Resource/mtcnn_demo.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                             (np.int(width), np.int(height)), True)

while True:
    ret, frame = capture.read()
    if ret is True:
        frame = cv.flip(frame, 1)
        cv.imshow("frame", frame)
        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        result = detection(rgb)

        out.write(result)

        c = cv.waitKey(10)
        if c == 27:
            break
    else:
        break

cv.destroyAllWindows()