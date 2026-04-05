from ultralytics import YOLO
import numpy as np


# image = np.zeros((100,100))
# print(image)
model = YOLO("yolov8n.pt")

result = model('image.png' , save=True)
names = model.names
count = 0
objectStats = {}
for box in result[0].boxes:
    # print(box)
    cls_id  = int(box.cls[0])
    name = names[cls_id]
    confidence = box.conf[0]
    if name == "person":
        count +=1
    
    if name in objectStats:
        objectStats[name] +=1
    else:
        objectStats[name] = 1

    print(f"Object: {name} | Confidence: {confidence}")


print(f"Total person which are detected are {count}")
print("Object Map:", objectStats)

if objectStats: 
    most_common = max(objectStats, key=objectStats.get)
    most_common_count = objectStats[most_common]
    print(f"\nMost common object: {most_common} ({most_common_count} times)")
else:
    print("No common object found.")


result[0].show()

# # task 3 

# # result = model('image.png', classes=[0])


# from ultralytics import YOLO
# import cv2

# model = YOLO("yolov8n.pt")

# result = model('image.png', classes=[0])
# img = result[0].orig_img

# count = 0

# for box in result[0].boxes:
#     confidence = float(box.conf[0])

#     if confidence > 0.7:
#         count += 1

#         x1, y1, x2, y2 = map(int, box.xyxy[0])

#         # Draw rectangle
#         cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

#         # Put confidence text
#         cv2.putText(
#             img,
#             f"person {confidence:.2f}",
#             (x1, y1 - 10),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.6,
#             (0, 255, 0),
#             2
#         )

# print(f"Total persons detected (conf > 0.7): {count}")

# cv2.imshow("Filtered Result", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()