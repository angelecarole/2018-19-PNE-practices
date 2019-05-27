import socket

# SERVER IP, PORT
IP = "192.168.1.37"
PORT = 8000

while True:
    class Seq:

        def __init__(self, strmessage):
            print("sequence created!")

            self.strmessage = strmessage

        def rev_comp(self):

            comp_seq = ""
            for i in self.strmessage:
                if i == "A":
                    comp_seq += "T"
                elif i == "T":
                    comp_seq += "A"
                elif i == "C":
                    comp_seq += "G"
                elif i == "G":
                    comp_seq += "C"

            rev_seq = comp_seq[::-1]
            return rev_seq


    class Message(Seq):
        pass


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data. No strings can be send, only bytes
    # It necesary to encode the string into bytes
    message = Message(input("Type your message: "))
    seq = message.strmessage

    sequence = message.rev_comp()

    s.send(str.encode(sequence))

    # Receive data from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(msg)

