# Use the specified base image
FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS base

# Update system and install required packages
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    socat \
    python3-pip

# Create challenge directory
RUN mkdir /challenge

# Copy application files and scripts
COPY app.py setup-challenge.py /app/
COPY start.sh /opt/
COPY requirements.txt /app/

# Set working directory
WORKDIR /app/
ARG FLAG 
RUN chmod +x /opt/start.sh
RUN python3 setup-challenge.py

RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the necessary port
EXPOSE 5000

# Command to start the application
CMD ["/opt/start.sh"]
