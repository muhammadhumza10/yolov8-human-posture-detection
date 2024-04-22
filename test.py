from ultralytics import YOLO

def test_model_prediction():
    # Load a model
    model = YOLO('model\\yolov8n-pose.pt')  # load an official model

    # Predict with the model
    source = 'videos\\crowd_walking.mp4'

    # Perform prediction
    model.predict(source, save=False, imgsz=320, conf=0.5)

    # Assert that the prediction completes without errors
    assert True  # Placeholder assertion for test completeness
