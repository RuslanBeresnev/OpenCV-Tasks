# Сместить изображение на 10 пикселей вправо
import cv2
import numpy as np

image_path = "input_images/photo1.jpg"
output_image_path = "output_images/image-move-to-right.jpg"

img = cv2.imread(image_path)

# find height and width of image
height, width = img.shape[:2]

move_horizontal = 10
move_vertical = 0
translation_matrix = np.float32([[1, 0, move_horizontal], [0, 1, move_vertical]])
result_img = cv2.warpAffine(img, translation_matrix, (width, height))

cv2.imwrite(output_image_path, result_img)
