FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    socat \
    pip

RUN mkdir /challenge

COPY app.py setup-challenge.py requirements.txt /app/
RUN mkdir /app/static; mkdir /app/junk
COPY static/ /app/static/
COPY junk/ /app/junk/

COPY start.sh /app/
RUN chmod +x /app/start.sh

WORKDIR /app/
# RUN tar czvf /challenge/artifacts.tar.gz picker-I.py

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py
RUN pip install --no-cache-dir -r requirements.txt
# The start.sh script starts a socat listener on port 5555, that connects to the
# python script.
EXPOSE 5000
# PUBLISH 5000

# CMD ["/app/start.sh"]
CMD ["python3", "/app/app.py"]
