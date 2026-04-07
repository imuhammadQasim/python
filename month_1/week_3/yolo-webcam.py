import cv2 as cv
from ultralytics import YOLO
cap = cv.VideoCapture(0)

model = YOLO('yolov8n.pt')

while True:
    success, img = cap.read()

    if not success:
        print("Failed to capture image")
        break
    
    result = model(img)

    annotated_frame = result[0].plot()

    # for r in result:
    #     for box in r.boxes:
    #         x1, y1, x2, y2 = map(int, box.xyxy[0])
    #         cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)

    cv.imshow('Video Capturing', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()