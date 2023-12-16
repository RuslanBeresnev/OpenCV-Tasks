# Сделать размытие изображения
import cv2

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/blurred_image.jpg"

img = cv2.imread(image_path)

blurred_img = cv2.GaussianBlur(img, (31, 31), 0)

cv2.imwrite(output_image_path, blurred_img)
