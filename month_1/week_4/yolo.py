from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_objects(self, image_path):
        results = self.model(image_path)
        return results

# Usage
detector = ObjectDetector("yolov8n.pt")
results = detector.detect_objects("https://ultralytics.com/images/bus.jpg")


# for result in results:
#     print(f"Detected {len(result.boxes)} objects")
#     boxes = result.boxes
#     for box in boxes:
#         class_id = int(box.cls[0])
#         confidence = float(box.conf[0])
#         print(f"Class ID: {class_id}, Confidence: {confidence}")
#     result.show()
    
for result in results:
    print(f"Detected {len(result.boxes)} objects")
    boxes = result.boxes
    for box in boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        print(f"Class ID: {class_id}, Confidence: {confidence}")
    result.show()