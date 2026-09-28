import cv2
import numpy as np

# Create a blank image
height = 300
width = 900
img = np.zeros((height, width, 3), dtype=np.uint8)

# Red to Green
for x in range(300):
    ratio = x / 299
    red = int(255 * (1 - ratio))
    green = int(255 * ratio)
    img[:, x] = (0, green, red)   # BGR

# Green to Blue
for x in range(300, 600):
    ratio = (x - 300) / 299
    green = int(255 * (1 - ratio))
    blue = int(255 * ratio)
    img[:, x] = (blue, green, 0)  # BGR

# Blue section
for x in range(600, 900):
    img[:, x] = (255, 0, 0)       # Pure Blue

# Show the image
cv2.imshow("Red -> Green -> Blue Gradient", img)
cv2.waitKey(0)
cv2.destroyAllWindows()