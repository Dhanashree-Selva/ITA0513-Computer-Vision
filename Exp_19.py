import cv2, numpy as np

img = cv2.imread("input.jpg", 0)
ero = cv2.erode(img, np.ones((5,5),np.uint8), 1)

cv2.imshow("Erosion", ero)
cv2.waitKey(0)
