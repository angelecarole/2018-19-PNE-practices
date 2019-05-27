import socket

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print some information about the socket
print()
print("Socket created:")
print(s)
print("End")