#! /usr/bin/env python3

import sys
import socket


class MyServer:

    # Define some understandable constants
    IP = socket.AF_INET
    IP6 = socket.AF_INET6
    TCP = socket.SOCK_STREAM
    UDP = socket.SOCK_DGRAM

    def __init__(self, host, port):

        # Please define the listening address and port on initialisation.
        self.host = host
        self.port = port

    def run(self):

        try:
            # Create the socket, bind it to the address and port, and listen for connection.
            my_sock = socket.socket(self.IP, self.TCP)
            my_sock.bind((self.host, self.port))
            my_sock.listen(1)
        except socket.error as e:
            print(e)
            sys.exit()

        try:
            # Enter waiting and accept incoming connection.
            connection, address = my_sock.accept()
            print("Connection from: " + str(address))

            while True:
                # Receive and decode the data.
                data = connection.recv(1024).decode()
                if not data:
                    break
                print("From connected user: " + str(data))

                # Prompt for server's response, then encode and send it.
                message = input("> ")
                connection.send(message.encode())
        except KeyboardInterrupt:
            # Ctrl+C to exit program.
            print("\nKeyboardInterrupt received. Closing...")
            connection.close()
            sys.exit()

        connection.close()


if __name__ == "__main__":

    server = MyServer("127.0.0.1", 5001)

    server.run()
