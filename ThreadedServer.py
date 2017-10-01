#! /usr/bin/env python3

import sys
import socket

import ClientThread


class ThreadedServer:

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
            # Create the socket and bind it to the address and port.
            my_sock = socket.socket(self.IP, self.TCP)
            my_sock.bind((self.host, self.port))
        except socket.error as e:
            print(e)
            sys.exit()

        try:
            while True:
                my_sock.listen(5)
                # Enter waiting and accept incoming connection.
                connection, address = my_sock.accept()

                newthread = ClientThread.ClientThread(connection, address)
                newthread.start()
        except KeyboardInterrupt:
            # Ctrl+C to exit program.
            print("\nKeyboardInterrupt received. Closing...")
            connection.close()
            sys.exit()

        connection.close()


if __name__ == "__main__":

    server = ThreadedServer("127.0.0.1", 5001)

    server.run()
