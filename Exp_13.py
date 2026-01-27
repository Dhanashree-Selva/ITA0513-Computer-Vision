import cv2, numpy as np

img = cv2.imread("input.jpg")
h, w = img.shape[:2]

pts1 = np.float32([[0,0],[w-1,0],[0,h-1]])
pts2 = np.float32([[50,50],[w-50,50],[50,h-50]])

M = cv2.getAffineTransform(pts1, pts2)
out = cv2.warpAffine(img, M, (w,h))

cv2.imshow("Affine", out)
cv2.waitKey(0)
