#--CMake--
FROM ubuntu
COPY . /opt/techprog
WORKDIR /opt/techprog
RUN apt-get update && \
    apt-get install -y \
        python3 python3-pip \
        g++ \
        cmake \
    && \
    cmake . && make
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install Flask
RUN pip install argumentparser
ENTRYPOINT [ "python3", "app.py", "--port", "8898", "--host", "0.0.0.0"]
RUN useradd -m -s /bin/bash tp2022user
USER tp2022user