import cv2

img = cv2.imread("input.jpg")
small = cv2.resize(img, None, fx=0.5, fy=0.5)
large = cv2.resize(img, None, fx=2, fy=2)

cv2.imshow("Small", small)
cv2.imshow("Large", large)
cv2.waitKey(0)
