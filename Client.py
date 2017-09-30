#! /usr/bin/env python3

import sys
import socket


class Client:

    # Define some understandable constants
    IP = socket.AF_INET
    IP6 = socket.AF_INET6
    TCP = socket.SOCK_STREAM
    UDP = socket.SOCK_DGRAM

    def __init__(self, host, port):

        # Please define the server address and port on initialisation.
        self.host = host
        self.port = port

    def run(self):

        # Create the socket and connect to host at specified port.
        my_sock = socket.socket(self.IP, self.TCP)
        my_sock.connect((self.host, self.port))

        # Show initial prompt
        message = input("> ")
        try:
            while True:
                # Start loop sending and receiving data.
                my_sock.send(message.encode())

                data = my_sock.recv(1024).decode()
                print("Received from server: " + data)

                message = input("> ")
        except KeyboardInterrupt:
            # Ctrl+C to exit program.
            print("\nKeyboardInterrupt received. Closing...")
            my_sock.close()
            sys.exit()


if __name__ == "__main__":

    client = Client("127.0.0.1", 5001)

    client.run()
