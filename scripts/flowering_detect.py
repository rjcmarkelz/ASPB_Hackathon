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
# output_image_name = args["name"]
# print output_image_name

################
################
# Detect Plants
################
################

# Convert original image to the L*a*b* color space for flower detection
cv2.imshow("original", input_image)
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
l_channel,a_channel,b_channel = cv2.split(lab_image)
# cv2.imshow("L",l_channel)
# cv2.imshow("a",a_channel) # focus on a channel because it provides best contrast for flowers
cv2.imshow("b",b_channel)

# take a look at the a channel histogram for pot detection, uncomment when finding correct threshold
hist = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

# Plot the histogram
# plt.figure()
# plt.title("b Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# hist = cv2.calcHist([a_channel], [0], None, [256], [0, 256])

# Plot the histogram
# plt.figure()
# plt.title("a Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# blur image to get better edges
# blur = cv2.bilateralFilter(a_channel, 9, 50, 100)
# cv2.imshow("blur", blur)
# blur = cv2.bilateralFilter(a_channel, 5, 50, 100)
# cv2.imshow("blur", blur)

blur2 = cv2.bilateralFilter(b_channel, 5, 50, 100)
cv2.imshow("blur2", blur2)

# hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
# # Plot the histogram
# plt.figure()
# plt.title("blur Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# pick peaks to threshold around
# (T, thresh_image) = cv2.threshold(blur, 75, 110, cv2.THRESH_BINARY)
# cv2.imshow("Threshold Binary", thresh_image)

# canny edge detection on the thresholded image
# canny_image = cv2.Canny(thresh_image, 100, 200, apertureSize = 3)
# cv2.imshow("Canny", canny_image)

# set kernal to "Dilate" the lines from the canny image
# this step is necessary to bring out the edges of the pots
# play with the size of the array and the number of iterations for various results
# kernel = np.ones((5,5), np.uint8)
# dilation = cv2.dilate(canny_image, kernel, iterations = 2)
# # cv2.imshow("Canny dilation", dilation)

# # # print lines
# input_copy2 = input_image.copy()

# # set parameters for HoughLinesP 
# # also play with these to get more or less numbers of lines
# minLineLength = 10000
# maxLineGap = 40
# linesP = cv2.HoughLinesP(dilation, 1, np.pi/180, 100, minLineLength, maxLineGap)
# hist = cv2.calcHist([blur2], [0], None, [256], [0, 256])

# Plot the histogram
# 



# threshold image based on a_channel region that provides the most contrast
# (aT, a_thresh_image) = cv2.threshold(blur, 113, 100, cv2.THRESH_BINARY)
# cv2.imshow("a_channel Threshold Binary", a_thresh_image)

(bT, b_thresh_image) = cv2.threshold(blur2, 200, 256, cv2.THRESH_BINARY)
cv2.imshow("b_channel Threshold Binary", b_thresh_image)

# take a look at the a channel histogram for pot detection, uncomment when finding correct threshold
# hist = cv2.calcHist([a_thresh_image], [0], None, [256], [0, 256])

# # Plot the histogram
# plt.figure()s
# plt.title("a_thresh Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# canny edge detection on the thresholded image
# canny_image = cv2.Canny(a_thresh_image, 110, 200, apertureSize = 3)
# cv2.imshow("Canny", canny_image)

# canny edge detection on the thresholded image
# canny_image2 = cv2.Canny(b_thresh_image, 100, 199, apertureSize = 3)
# cv2.imshow("Canny 2", canny_image2)

# plants = input_image.copy()
# (cnts, _) = cv2.findContours(a_thresh_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
(cnts2, _) = cv2.findContours(b_thresh_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# print "I count %d plants" % (len(cnts))
print "I count %d flowers" % (len(cnts2))

# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:20]
cnts2 = sorted(cnts2, key = cv2.contourArea, reverse = True)[:20]

cv2.drawContours(plants, cnts2, 0, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 1, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 2, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 3, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 4, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 5, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 6, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 7, (255, 255, 0), 4)
cv2.drawContours(plants, cnts2, 9, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 10, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 11, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 12, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 13, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 14, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 15, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 17, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 18, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 19, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 20, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 21, (255, 255, 0), 4)
# cv2.drawContours(plants, cnts2, 22, (255, 255, 0), 4)

# cv2.imshow("plants", plants)
# # Add QR CODE Print
# font = cv2.FONT_HERSHEY_SIMPLEX
# thickness = 3
# black = (0,)*3
# size = 1
# left = (10,50)
# left2 = (20, 100)
# cv2.putText(plants, symbol.data, left, font, size, black, thickness) 


if len(cnts2) > 2:
    flowers = 'Flowering'
else:
    flowers = 'Not Flowering' 
cv2.putText(plants, flowers, left2, font, size, black, thickness) 


# cv2.imshow("input_image", plants)
# # output_image = "%s_4.tif" % symbol.data

# cv2.imwrite("ouput_flower_testX.png", plants)
# # keep images open to view the results
cv2.waitKey(0)

######
# END SCRIPT
######
