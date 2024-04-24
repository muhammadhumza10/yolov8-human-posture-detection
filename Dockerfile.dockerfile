# Base image with Python 3.12 (adjust if needed)
FROM python:3.12.1-slim

# Install dependencies for virtual environment creation
RUN apt-get update && apt-get install -y python3-venv

# Create virtual environment (replace with your actual directory)
WORKDIR /app
RUN python3 -m venv .venv

# Install dependencies within the virtual environment
RUN .venv/bin/pip install ultralytics pytest 

# Copy project code from Git repository (optional)
COPY --from=source . /app
RUN git config --global user.email "humzamuhammad14@gmail.com"
RUN git config --global user.name "muhammadhumza10"
RUN git clone https://github.com/muhammadhumza10/yolov8-human-posture-detection.git .

# Run the detection script
CMD ["python", "pose.py"]  # Replace with your actual script name
