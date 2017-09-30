from threading import Thread


class ClientThread(Thread):

    def __init__(self, connection, address):
        Thread.__init__(self)

        self.connection = connection
        self.address = address

        print("[+] New connection from: " + str(address))

    def run(self):

        try:
            #TODO: Handle each thread response better.
            while True:
                data = self.connection.recv(1024).decode()
                print(str(self.address) + ": " + str(data))

                message = input("> ")
                self.connection.send(message.encode())
        #TODO: Figure out how to handle closed connections.
        except KeyboardInterrupt:
            print("Closed connection: " + self.address)
            self.connection.close()
