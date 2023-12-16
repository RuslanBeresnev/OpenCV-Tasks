# Сделать гамма-преобразование
import cv2
import numpy as np

image_path = "input_images/photo3.jpg"
output_image_path = "output_images/gamma_corrected_img.jpg"

img = cv2.imread(image_path)

# Gamma parameter
gamma = 1.5

# Creating a conversion table (Look-Up Table)
gamma_table = np.array([((i / 255.0) ** (1.0 / gamma)) * 255 for i in np.arange(0, 256)]).astype(np.uint8)

# Gamma conversion applying using cv2.LUT
gamma_corrected_img = cv2.LUT(img, gamma_table)

cv2.imwrite(output_image_path, gamma_corrected_img)
