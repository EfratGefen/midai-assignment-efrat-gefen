import torch
from pathlib import Path

# Loading the built-in model of YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

# Read the picture
img_path = 'input.jpg'
results = model(img_path)

#Prints the detection results.
print(results.pandas().xyxy[0])

# Saves the result with tags for identification
output_dir = Path("results")
output_dir.mkdir(exist_ok=True)
results.save(save_dir=output_dir)
