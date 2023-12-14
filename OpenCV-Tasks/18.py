# Сделать бинаризацию изображения
import cv2

image_path = "input_images/photo4.jpg"
output_image_path = "output_images/binary_image.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, result_img = cv2.threshold(gray_img, 127, 255, 0)

cv2.imwrite(output_image_path, result_img)
