# Изменить баланс белого, сделать более "холодную" картинку
import cv2

image_path = "input_images/photo4.jpg"
output_image_path = "output_images/cold_white_balance_image.jpg"

img = cv2.imread(image_path)

white_balancer = cv2.xphoto.createSimpleWB()
white_balancer.setP(10)
result_img = white_balancer.balanceWhite(img)

cv2.imwrite(output_image_path, result_img)
