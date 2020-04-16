# Docker Echo Server

Simple docker container which just echo data sent on UDP and TCP port.

Can be useful when doing some network tests.

Available on Docker Hub as `vhiribarren/echo-server`

Run memo:

    $ docker run --rm -p 4001:4001/udp -p 5001:5001 vhiribarren/echo-server

Test memo:

    $ nc -u -4 localhost 4001 # may be necessary to force IPv4 on MacOS
    $ nc localhost 5001

Maintenance memo:

    $ docker build -t vhiribarren/echo-server
    $ docker login
    $ docker push vhiribarren/echo-server