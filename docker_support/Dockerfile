# Base image for Raspberry Pi 3B (armhf architecture)
FROM ubuntu:22.04

# Update package lists
RUN apt-get update && apt-get upgrade -y

RUN apt-get install libsndfile1 -y
RUN apt-get install libsndfile1-dev -y
RUN apt-get install libasound2-dev -y

RUN apt-get install -y build-essential
RUN apt-get update && apt-get install -y cmake

RUN apt-get install -y libpng-dev

CMD ["sh", "-c", "while true; do sleep 1; done"]
