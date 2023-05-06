#Import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('exp9.jpg',0)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
#define the kernal
kernal = np.ones((5,5),np.uint8)
#erosion of the image ie.removes pixels on object boundaries
erosion = cv2.erode(img,kernal,iterations = 1)
cv2.imshow('erosion method',erosion)
plt.imshow(erosion, cmap='gray')
plt.axis('off')
plt.show()
#Dilation adds pixels to the boundaries of objects in an image
dilation = cv2.dilate(img,kernal,iterations = 1)
plt.imshow(dilation, cmap='gray')
plt.axis('off')
plt.show()
#the definition of a morphological opening of an image is an erosion followed by a dilation,
opeing = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal,iterations = 1)
plt.imshow(opeing, cmap='gray')
plt.axis('off')
plt.show()
#The closing operation dilates an image and then erodes the dilated image
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal,iterations = 1)
plt.imshow(closing, cmap='gray')
plt.axis('off')
plt.show()
