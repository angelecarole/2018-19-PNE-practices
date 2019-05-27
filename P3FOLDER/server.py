import socket

PORT = 8080
IP = "192.168.1.37"
#Maximum number of clients that can connect to this server
MAX_OPEN_REQUEST = 5

def check(s):
    for i in s:
        if i != "A" and i != "T" and i != "C" and i != "G":
            seq = "bad"
            break
        else:
            seq = "good"
    if seq == "bad":
        print("ERROR")
    else:
        print("OK")

def length(s):
    return len(s)

def complement(s):

    complement_seq = ""
    for i in s:
        if i == "A":
            complement_seq += "T"
        elif i == "T":
            complement_seq += "A"
        elif i == "C":
            complement_seq += "G"
        elif i == "G":
            complement_seq += "C"
    return complement_seq

def reverse(s):
    rev_seq = s[::-1]
    return rev_seq

def count_A(s):
    num_A = 0
    for i in s:
        if i == "A":
            num_A += 1
    i = num_A
    return i

def count_T(s):
    num_T = 0
    for i in s:
        if i == "T":
            num_T += 1
    i = num_T
    return i

def count_C(s):
    result_C = 0
    for x in s:
        if x == "C":
            result_C += 1
    x = result_C
    return x

def count_G(s):
    num_G = 0
    for i in s:
        if i == "G":
            num_G += 1
    i = num_G
    return i

def perc_A(s):
    seq_len = len(s)
    result_A = 0
    for x in s:
        if x == "A":
            result_A += 1
    if seq_len > 0:
        per_A = round(100.0 * result_A / seq_len, 1)
    else:
        per_A = 0
    return per_A

def perc_T(s):
    seq_len = len(s)
    result_T = 0
    for i in s:
        if i == "T":
            result_T += 1
    if seq_len > 0:
        per_T = round(100.0 * result_T / seq_len, 1)
    else:
        per_T = 0
    return per_T

def perc_C(s):
    seq_len = len(s)
    result_C = 0
    for i in s:
        if i == "C":
            result_C += 1
    if seq_len > 0:
        per_C = round(100.0 * result_C / seq_len, 1)
    else:
        per_C = 0
    return per_C

def perc_G(s):
    seq_len = len(s)
    result_G = 0
    for i in s:
        if i == "G":
            result_G += 1
    if seq_len > 0:
        per_G = round(100.0 * result_G / seq_len, 1)
    else:
        per_G = 0
    return per_G

def process_client(cs):

    #ECHO SERVER
    #Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    message = msg.split("\n")

    print("Message from the client: {}". format(message))

    if message[0] == "":
        print("ALIVE")
    else:
        check(message[0])
        for i in message:
            if i == "len":
                len = length(message[0])
                print("The length of the sequence is: {}".format(len))
                cs.send(str.encode(msg))
            elif i == "complement":
                comp = complement(message[0])
                print("The complement of the sequence is: {}".format(comp))
                cs.send(str.encode(msg))
            elif i == "reverse":
                rev = reverse(message[0])
                print("The reverse  is: {}".format(rev))
                cs.send(str.encode(msg))
            elif i == "countA":
                count = count_A(message[0])
                print("The number of A bases is: {}".format(count))
                cs.send(str.encode(msg))
            elif i == "countT":
                count = count_T(message[0])
                print("The number of T bases is: {}".format(count))
                cs.send(str.encode(msg))
            elif i == "countC":
                count = count_C(message[0])
                print(" number of C base is: {}".format(count))
                cs.send(str.encode(msg))
            elif i == "countG":
                count = count_G(message[0])
                print(" number of G bases is: {}".format(count))
                cs.send(str.encode(msg))
            elif i == "percA":
                perc = perc_A(message[0])
                print(" percentage of A bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
            elif i == "percT":
                perc = perc_T(message[0])
                print(" percentage of T bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
            elif i == "percC":
                perc = perc_C(message[0])
                print(" percentage of C bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
            elif i == "percG":
                perc = perc_G(message[0])
                print(" percentage of G bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
    cs.close()

#Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

#To listen to the client's requests
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}". format(serversocket))

while True:

    print("Waiting for connections at: {}, {}". format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    #-- Process the client request
    print("Attending client: {}". format(adress))

    process_client(clientsocket)


    #-- Close the socket
    clientsocket.close()