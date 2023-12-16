# Применить операцию диляции к изображению
import cv2
import numpy as np

image_path = "input_images/photo4.jpg"
output_image_path = "output_images/dilated_image.jpg"

img = cv2.imread(image_path)

kernel = np.ones((7, 7))
result_img = cv2.dilate(img, kernel, iterations=1)

cv2.imwrite(output_image_path, result_img)
