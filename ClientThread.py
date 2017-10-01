import socket
from threading import Thread


class ClientThread(Thread):

    def __init__(self, conn, address):
        Thread.__init__(self)

        self.conn = conn
        self.address = address

        print("[+] New connection from: " + address[0])

    def run(self):

        data = ""
        try:
            while data != "/quit":
                data = self.conn.recv(1024).decode()
                if not data:
                    break
                print(self.address[0] + ": " + data)

                message = data
                self.conn.send(message.encode())

            self.conn.shutdown(socket.SHUT_RDWR)
            self.conn.close()
            print("[-] Closed connection: " + self.address[0])
        except KeyboardInterrupt:
            self.conn.shutdown(socket.SHUT_RDWR)
            self.conn.close()
            print("[-] Closed connection: " + self.address[0])
        except Exception:
            raise
