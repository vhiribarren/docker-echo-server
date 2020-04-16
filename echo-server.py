#!/usr/bin/env python3

import os
import socket
import asyncio

PORT_ECHO_UDP = 4001
PORT_ECHO_TCP = 5001
PORT_HTTP = 80
INADDR_ANY = "0.0.0.0"


class UdpEchoServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode().strip()
        print(f'UDP: Received {message} from {addr}')
        self.transport.sendto(data, addr)


class TcpEchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f'TCP: Connection from {self.peername}')
        self.transport = transport

    def data_received(self, data):
        message = data.decode().strip()
        print(f'TCP: Received: {message} from {self.peername}')
        self.transport.write(data)


async def main():
    loop = asyncio.get_running_loop()

    print(f"Starting UDP server on port {PORT_ECHO_UDP}")
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UdpEchoServer(),
        local_addr=(INADDR_ANY, PORT_ECHO_UDP))

    print(f"Starting TCP server on port {PORT_ECHO_TCP}")
    tcp_server = await loop.create_server(
        lambda: TcpEchoServer(),
        INADDR_ANY, PORT_ECHO_TCP)

    async with tcp_server:
        await tcp_server.serve_forever()


asyncio.run(main())