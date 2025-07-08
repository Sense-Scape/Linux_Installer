FROM debian:11

# Update package lists
RUN apt-get update && apt-get upgrade -y

# c++ Apt Packages
RUN apt-get install libsndfile1 -y
RUN apt-get install libsndfile1-dev -y
RUN apt-get install libasound2-dev -y

RUN apt-get install -y build-essential
RUN apt-get update && apt-get install -y cmake

RUN apt-get install -y libpng-dev
RUN apt-get install -y libgtest-dev

RUN apt-get install -y libgps-dev

# Python Apt Packages
RUN apt-get install -y libcap-dev
RUN  apt-get install -y python3 python3-pip

WORKDIR /home
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "while true; do sleep 1; done"]

