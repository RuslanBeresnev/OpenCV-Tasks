# Сделать гистограмную эквализацию
import cv2

image_path = "input_images/photo3.jpg"
output_color_image_path = "output_images/equal_histogram_img.jpg"
output_gray_image_path = "output_images/equal_histogram_gray_img.jpg"

img = cv2.imread(image_path)

# For color images
channels = cv2.split(img)
equalized_channels = [cv2.equalizeHist(channel) for channel in channels]
result_img = cv2.merge(equalized_channels)

cv2.imwrite(output_color_image_path, result_img)

# For grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result_gray_img = cv2.equalizeHist(gray_img)

cv2.imwrite(output_gray_image_path, result_gray_img)
