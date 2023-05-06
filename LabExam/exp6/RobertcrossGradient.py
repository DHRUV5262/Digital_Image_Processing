import cv2
import numpy as np
# Load the image
img = cv2.imread('minions.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply Roberts Cross operator to detect edges
roberts = cv2.filter2D(gray, -1, np.array([[1, 0], [0, -1]], 
dtype=np.float32))
# Apply Sobel operator to detect edges
sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
# Display the original image and the edges detected by Roberts and Sobel operators
cv2.imshow('Original Image', img)
cv2.imshow('Roberts Cross Edges', roberts)
cv2.imshow('Sobel Edges', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
