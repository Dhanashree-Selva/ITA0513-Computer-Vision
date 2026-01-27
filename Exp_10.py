import cv2

img = cv2.imread("input.jpg")
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Rotated", rot)
cv2.waitKey(0)
