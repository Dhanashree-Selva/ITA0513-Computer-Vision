import cv2, numpy as np

img = cv2.imread("input.jpg", 0)
dil = cv2.dilate(img, np.ones((5,5),np.uint8), 1)

cv2.imshow("Dilation", dil)
cv2.waitKey(0)
