import torch
import matplotlib.pyplot as plt
import cv2

# Loading in yolov5s - you can switch to larger models such as yolov5m or yolov5l, or smaller such as yolov5n
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
img = 'img1.png'  # or file, Path, PIL, OpenCV, numpy, list
results = model(img)
fig, ax = plt.subplots(figsize=(16, 12))
ax.imshow(results.render()[0])
plt.show()
