import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Unable to read camera.")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Color ranges
    red1 = cv.inRange(hsv, (0, 100, 100), (10, 255, 255))
    red2 = cv.inRange(hsv, (170, 100, 100), (180, 255, 255))
    red = red1 | red2

    green = cv.inRange(hsv, (35, 100, 100), (85, 255, 255))

    blue = cv.inRange(hsv, (90, 100, 100), (130, 255, 255))

    # Count pixels
    red_count = cv.countNonZero(red)
    green_count = cv.countNonZero(green)
    blue_count = cv.countNonZero(blue)

    detected_color = "No color detected"

    if red_count > 500 and red_count > green_count and red_count > blue_count:
        detected_color = "RED"

    elif green_count > 500 and green_count > red_count and green_count > blue_count:
        detected_color = "GREEN"

    elif blue_count > 500 and blue_count > red_count and blue_count > green_count:
        detected_color = "BLUE"

    cv.putText(
        frame,
        "Color: " + detected_color,
        (20, 50),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv.imshow("Camera Color Detection", frame)

    # Press Q to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()