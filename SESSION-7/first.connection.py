import socket

# SERVER IP, PORT
IP = "192.168.1.37"
PORT = 8008

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

print(s)
print("End")
s.close()