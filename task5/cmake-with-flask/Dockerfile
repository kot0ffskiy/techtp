#--Flask--
FROM python
COPY app.py /opt/techprog
RUN pip install flask
RUN pip install argumentparser
ENTRYPOINT [ "python3" ]
CMD ["/opt/techprog/app.py", "--port", "8898", "--host", "0.0.0.0"]

#--CMake--
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