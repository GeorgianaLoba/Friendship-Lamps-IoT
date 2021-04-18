FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
# Use Python37
FROM python:3.7
# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
# Set the WORKDIR to be the folder
COPY . /app
WORKDIR /app

# Expose port 5000
EXPOSE 8080
ENV PORT 8080

# Run the web service on container startup.
#CMD exec gunicorn --bind :$PORT main_v1:app --workers 1 --threads 1 --timeout 60
ENTRYPOINT ["python", "mine.py"]