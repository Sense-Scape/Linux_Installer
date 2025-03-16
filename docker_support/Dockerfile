FROM debian:11

# Update package lists
RUN apt-get update && apt-get upgrade -y

RUN apt-get install libsndfile1 -y
RUN apt-get install libsndfile1-dev -y
RUN apt-get install libasound2-dev -y

RUN apt-get install -y build-essential
RUN apt-get update && apt-get install -y cmake

RUN apt-get install -y libpng-dev
RUN apt-get install -y libgtest-dev

RUN apt-get install -y libgps-dev

CMD ["sh", "-c", "while true; do sleep 1; done"]

