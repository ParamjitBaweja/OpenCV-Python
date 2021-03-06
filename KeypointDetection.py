#!/usr/bin/env python
import numpy as np
import cv2

# Load the image
img = cv2.imread('/home/paramjit/catkin_ws/src/opencv_ros/src/test1.jpg')
print(img)

# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the ORB key points and compute the descriptors
orb = cv2.ORB_create()
keyPoints, descriptors = orb.detectAndCompute(gray, None)

# Paint the key points over the original image
result = cv2.drawKeypoints(img, keyPoints, None, color=(0, 255, 0), flags=0)

# Display the results
cv2.imshow('Key points', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
