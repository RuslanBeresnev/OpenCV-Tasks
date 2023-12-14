# Important NOTE:  Use opencv >=4.4
import cv2

image_path = "input_images/photo1.jpg"
output_image_path = "output_images/grayscale_image.jpg"

img = cv2.imread(image_path)

# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite(output_image_path, gray_img)
