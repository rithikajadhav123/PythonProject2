import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Resize the image
resized = cv2.resize(img, (400, 400))

# Rotate the image 90 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Flip the image horizontally
flipped = cv2.flip(img, 1)

# Crop the image
cropped = img[50:250, 50:250]

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display all images
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.imshow("Rotated", rotated)
cv2.imshow("Flipped", flipped)
cv2.imshow("Cropped", cropped)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()