import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Capture.jpg", 0)
x, y = img.shape
z = np.zeros((x, y))
for i in range(0, x):
    for j in range(0, y):
        if (img[i][j] > 50 and img[i][j] < 150):
            z[i][j] = 255
else:
    z[i][j] = img[i][j]
# cv2.imwrite("write.jpg", z)
slicing = np.hstack((img, z))
cv2.imwrite("write.jpg", slicing)
cv2.imshow("Slicing", slicing)
cv2.waitKey(0)
cv2.destroyAllWindows()
