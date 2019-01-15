FROM ubuntu:16.04
COPY ./src /src
COPY ./wait-for-it/wait-for-it.sh /bin
RUN chmod +x /bin/wait-for-it.sh

WORKDIR /src

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y netcat

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]