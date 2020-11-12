import cv2
import numpy as np

# img = cv2.imread('images/polka.jpg')
#
# hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# low_blue = np.array([94, 80, 2])
# high_blue = np.array([126, 255, 255])
# blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
# blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

frame = cv2.imread('images/black_top.jpg')
# frame = cv2.imread('images/orig.jpg')
# frame = cv2.blur(frame, (5, 5))
frame = cv2.resize(frame, (340, 240))
blur = cv2.blur(frame, (5, 5))
hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

"""Red color"""
# color = {
#     1:  [[], []],
#     2:  [[0, 68, 0], [16, 255, 255]],
#     10: [[16, 194, 0], [28, 255, 255]],
#     14: [[24, 170, 0], [60,194,200]],
#     15: [[39,57,0], [60,194,200]],
#
# }
color = {
    1: [[174, 157, 79], [178, 255, 251]],
    2: [[104, 177, 69], [173, 255, 255]],
    3: [[69, 226, 79], [93, 255, 251]],
    4: [[19, 226, 26], [30, 255, 255]],
    5: [[99, 247, 95], [102, 255, 251]],
    6: [[148, 140, 79], [170, 255, 251]],
    7: [[116, 111, 79], [147, 255, 251]],
    8: [[58, 59, 172], [87, 255, 255]],
    9: [[96, 74, 211], [103, 255, 255]],
    10: [[98, 213, 142], [100, 230, 176]],
    11: [[7, 145, 162], [22, 255, 255]],
    12: [[39, 188, 0], [46, 255, 255]],
    13: [[84, 17, 0], [150, 164, 71]]
}

color_2 = {
    1: [[178, 106, 83], [179, 198, 255]],
    2: [[19, 93, 0], [22, 255, 255]],
    3: [[44, 37, 129], [73, 250, 255]],
    4: [[108, 51, 0], [129, 255, 255]],
    5: [[29, 125, 171], [49, 156, 231]],
    6: [[34, 160, 147], [105, 215, 241]],
    7: [[0, 81, 168], [19, 255, 255]],
    8: [[167, 82, 0], [173, 222, 255]],
    9: [[0, 21, 0], [67, 58, 97]],
    10: [[23, 197, 0], [29, 255, 255]],
    11: [[35, 32, 165], [47, 255, 213]],
    12: [[76, 22, 171], [102, 41, 217]],
    13: [[0, 0, 169], [102, 41, 217]],
    14: [[19, 56, 188], [25, 97, 255]],
    15: [[29, 156, 0], [37, 255, 255]],
    16: [[37, 214, 141], [141, 249, 255]],
    17: [[24, 166, 0], [26, 199, 188]],
    18: [[0, 71, 0], [33, 222, 125]],
    19: [[173, 147, 0], [177, 186, 194]],

}



"""Green color"""
# low_green = np.array([47, 35, 0])
# high_green = np.array([62, 247, 255])
low_green = np.array(color[3][0])
high_green = np.array(color[3][1])
green_mask = cv2.inRange(hsv_frame, low_green, high_green)
green = cv2.bitwise_and(frame, frame, mask=green_mask)

# contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(blue, contours, -1, (0, 0, 0), 3)

contours_2, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(green, contours_2, -1, (0, 0, 0), 3)


l_2 = [cv2.contourArea(cnt) for cnt in contours_2 if (cv2.contourArea(cnt)) > 200]
print(l_2)
print("Green--->", len(l_2))
# actual = 13 - len(l_2)
# print("Actual Length---->", (actual - 1) * 2.5, "cm")

# l_y = [cv2.contourArea(cnt) for cnt in contours_y if(cv2.contourArea(cnt))>300]
# print("Yellow-->", len(l_y))

# l_r = [cv2.contourArea(cnt) for cnt in contours_r if(cv2.contourArea(cnt))>300]
# print("Red-->", len(l_r))
# print(l_r)

cv2.imshow("Frame", frame)

cv2.imshow("Green", green)


key = cv2.waitKey(0)
# if key == 27:
#     break

cv2.destroyAllWindows()
