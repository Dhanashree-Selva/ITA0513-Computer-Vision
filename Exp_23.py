import cv2
import numpy as np

img = cv2.imread(r"C:/Users/admin/Documents/OpenCV_Lab_Programs/input.jpg",
                 cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Image not found"); exit()

kernel = np.ones((9,9), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original", img)
cv2.imshow("Top Hat", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
