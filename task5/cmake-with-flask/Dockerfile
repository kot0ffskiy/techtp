FROM ubuntu
RUN groupadd -r proj && useradd -m -s /bin/bash -r -g proj techproguser
WORKDIR /opt/techprog
COPY . .
RUN apt-get update && \
    apt-get install -y \
        g++ \
        libboost-dev libboost-program-options-dev \
        cmake \
    && \
    cmake . && make