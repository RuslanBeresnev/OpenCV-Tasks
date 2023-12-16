# Сделать фильтрацию изображения при помощи Фурье преобразования, оставить только быстрые частоты
import cv2
import numpy as np

image_path = "input_images/photo2.jpg"
output_image_path = "output_images/Fourier_transform_fast_frequencies_image.jpg"

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 2-DFT (Two-Dimensional Fourier Transformation) applying
f_transform = np.fft.fft2(img)

# Shift of zero frequency to the center
f_transform_shifted = np.fft.fftshift(f_transform)
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)

# Create a mask for filtering (leaving only high frequencies)
rows, cols = img.shape
mask = np.ones((rows, cols), np.uint8)
# Circular window radius for high frequencies
r = 30
center = [rows // 2, cols // 2]
# Represent the image as a grid with x and y axes
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
# Remove low frequencies that are in the center within the window
mask[mask_area] = 0

# Multiplying the results of the Fourier transform by a mask
f_transform_filtered = f_transform_shifted * mask

# Apply an inverse frequency shift and then an inverse Fourier transform
filtered_img = np.fft.ifft2(np.fft.ifftshift(f_transform_filtered)).real

cv2.imwrite(output_image_path, filtered_img)
