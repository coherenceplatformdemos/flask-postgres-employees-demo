# Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV production
ENV GUNICORN_WORKERS 4

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

RUN pip install Flask-Migrate

# Copy the current directory contents into the container
COPY . .

# Run migrations.py from project root
CMD ["python", "migrations.py"]

# Run the application gunicorn --bind 127.0.0.1:8080 app:gunicorn_app
CMD ["gunicorn", "app:app.run_app"]