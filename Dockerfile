# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY ./app /app

# Install dependencies
RUN pip install fastapi uvicorn

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]