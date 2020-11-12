import cv2
import numpy as np

"""Add you image and mention the path"""
path = 'images/black_top_2.jpg'
frame = cv2.imread(path)

"""Few modification/adjusting  the image"""
frame = cv2.resize(frame, (340, 240))
blur = cv2.blur(frame, (5, 5))
hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

"""Choose Color number"""
# req = list(map(int, input().split()))
"""Set the margin according to the pattern/ gap between two pixel dots"""
margin = 2.1
num_dots = 9

"""A dictionary of colors along with its specific value"""
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
low_c = {
    1: [174, 157, 79],
    2: [104, 177, 69],
    3: [69, 226, 79],
    4: [19, 226, 26],
    5: [99, 247, 95],
    6: [148, 140, 79],
    7: [116, 111, 79],
    8: [58, 59, 172],
    9: [96, 74, 211],
    10: [98, 213, 142],
    11: [7, 145, 162],
    12: [39, 188, 0],
    13: [84, 17, 0],
}
high_c = {
    1:  [178, 255, 251],
    2:  [173, 255, 255],
    3:  [93, 255, 251],
    4:  [30, 255, 255],
    5:  [102, 255, 251],
    6:  [170, 255, 251],
    7:  [147, 255, 251],
    8:  [87, 255, 255],
    9:  [103, 255, 255],
    10: [100, 230, 176],
    11: [22, 255, 255],
    12: [46, 255, 255],
    13: [150, 164, 71]
}


# color = {
#     1: [[178, 106, 83], [179, 198, 255]],
#     2: [[19, 93, 0], [22, 255, 255]],
#     3: [[44, 37, 129], [73, 250, 255]],
#     4: [[108, 51, 0], [129, 255, 255]],
#     5: [[29, 125, 171], [49, 156, 231]],
#     6: [[34, 160, 147], [105, 215, 241]],
#     7: [[0, 81, 168], [19, 255, 255]],
#     8: [[167, 82, 0], [173, 222, 255]],
#     9: [[0, 21, 0], [67, 58, 97]],
#     10: [[23, 197, 0], [29, 255, 255]],
#     11: [[35, 32, 165], [47, 255, 213]],
#     12: [[76, 22, 171], [102, 41, 217]],
#     13: [[0, 0, 169], [102, 41, 217]],
#     14: [[19, 56, 188], [25, 97, 255]],
#     15: [[29, 156, 0], [37, 255, 255]],
#     16: [[37, 214, 141], [141, 249, 255]],
#     17: [[24, 166, 0], [26, 199, 188]],
#     18: [[0 , 71 , 0], [33 , 222 , 125]],
#     19: [[173, 147, 0], [177, 186, 194]],
#
# }
# print(color[2][0])

"""Set the color"""
store = []
for i in range(1, 14):
    frame = cv2.resize(frame, (340, 240))
    blur = cv2.blur(frame, (5, 5))
    hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    low = np.array(low_c[i])
    high = np.array(high_c[i])
    # print(low, high)
    color_mask = cv2.inRange(hsv_frame, low, high)
    color = cv2.bitwise_and(frame, frame, mask=color_mask)

    """Draw the contours around the detected circles"""
    contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(color, contours, -1, (0, 0, 0), 3)

    detected = [cv2.contourArea(cnt) for cnt in contours if (cv2.contourArea(cnt)) > 200]
    print("Detected--->", len(detected))
    if len(detected) >= num_dots:
        break
    store.append(len(detected))
    # cv2.imshow("Frame", frame)
    # cv2.imshow("color", color)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

print(len(store))
"""For Calculating length"""
max_length = len(store)*margin


"""For Calculating Width"""
max_width = min(store)
# print(max_width)
covered = (num_dots - max_width)
width = max_width * margin

print('Length------------->', max_length)
print("Width------------->", width)
# if key == 27:
#     break


