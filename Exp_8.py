import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

if img is None:
    print("Image not found")
    exit()

dil = cv2.dilate(img, np.ones((5,5),np.uint8), 1)

cv2.imshow("Dilated Image", dil)
cv2.waitKey(0)
cv2.destroyAllWindows()
