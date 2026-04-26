import cv2 as cv
from ultralytics import YOLO
import time
import winsound

# Initialize camera
video_capture = cv.VideoCapture(0)

# Load model
model = YOLO("yolov8n.pt")
class_names = model.names

# Settings
alert_cooldown = 1
last_alert_time = 0
MIN_AREA = 15000  # adjust for "closeness"

while True:
    success, frame = video_capture.read()

    if not success:
        print("Failed to capture image")
        break

    results = model(frame)

    best_detection = None
    max_area = 0

    # 🔍 Find the closest mouse only
    for result in results:
        for detection in result.boxes:
            class_id = int(detection.cls[0])
            class_name = class_names[class_id].lower()

            # Only consider mouse
            if class_name != "mouse":
                continue

            x1, y1, x2, y2 = map(int, detection.xyxy[0])
            box_area = (x2 - x1) * (y2 - y1)

            # Only consider close objects
            if box_area < MIN_AREA:
                continue

            # Keep the largest (closest)
            if box_area > max_area:
                max_area = box_area
                best_detection = detection

    # 🎯 Process only ONE object
    if best_detection is not None:
        class_id = int(best_detection.cls[0])
        class_name = class_names[class_id]
        confidence = float(best_detection.conf[0])

        # Alert
        if time.time() - last_alert_time > alert_cooldown:
            winsound.Beep(2000, 200)
            last_alert_time = time.time()

    # 📺 Show frame (with all boxes drawn for visualization)
    annotated_frame = results[0].plot()
    cv.imshow("Video Capture", annotated_frame)

    # Exit key
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
video_capture.release()
cv.destroyAllWindows()