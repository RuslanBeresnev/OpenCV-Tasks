import cv2

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/mirrored_image.jpg"

img = cv2.imread(image_path)

# Image reflection relative to the vertical
result = cv2.flip(img, flipCode=1)

cv2.imwrite(output_image_path, result)
