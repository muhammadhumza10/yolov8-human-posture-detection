FROM ultralytics/yolov8:latest  

# Copy your inference code directory
COPY . /app

# Install any additional python dependencies (if needed)
# RUN pip install -r requirements.txt  # Example for requirements file

# Set the working directory within the container
WORKDIR /app

# Expose the port used by your application (if applicable)
# EXPOSE 8080  # Example for port 8080

# Command to execute your python script
CMD ["python", "pose.py"]  
