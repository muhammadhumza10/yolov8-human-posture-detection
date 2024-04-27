# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Ultralytics and dependencies
RUN pip install --upgrade pip && \
    pip install pytest && \
    pip install ultralytics

# Command to run pose.py
CMD ["python", "pose.py"]
