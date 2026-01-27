import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Display images
cv2.imshow("Original Grayscale", gray)
cv2.imshow("Histogram Equalized", equalized)

# Plot histograms
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Histogram")
plt.hist(gray.ravel(), 256, [0,256])

plt.subplot(1,2,2)
plt.title("Equalized Histogram")
plt.hist(equalized.ravel(), 256, [0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
