# Повернуть изображение на 45 градусов
import cv2

image_path = "input_images/photo1.jpg"
output_image_path = "output_images/rotated_by_45_degrees.jpg"

img = cv2.imread(image_path)

# find height, width and center of image
height, width = img.shape[:2]
center_of_image = (int(width / 2), int(height / 2))

# Rotate by 45 degrees and reduce the image size by 0.6 to fit in image
rotation_matrix = cv2.getRotationMatrix2D(center_of_image, -45, 0.6)
rotated = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imwrite(output_image_path, rotated)
