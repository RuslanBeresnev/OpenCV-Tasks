# Изменить цветовую палитру по заданному шаблону
import cv2

image_path = "input_images/photo4.jpg"
output_image_path = "output_images/color_corrected_image.jpg"

img = cv2.imread(image_path)
image_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Color correction
hue_shift = 20
image_hsv[:, :, 0] = (image_hsv[:, :, 0] + hue_shift) % 360  # Color correction via hue value shifting

image_bgr = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite(output_image_path, image_bgr)
