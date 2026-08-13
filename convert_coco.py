import json
import shutil
from pathlib import Path

# COCO dataset
COCO = Path("COCO2017")

# New YOLO dataset
OUTPUT = Path("COCO2017_YOLO")

# COCO's 80 object-detection classes
CLASSES = [
    "person", "bicycle", "car", "motorcycle", "airplane",
    "bus", "train", "truck", "boat", "traffic light",
    "fire hydrant", "stop sign", "parking meter", "bench",
    "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee",
    "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon",
    "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "couch", "potted plant", "bed", "dining table", "toilet",
    "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator",
    "book", "clock", "vase", "scissors", "teddy bear",
    "hair drier", "toothbrush"
]

# COCO category IDs are not simply 0-79,
# so create a mapping from COCO IDs to YOLO class IDs.
def convert_split(split):
    print(f"\nProcessing {split}...")

    annotation_file = COCO / "annotations" / f"instances_{split}2017.json"

    with open(annotation_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Map COCO category IDs to YOLO class IDs
    categories = sorted(data["categories"], key=lambda x: x["id"])
    category_map = {
        category["id"]: i
        for i, category in enumerate(categories)
    }

    images = {
        image["id"]: image
        for image in data["images"]
    }

    annotations_by_image = {}

    for ann in data["annotations"]:
        if "bbox" not in ann:
            continue

        if ann.get("iscrowd", 0) == 1:
            continue

        image_id = ann["image_id"]

        if image_id not in annotations_by_image:
            annotations_by_image[image_id] = []

        annotations_by_image[image_id].append(ann)

    image_output = OUTPUT / "images" / split
    label_output = OUTPUT / "labels" / split

    image_output.mkdir(parents=True, exist_ok=True)
    label_output.mkdir(parents=True, exist_ok=True)

    total = len(images)

    for count, (image_id, image_info) in enumerate(images.items(), 1):

        filename = image_info["file_name"]

        source_image = COCO / f"{split}2017" / filename
        destination_image = image_output / filename

        if source_image.exists():
            shutil.copy2(source_image, destination_image)

        label_file = label_output / f"{Path(filename).stem}.txt"

        width = image_info["width"]
        height = image_info["height"]

        with open(label_file, "w") as f:

            for ann in annotations_by_image.get(image_id, []):

                category_id = ann["category_id"]

                if category_id not in category_map:
                    continue

                x, y, w, h = ann["bbox"]

                # Convert COCO bbox → YOLO format
                x_center = (x + w / 2) / width
                y_center = (y + h / 2) / height
                box_width = w / width
                box_height = h / height

                class_id = category_map[category_id]

                f.write(
                    f"{class_id} "
                    f"{x_center:.6f} "
                    f"{y_center:.6f} "
                    f"{box_width:.6f} "
                    f"{box_height:.6f}\n"
                )

        if count % 1000 == 0:
            print(f"{count}/{total} images processed")

    print(f"{split} finished!")


# Convert training and validation sets
convert_split("train")
convert_split("val")

# Create data.yaml
yaml_file = OUTPUT / "data.yaml"

with open(yaml_file, "w", encoding="utf-8") as f:
    f.write(f"path: {OUTPUT.resolve()}\n")
    f.write("train: images/train\n")
    f.write("val: images/val\n")
    f.write(f"nc: {len(CLASSES)}\n")
    f.write("names:\n")

    for i, name in enumerate(CLASSES):
        f.write(f"  {i}: {name}\n")

print("\n===================================")
print("COCO → YOLO conversion completed!")
print(f"Dataset saved to: {OUTPUT.resolve()}")
print("===================================")