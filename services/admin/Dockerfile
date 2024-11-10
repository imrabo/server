# Use the official Python image from the Docker Hub
FROM python:latest-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (e.g., build tools)
RUN apk add --no-cache build-base

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the app will run on (FastAPI default is 8000)
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
