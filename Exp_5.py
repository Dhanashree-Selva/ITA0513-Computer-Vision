import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    img = cv2.imread(image_path)
    colors = ('b', 'g', 'r')

    plt.figure(figsize=(8,5))
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0,256])
        plt.plot(hist, color=col)
        plt.xlim([0,256])

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

# Call function
analyze_color_histogram("input.jpg")
