# Use the official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install libgl1-mesa-glx package
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Create a virtual environment named my_venv
RUN python -m venv my_venv

# Activate the virtual environment
RUN /bin/bash -c "source my_venv/bin/activate"

# Install Python dependencies from requirements.txt inside the virtual environment
RUN pip install pytest && \
    pip install ultralytics

# Copy the Python script into the container
COPY pose.py .

# Set the entrypoint command to run the Python script
CMD ["python", "pose.py"]
