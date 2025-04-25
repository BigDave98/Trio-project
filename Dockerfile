# Python base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN  pip install -r requirements.txt

# Expose the port that the Flask app runs on
EXPOSE 8000

# Set environment variables required by Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Run the Flask application
CMD ["gunicorn", "run:app", "-b", "0.0.0.0:8000"]
