# Use a smaller base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies first (for caching)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files AFTER copying full project
RUN python manage.py collectstatic --noinput

# Expose Django port
EXPOSE 8000

# Run migrations and start server
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

ENV DJANGO_SETTINGS_MODULE=crud.settings
CMD ["gunicorn", "crud.wsgi:application", "--bind", "0.0.0.0:8000"]
