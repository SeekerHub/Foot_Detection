import cv2
import numpy as np


"""Add you image and mention the path"""
path = 'images/orig.jpg'
frame = cv2.imread(path)


"""Few modification/adjusting  the image"""
frame = cv2.resize(frame, (400, 500))
blur = cv2.blur(frame, (5, 5))
hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

"""Choose Color number"""
req = list(map(int, input().split()))
"""Set the margin according to the pattern/ gap between two pixel dots"""
margin = 2.5

"""A dictionary of colors along with its specific value"""
color = {
    1: [[], []],
    2: [[0, 68, 0], [16, 255, 255]],
    10: [[16, 194, 0], [28, 255, 255]],
    14: [[24, 170, 0], [60, 194, 200]],
    15: [[39, 57, 0], [60, 194, 200]],

}
# print(color[2][0])

"""Set the color"""
for i in req:
    low = np.array(color[i][0])
    high = np.array(color[i][1])
    color_mask = cv2.inRange(hsv_frame, low, high)
    color = cv2.bitwise_and(frame, frame, mask=color_mask)

    """Draw the contours around the detected circles"""
    contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(color, contours, -1, (0, 0, 0), 3)

    detected = [cv2.contourArea(cnt) for cnt in contours if (cv2.contourArea(cnt)) > 200]
    # print("Green--->", len(l_2))
    covered = (13 - len(detected)) - 1
    # actual = 13 - len(cont_list)
    actual_width = covered * margin
    print("Actual Length---->", actual_width, "cm")

    cv2.imshow("Frame", frame)
    cv2.imshow("color", color)

    key = cv2.waitKey(0)
# if key == 27:
#     break

cv2.destroyAllWindows()
