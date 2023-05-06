
import cv2
import numpy as np
img = cv2.imread("minions.jpg")
img = cv2.resize(img, (512, 512))
images = []
for _ in range(20):
    img1 = img.copy()
    cv2.randn(img1, (0, 0, 0), (50, 50, 50))
    images.append(img+img1)
img_avg = np.zeros(img.shape, np.float32)
for i in images:
    img_avg = img_avg+i/20
    img_avg = np.array(np.round(img_avg), dtype=np.uint8)
cv2.imshow("Original image", img)
cv2.imshow("average image", img_avg)
cv2.waitKey(0)
