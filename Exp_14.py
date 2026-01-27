import cv2, numpy as np

img = cv2.imread("input.jpg")
h, w = img.shape[:2]

pts1 = np.float32([[0,0],[w,0],[0,h],[w,h]])
pts2 = np.float32([[50,50],[w-50,0],[0,h-50],[w-50,h-50]])

M = cv2.getPerspectiveTransform(pts1, pts2)
out = cv2.warpPerspective(img, M, (w,h))

cv2.imshow("Perspective", out)
cv2.waitKey(0)
