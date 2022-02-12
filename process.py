# THIS SCRIPT IS FOR PROCESSING THE IMAGE BEFORE WE DISPLAY IT

# IMPORT DEPENDENCIES

import numpy as np
from cv2 import cv2
import preprocess as pre
import os
from datetime import datetime as dt

# PROCESSING SCRIPT

# process FUNCTION
# INPUTS:
# cap - a video capture object
# my_colors - an array indicating the saturation values for the colors we are using
# my_color_vals - BGR values of the exact color that we will draw with

def process(cap, my_colors, my_color_vals):
    my_points = []
    # Check if camera opened successfully
    print(cap.isOpened())
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    # Read until video is completed

    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        # HAVE ANOTHER IMAGE TO DRAW CONTOURS ON
        imgResult = frame.copy()
        new_points = pre.find_color(frame, my_colors, my_color_vals, imgResult)
        if len(new_points) != 0:
            for points in new_points:
                my_points.append(points)
        if len(my_points) != 0:
            pre.draw(imgResult, my_points, my_color_vals)

        # Display the resulting frame
        if not ret:
            print('Not able to receive video stream...')
            break
        cv2.imshow('Frame', imgResult)
        # Press Q on keyboard to exit and to save a screenshot of the current work
        if cv2.waitKey(1) & 0xFF == ord('q'):
            now = dt.now().strftime('%Y-%m-%d, %H hr %M min %S sec')
            # save_path = os.getcwd() + '\\Air Canvas' + str(now) + '.jpg'
            save_path = os.path.join(os.getcwd(), 'Air Canvas ' + now + '.jpg')
            print(save_path)
            cv2.imwrite(save_path, imgResult)
            break

    cap.release()
    cv2.destroyAllWindows()