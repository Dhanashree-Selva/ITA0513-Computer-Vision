import cv2, time

cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, f = cap.read()
    if not ret: break
    cv2.imshow("Video", f)
    time.sleep(0.05)   # slow → increase | fast → decrease
    if cv2.waitKey(1)==27: break

cap.release()
cv2.destroyAllWindows()
