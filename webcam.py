from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train3/weights/best.pt")

# Start webcam
model.predict(
    source=0,      # 0 = default webcam
    show=True,     # Show live video
    conf=0.25
)