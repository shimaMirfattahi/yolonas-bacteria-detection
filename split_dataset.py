import os
import shutil
import random
from pathlib import Path


base_dir = Path.home() / "Downloads" / "my_yolonas_data"
images_dir = base_dir / "train"
labels_dir = base_dir / "yolo_labels_corrected"
output_base = base_dir / "dataset"
split_ratio = 0.8  # 80% train, 20% val

#  Create output structure
for split in ["train", "val"]:
    (output_base / "images" / split).mkdir(parents=True, exist_ok=True)
    (output_base / "labels" / split).mkdir(parents=True, exist_ok=True)

#  Match images with their labels
image_files = list(images_dir.glob("*.png"))
random.shuffle(image_files)

split_index = int(len(image_files) * split_ratio)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

def copy_pair(image_list, split_name):
    for img_path in image_list:
        label_path = labels_dir / f"{img_path.stem}.txt"
        if not label_path.exists():
            print(f"⚠️ Missing label for: {img_path.name}")
            continue

        shutil.copy(img_path, output_base / "images" / split_name / img_path.name)
        shutil.copy(label_path, output_base / "labels" / split_name / label_path.name)

# Copy files
copy_pair(train_images, "train")
copy_pair(val_images, "val")

print(f"✅ Split complete: {len(train_images)} train images, {len(val_images)} val images")