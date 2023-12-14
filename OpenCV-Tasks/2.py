# Найти все sift features точки на изображении
import cv2

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/image-with-key_points.jpg"

# Loading the image
img = cv2.imread(image_path)

# Applying SIFT detector
sift = cv2.SIFT_create()
key_points = sift.detect(img, None)

# Marking the keypoint on the image using circles
img = cv2.drawKeypoints(
    img, key_points, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.imwrite(output_image_path, img)
