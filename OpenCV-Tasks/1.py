# Найти все orb features точки на изображении
import cv2

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/image-with-orb-key_points.jpg"

# Load the color image
image_color = cv2.imread(image_path)

# Convert the image to grayscale (for algorithm optimization)
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# Initialize the ORB detector
orb = cv2.ORB_create()

# Detect key points and their descriptors
key_points, descriptors = orb.detectAndCompute(image_gray, None)

# Marking the keypoint on the image using circles
result_image = cv2.drawKeypoints(image_gray, key_points, image_gray, color=(0, 0, 255),
                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Save result image to the file
cv2.imwrite(output_image_path, result_image)
