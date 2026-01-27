import cv2
img = cv2.imread("input.jpg")
rot = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("270 Rotation", rot)
cv2.waitKey(0)
