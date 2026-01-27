import cv2

img = cv2.imread("input.jpg", 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.waitKey(0)
