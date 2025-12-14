FROM python:3.10-slim

# Install system dependencies (nmap)
RUN apt-get update && apt-get install -y nmap

# Set working directory
WORKDIR /app

# Copy requirements first (important for Docker)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
