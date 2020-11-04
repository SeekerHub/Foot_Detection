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

# frame = cv2.imread('images/polka_5.jpg')
frame = cv2.imread('images/orig_1.jpg')
frame = cv2.resize(frame, (400, 500))
blur = cv2.blur(frame, (5, 5))
hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

"""Red color"""
# low_red = np.array([0, 50, 120])
# high_red = np.array([10, 255, 255])
low_red = np.array([103, 86, 65])
high_red = np.array([145, 133, 128])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red = cv2.bitwise_and(frame, frame, mask=red_mask)


"""Yellow Color"""
low_yellow = np.array([25, 70, 120])
high_yellow = np.array([30, 255, 255])
yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

"""Blue color"""
low_blue = np.array([90, 60, 0])
high_blue = np.array([121, 255, 255])
blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    # #
"""Green color"""
low_green = np.array([47, 35, 0])
high_green = np.array([62, 247, 255])
green_mask = cv2.inRange(hsv_frame, low_green, high_green)
green = cv2.bitwise_and(frame, frame, mask=green_mask)


# contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(blue, contours, -1, (0, 0, 0), 3)

contours_2, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(green, contours_2, -1, (0, 0, 0), 3)

# contours_y, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(yellow, contours_2, -1, (0, 0, 0), 3)

# contours_r, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(red, contours_r, -1, (0, 0, 0), 3)

# print(len(contours))
# l = [cv2.contourArea(cnt) for cnt in contours if(cv2.contourArea(cnt))>300]
# print('Blue--->',len(l))

l_2 = [cv2.contourArea(cnt) for cnt in contours_2 if(cv2.contourArea(cnt))>300]
print("Green--->", len(l_2))
actual = 13-len(l_2)
print("Actual Length---->", (actual-1)*2.5,"cm")

# l_y = [cv2.contourArea(cnt) for cnt in contours_y if(cv2.contourArea(cnt))>300]
# print("Yellow-->", len(l_y))

# l_r = [cv2.contourArea(cnt) for cnt in contours_r if(cv2.contourArea(cnt))>300]
# print("Red-->", len(l_r))
# print(l_r)

cv2.imshow("Frame", frame)
# cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
# cv2.imshow("Yellow", yellow)
# cv2.imshow("Red", red)

key = cv2.waitKey(0)
# if key == 27:
#     break

cv2.destroyAllWindows()


