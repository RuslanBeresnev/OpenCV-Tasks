# Изменить яркость изображения
import cv2

image_path = "input_images/photo3.jpg"
output_image_path = "output_images/brightened_image.jpg"

img = cv2.imread(image_path)

alpha = 1  # Contrast control (1.0-3.0)
beta = 75  # Brightness control (0-100)
brightened_image = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

cv2.imwrite(output_image_path, brightened_image)
