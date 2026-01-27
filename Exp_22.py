import cv2
import numpy as np

path = r"C:/Users/admin/Documents/OpenCV_Lab_Programs/input.jpg"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found")
    exit()

kernel = np.ones((5,5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", img)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
