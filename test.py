import os
from ultralytics import YOLO

def test_model_prediction():
    # Load a model
    model = YOLO('model\\yolov8n-pose.pt')  # load an official model

    # Predict with the model
    source = 'videos\\crowd_walking.mp4' 

    # Save the annotated image
    output_file = 'test_output.jpg'
    model.predict(source, save=output_file, imgsz=320, conf=0.5)

    # Check if the output file was created
    assert os.path.exists(output_file)

    # Clean up
    os.remove(output_file)
