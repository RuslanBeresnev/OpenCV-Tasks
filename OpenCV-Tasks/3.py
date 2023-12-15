# Найти canny edges на изображении
import cv2

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/image-with-canny-edges.jpg"

# Loading the image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Find edges depending on thresholds
edges_img = cv2.Canny(img, 75, 125)

cv2.imwrite(output_image_path, edges_img)
