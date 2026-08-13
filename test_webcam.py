import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train3/weights/best.pt")

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    results = model(frame, conf=0.25)

    annotated_frame = results[0].plot()

    cv2.imshow("COCO 2017 Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()