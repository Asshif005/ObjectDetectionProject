from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train3/weights/best.pt")

# Test on an image
results = model.predict(
    source="coco128.v10i.yolov8/test/images",
    save=True,
    conf=0.25
)

print("Detection completed!")