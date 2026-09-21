import cv2

# Open the video
video = cv2.VideoCapture("moving_video.mp4")

# Background subtractor
background = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

object_id = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Detect moving objects
    mask = background.apply(frame)

    # Remove shadows/noise
    _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        # Ignore very small objects
        area = cv2.contourArea(contour)

        if area < 500:
            continue

        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)

        # Draw bounding box
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Calculate center
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw center point
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (0, 0, 255),
            -1
        )

        # Display object ID
        cv2.putText(
            frame,
            "Object",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

    # Display output
    cv2.imshow("Moving Object Tracking", frame)

    # Press Q to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()