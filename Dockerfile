# Use official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Use gunicorn to serve the app on port 8080 (as expected by Azure)
CMD ["gunicorn", "-b", "0.0.0.0:8081", "app:app"]
