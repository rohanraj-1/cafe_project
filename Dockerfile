# Use lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy python file into container
COPY cafe_project.py .

EXPOSE 8080

# Command to run the app
CMD ["python", "cafe_project.py"]

