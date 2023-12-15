# Найти контуры на изображении, применив фильтры (Собеля или Лапласиан)
import cv2
import numpy as np

image_path = "input_images/photo2.jpg"
output_sobel_image_path = "output_images/sobel_image.jpg"
output_laplacian_image_path = "output_images/laplacian_image.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel
kernel_sobel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
img_sobel_first = cv2.filter2D(gray_img, -1, kernel_sobel)
result_img_sobel = cv2.filter2D(img_sobel_first, -1, kernel_sobel)
cv2.imwrite(output_sobel_image_path, result_img_sobel)

# Laplacian
kernel_laplacian = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
img_laplacian_first = cv2.filter2D(gray_img, -1, kernel_laplacian)
result_img_laplacian = cv2.filter2D(img_laplacian_first, -1, kernel_laplacian)
cv2.imwrite(output_laplacian_image_path, result_img_laplacian)
