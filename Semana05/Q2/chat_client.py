import socket
import select
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    IP_address = sys.argv[1]
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))

    while True:
        read_sockets, [], [] = select.select([sys.stdin, server], [], [])
        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                if(len(message) > 0):
                    print(message)
            else:
                message = sys.stdin.readline()
                server.send(bytearray(message.encode("UTF-8")))
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
