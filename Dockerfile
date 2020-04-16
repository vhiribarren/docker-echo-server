FROM alpine:3.11
RUN apk add python3

EXPOSE 4001/udp
EXPOSE 5001/tcp
EXPOSE 8080/tcp

ADD echo-server.py /echo-server.py
CMD ["python3", "-u","/echo-server.py"]