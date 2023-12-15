# Повернуть изображение на 30 градусов вокруг заданной точки
import cv2

image_path = "input_images/photo1.jpg"
output_image_path = "output_images/rotated_by_30_degrees.jpg"

img = cv2.imread(image_path)

# Define the point around which we want to rotate the image
height, width = img.shape[:2]
defined_point = (int(width / 8), int(height / 8))

# Rotate by 30 degrees and reduce the image size by 0.3 to fit in image
rotation_matrix = cv2.getRotationMatrix2D(defined_point, -30, 0.3)
rotated = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imwrite(output_image_path, rotated)
