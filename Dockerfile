# Use official Python 3.12 image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . .

# Set environment variable
ENV ENV=$env

# Expose port 8000
EXPOSE 8000

# Run Django serverr
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
