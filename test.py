# from ultralytics import YOLO

# def test_model_prediction():
#     # Load a model
#     model = YOLO('model\\yolov8n-pose.pt')  # load an official model

#     # Predict with the model
#     source = 'videos\\crowd_walking.mp4'

#     # Perform prediction
#     model.predict(source, save=False, imgsz=320, conf=0.5)

#     # Assert that the prediction completes without errors
#     assert True  # Placeholder assertion for test completeness


from ultralytics import YOLO
import cv2

def test_model_prediction():
    # Load a model
    model = YOLO('model\\yolov8n-pose.pt')  # load an official model

    # Define chunk size in frames
    chunk_size = 100  # Adjust this value based on your needs

    # Open the video source
    source = 'videos\\crowd_walking.mp4'
    cap = cv2.VideoCapture(source)

    # Initialize result list
    merged_results = []

    # Loop through video in chunks
    while True:
        # Read a chunk of frames
        frames = []
        for _ in range(chunk_size):
            ret, frame = cap.read()
            if not ret:
                break  # Reached end of video
            frames.append(frame)

        # Check if frames were read
        if not frames:
            break

        # Process the chunk of frames with Ultralytics
        results = model(frames, imgsz=320, conf=0.5)  # Assuming model accepts list of frames

        # Merge results with previous results
        if merged_results:
            merged_results.extend(results)
        else:
            merged_results = results

        # Release memory for processed frames
        for frame in frames:
            del frame

        # Exit loop if video ends
        if not ret:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    # Assert that the prediction completes without errors
    assert True  # Placeholder assertion for test completeness
