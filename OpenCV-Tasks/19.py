# Найти контуры на бинаризированном изображении
import cv2
import numpy as np

image_path = "input_images/photo4.jpg"
output_image_path = "output_images/contours_from_binary_image.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Image binarization
thresh = 75
_, threshed_img = cv2.threshold(gray_img, thresh, 255, 0)

# Contours finding on the binarized image
contours, _ = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# The empty image creating and drawing retrieved contours on it
contours_img = np.zeros(img.shape)
contours_color = (0, 0, 255)
cv2.drawContours(contours_img, contours, -1, contours_color, 1)

cv2.imwrite(output_image_path, contours_img)
