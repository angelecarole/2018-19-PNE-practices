import http.client
import json


HOSTNAME = "rest.ensembl.org"
endpoint = "/sequence/id/ENSG00000165879?content-type=application/json"
method = "GET"
headers= {'User-Agent':'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(method, endpoint, None, headers)

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
text = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(text)
seq = person['seq']
print(seq)

print('the length of the sequence is: ', len(seq))

baseT = 0
baseA = 0
baseC = 0
baseG = 0


for i in seq:
    if i == 'T':
        baseT += 1
    elif i == 'A':
        baseA += 1
    elif i == 'C':
        baseC += 1
    else:
        baseG += 1

print('Number of T bases in the FRAT1 gene: ', baseT)

if (baseT > baseA) and (baseT > baseC) and (baseT > baseG):
    predominantbase = 'Thymine'
elif (baseA > baseT) and (baseA > baseC) and (baseA > baseG):
    predominantbase = 'Adenine'
elif (baseG > baseT) and (baseG > baseA) and (baseG > baseC):
    predominantbase = 'Guanine'
else:
    predominantbase = 'Cytosine'

print('The most abundant base is: ', predominantbase)


def perc(base):
    seq_len = len(seq)
    result = 0
    for i in seq:
        if i == base:
            result += 1
    if seq_len > 0:
        perc = round(100.0 * result / seq_len, 1)
    else:
        perc = 0
    return perc

perc_A = perc('A')
perc_T = perc('T')
perc_G = perc('G')
perc_C = perc('C')

print('The percentage of A : ', perc_A)
print('The percentage of T : ', perc_T)
print('The percentage of G : ', perc_G)
print('The percentage of C: ', perc_C)


