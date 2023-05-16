# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements.txt file to the container
COPY mergeFiles.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the web server will run
EXPOSE 8008

# Run the Python script
CMD ["python", "mergeFiles.py"]