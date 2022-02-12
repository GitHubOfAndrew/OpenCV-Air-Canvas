# THIS SCRIPT IS FOR PREPROCESSING THE WEBCAM FOOTAGE BEFORE WE OUTPUT IT

# IMPORT DEPENDENCIES

import numpy as np
from cv2 import cv2

# preprocessing script

# DETECT COLOR

def find_color(img, my_colors, my_color_vals, img_copy):
    # convert image colors to HSV space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    # masking and color detection
    for color in my_colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask, img_copy)
        cv2.circle(img_copy, (x, y), 20, my_color_vals[count], cv2.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, count])
        count += 1
        # output mask
    return new_points


#         cv2.imshow(str(color[0]), mask)

# FIND CONTOURS TO LOCALIZE OUR WRITING

def getContours(img, img_copy):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, width, height = 0, 0, 0, 0
    for cnt in contours:
        # FINDS AREA OF EACH CONTOUR
        area = cv2.contourArea(cnt)
        # DETECT MINIMAL AREA
        if area > 3000:
            # DRAWS EACH CONTOUR IT FINDS
            # cv2.drawContours(img_copy, cnt, -1, (255,0,0), 3)
            # FIND ARC LENGTH OF EACH SHAPE
            arc_length = cv2.arcLength(cnt, True)
            # FIND NUMBER OF CORNERS
            approx = cv2.approxPolyDP(cnt, 0.02 * arc_length, True)
            x, y, width, height = cv2.boundingRect(approx)
    # center the color at the middle of the tip of colored pen
    return x + width // 2, y

# DRAW

def draw(img_copy, my_points, my_color_vals):
    for point in my_points:
        cv2.circle(img_copy, (point[0], point[1]), 10, my_color_vals[point[2]], cv2.FILLED)
