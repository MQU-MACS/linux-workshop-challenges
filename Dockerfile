FROM ubuntu

RUN apt-get update

RUN apt-get update && apt-get install -y awscli python3 python3-pip sudo gcc vim cron git

WORKDIR /root

COPY ./setup-files/ .

RUN pip3 install ctfcli

RUN pip3 install -r requirements.txt

# RUN python3 initialise.py
