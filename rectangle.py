import cv2
import numpy as np

# Track mouse coordinates and drawing state
drawing = False  # True if mouse is pressed down
ix, iy = -1, -1  # Initial x, y coordinates when clicked

# Create a black window background
img = np.zeros((600, 800, 3), dtype=np.uint8)
img_backup = img.copy()


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img

    # 1. Left mouse button pressed down: Record start position
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # 2. Mouse moving: Show live preview of the rectangle size
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Copy backup image to erase old preview lines while dragging
            img = img_backup.copy()
            # Draw temporary preview rectangle (Blue, thickness 2)
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)

    # 3. Left mouse button released: Finalize the permanent shape
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Save the drawn shape onto the backup image layer permanently
        cv2.rectangle(img_backup, (ix, iy), (x, y), (0, 255, 0), 3)
        img = img_backup.copy()


# Set up window and link mouse listener
cv2.namedWindow("Mouse Paint Window")
cv2.setMouseCallback("Mouse Paint Window", draw_rectangle)

print("Instructions:")
print("- CLICK AND DRAG your mouse to draw rectangles.")
print("- Press 'c' to CLEAR the screen.")
print("- Press 'q' to EXIT.")

while True:
    cv2.imshow("Mouse Paint Window", img)
    key = cv2.waitKey(1) & 0xFF

    # Reset screen
    if key == ord("c"):
        img_backup = np.zeros((600, 800, 3), dtype=np.uint8)
        img = img_backup.copy()
        print("Screen cleared.")

    # Break loop
    elif key == ord("q") or key == 27:
        break

cv2.destroyAllWindows()
