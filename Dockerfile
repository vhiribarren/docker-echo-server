FROM alpine:3.11

RUN apk add python3
COPY echo-server.py /echo-server.py

CMD ["python3", "-u","/echo-server.py"]

EXPOSE 4001/udp
EXPOSE 5001/tcp