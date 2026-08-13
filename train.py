from ultralytics import YOLO

def main():
    # Load pretrained YOLOv8 Nano model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="coco128.v10i.yolov8/data.yaml",
        epochs=150,
        imgsz=640,
        batch=16,
        device=0,
        workers=0
    )

if __name__ == "__main__":
    main()