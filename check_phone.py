from pathlib import Path

labels_folder = Path("coco128.v10i.yolov8/train/labels")

phone_count = 0
total_objects = 0

for file in labels_folder.glob("*.txt"):
    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()

            if not parts:
                continue

            class_id = int(parts[0])
            total_objects += 1

            if class_id == 20:
                phone_count += 1

print("Cell phone objects:", phone_count)
print("Total objects:", total_objects)