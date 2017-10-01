#! /usr/bin/env python3

import sys
import socket


class Server:

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
        except socket.error as e:
            print(e)
            sys.exit()

        try:
            while True:
                my_sock.listen(1)
                # Enter waiting and accept incoming connection.
                conn, address = my_sock.accept()
                print("[+] Connection from: " + str(address))

                # Receive and decode the data.
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(address[0] + ": " + data)

                # Prompt for server's response, then encode and send it.
                message = data
                conn.send(message.encode())
        except KeyboardInterrupt:
            # Ctrl+C to exit program.
            print("\nKeyboardInterrupt received. Closing...")
            if conn:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                print("[-] " + address[0] + "disconnected.")
            sys.exit()
        except Exception:
            if conn:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                print("[-] " + address[0] + "disconnected.")
            raise

        conn.shutdown(socket.SHUT_RDWR)
        conn.close()


if __name__ == "__main__":

    server = Server("127.0.0.1", 5001)

    server.run()
