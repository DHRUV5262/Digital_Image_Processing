import cv2
import numpy as np

img1 = cv2.imread('BlackBorderCircle.png')
img2 = cv2.imread('BlackBorderHexagon.jpeg')

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))

#Logical And
bit_and = cv2.bitwise_and(img1,img2)

#Logical Or

bit_or = cv2.bitwise_or(img1,img2)

bit_xor = cv2.bitwise_xor(img1,img2)

bit_not = cv2.bitwise_not(img1 , img2)

#Display
cv2.imshow("Img1", img1)
cv2.imshow("Img2", img2)
cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.waitKey(10000)
cv2.destroyAllWindows()