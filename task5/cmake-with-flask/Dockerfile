FROM ubuntu
RUN groupadd -r proj && useradd -r -g proj techproguser
WORKDIR /PROJECT
COPY . .
RUN apt-get update && \
    apt-get install -y \
        g++ \
        libboost-dev libboost-program-options-dev \
        cmake \
    && \
    cmake . && make
