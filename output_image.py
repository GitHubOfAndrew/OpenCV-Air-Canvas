# SCRIPT FOR OUTPUTTING OUR AIR CANVAS

import numpy as np
from cv2 import cv2
import process as pro

framewidth = 640
frameheight = 480

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)

# define maximum, minimum saturation values for orange, purple, green
my_colors = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]

# WRITE COLORS IN BGR FORMAT (BLUE,GREEN,RED) corresponding to colors above
my_color_vals = [[51, 153, 255],
                 [255, 102, 178],
                 [0, 255, 0]]

# CALL THE PROCESS FUNCTION
pro.process(cap, my_colors, my_color_vals)