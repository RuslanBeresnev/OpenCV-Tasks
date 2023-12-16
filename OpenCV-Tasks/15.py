# Изменить баланс белого, сделать более "теплую" картинку
import cv2
import numpy as np

image_path = "input_images/photo4.jpg"
output_image_path = "output_images/warm_image.jpg"

img = cv2.imread(image_path)

# Make the image warmer using color correction (increasing red channel and decreasing blue channel values)
warm_img = np.clip(img * [0.7, 1, 1.3], 0, 255)

cv2.imwrite(output_image_path, warm_img)
