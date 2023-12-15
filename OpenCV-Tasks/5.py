# Перевести изорбражение в hsv
import cv2

image_path = "input_images/photo1.jpg"
output_image_path = "output_images/hsv_image.jpg"

img = cv2.imread(image_path)

# Converting image to hsv format
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite(output_image_path, hsv_img)
