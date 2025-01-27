# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app directory into the container
COPY . /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Default command to run the application
CMD ["python", "app/app.py"]

