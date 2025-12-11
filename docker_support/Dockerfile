FROM debian:11

# Update package lists and install essential packages, including bash
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y bash

# c++ Apt Packages (Combined to reduce layers)
RUN apt-get install -y \
    libc6-dev \
    libsndfile1 \
    libsndfile1-dev \
    libasound2-dev \
    build-essential \
    cmake \
    libpng-dev \
    libgtest-dev \
    libgps-dev

# Python Apt Packages (Combined to reduce layers)
RUN apt-get install -y \
    libcap-dev \
    python3 \
    python3-pip \
    libcurl4-openssl-dev

WORKDIR /home
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- CHANGE MADE HERE ---
# Specify "/bin/bash" instead of "sh" to execute the loop command.
# This ensures the shell running the script is bash.
CMD ["/bin/bash", "-c", "while true; do sleep 1; done"]
# ------------------------
