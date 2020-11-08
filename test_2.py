import cv2
import numpy as np


def empty(a):
    pass


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

path = "images/polka_dots.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 140)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 27, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    img = cv2.resize(img, (240, 300))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    imgCany = cv2.Canny(mask, 100, 200)

    contours, hierarchy = cv2.findContours(imgCany, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgCany, contours, 3, (0, 255, 0), 3)
    print(len(contours))
    # hull = cv2.convexHull(cnt)
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[7]
    cnt_2 = contours[6]
    print(areas)

    # for cnt in contours:
    #     # get convex hull
    #     hull = cv2.convexHull(cnt)
    #     cv2.drawContours(img, [hull], -1, (0, 0, 255), 1)
    # hull = cv2.convexHull(cnt, returnPoints=False)
    # defects = cv2.convexityDefects(cnt, hull)
    # print(defects.shape)

    """Drawing a bounding box rectangle"""
    x, y, w, h = cv2.boundingRect(cnt)
    x1, y1, w1, h1 = cv2.boundingRect(cnt_2)
    img = cv2.rectangle(img, (x, y), (x + w1 + w, y + h ), (255, 0, 0), 2)
    print("Length due to inclination--->", y+h)
    print("Width---->", x+w1+w)
    hypo = y+h
    """Measure by the measuring tool in the box or the box fixed height"""
    height = 125
    """Note: we will have to make sure the height of the box so to set the camera accordingly"""
    actual_length = (hypo**2 - height**2)**0.5
    print("actual_length----->",actual_length)

    # leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    # rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    #
    # print("=====", leftmost, rightmost, "-------------")
    # ellipse = cv2.fitEllipse(cnt)
    # im = cv2.ellipse(imgResult, ellipse, (0, 25, 0), 2)

    """Line drawing"""
    # img = cv2.line(img, leftmost, rightmost, (0, 0, 255), 3)

    # cv2.drawContours(img, hull, -1, (255, 0, 0), 4)
    imgStack = stackImages(1.2, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)
    cv2.waitKey(1)
