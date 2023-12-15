# Изменить яркость изображения
import cv2
import numpy as np

image_path = "input_images/photo3.jpg"
output_image_path = "output_images/brightened_image.jpg"

img = cv2.imread(image_path)

# Lightening with gamma-correction
gamma = 0.5
brightened_image = np.clip(np.power(img / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)

cv2.imwrite(output_image_path, brightened_image)
