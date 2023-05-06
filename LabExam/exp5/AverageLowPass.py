import cv2
import numpy as np
img=cv2.imread("salt&paperNoise.jpg")
Kernel_3 = np.ones((5,5),dtype=np.float32)/25
output = cv2.filter2D(img,-1,Kernel_3)
output1= cv2.GaussianBlur(img,(5,5),1)
cv2.imshow("image org", img)
cv2.imshow("image gussuan",output1)
cv2.imshow("image filter2D",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
