import cv2
img = cv2.imread("input.jpg")
rot = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("180 Rotation", rot)
cv2.waitKey(0)
