#!/usr/bin/python
#########
# Cody Markelz
# July 28th, 2015
# markelz@gmail.com
# github, twitter, bitbucket: rjcmarkelz
#########

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import zbar
from PIL import Image

# get some info from the user
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
print args
# Load the image and display it
input_image = cv2.imread(args["image"])

# Convert original image to the L*a*b* color space for flower detection
cv2.imshow("original", input_image)
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
l_channel,a_channel,b_channel = cv2.split(lab_image)
# cv2.imshow("L",l_channel)
# cv2.imshow("a",a_channel) # focus on a channel because it provides best contrast for flowers
cv2.imshow("b",b_channel)

# take a look at the a channel histogram for pot detection, uncomment when finding correct threshold
hist = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

blur2 = cv2.bilateralFilter(b_channel, 5, 50, 100)
cv2.imshow("blur2", blur2)

(bT, b_thresh_image) = cv2.threshold(blur2, 195, 256, cv2.THRESH_BINARY)
cv2.imshow("b_channel Threshold Binary", b_thresh_image)

# canny edge detection on the thresholded image
canny_image2 = cv2.Canny(b_thresh_image, 100, 199, apertureSize = 3)
cv2.imshow("Canny 2", canny_image2)

plants = input_image.copy()
(cnts2, _) = cv2.findContours(b_thresh_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print "I count %d flowers" % (len(cnts2))

cnts2 = sorted(cnts2, key = cv2.contourArea, reverse = True)[:20]

#this part is hacky and could be cleaned up
cv2.drawContours(plants, cnts2, 0, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 1, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 2, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 3, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 4, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 5, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 6, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 7, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 8, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 9, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 10, (255, 255, 0), 4)


if len(cnts2) > 2:
    flowers = 'Flowering'
else:
    flowers = 'Not Flowering' 
print flowers

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(plants, flowers,(10,150), font, 5,(0,0,255),5)
cv2.imshow("plants", plants)

cv2.imwrite('flowering.png', plants)

cv2.waitKey(0)

######
# END SCRIPT
######



