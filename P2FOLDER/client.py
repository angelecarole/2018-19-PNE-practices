import socket
from Seq import Seq

# SERVER IP, PORT
IP = "192.168.1.37"
PORT = 8000

while True:
    sequence = input('Enter a sequence:')
    sequence1 = Seq(sequence)
    comp = sequence1.complement()
    reverse = sequence1.reverse()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode('\n complement sequence: '))
    s.send(str.encode(comp.strbase))
    s.send(str.encode('\n reverse sequence: '))
    s.send(str.encode(reverse.strbase))
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: /n')
    print(msg)
    s.close()
