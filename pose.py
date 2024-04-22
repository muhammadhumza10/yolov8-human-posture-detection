from ultralytics import YOLO

# Load a model
model = YOLO('model\\yolov8n-pose.pt')  # load an official model

# Predict with the model
source = 'videos\\crowd_walking.mp4' 

# Save the annotated image
model.predict(source, save=True, imgsz=320,conf=0.5)
