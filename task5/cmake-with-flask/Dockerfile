FROM ubuntu
COPY . /opt/techprog
WORKDIR /opt/techprog
RUN apt-get update && \
    apt-get install -y \
        g++ \
        libboost-dev libboost-program-options-dev \
        cmake \
    && \
    cmake . && make
RUN useradd -m -s /bin/bash tp2022user
USER tp2022user