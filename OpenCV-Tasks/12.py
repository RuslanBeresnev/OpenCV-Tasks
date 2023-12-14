# Изменить контраст изображения
import cv2

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/contrast_img.jpg"

img = cv2.imread(image_path)

alpha = 2  # Contrast control (1.0-3.0)
beta = 0  # Brightness control (0-100)
result_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

cv2.imwrite(output_image_path, result_img)
