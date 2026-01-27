import cv2

img = cv2.imread("input.jpg")

roi = img[50:200, 50:200]  

h, w = roi.shape[:2]

img[0:h, 0:w] = roi         
cv2.imshow("ROI Copy-Paste", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
