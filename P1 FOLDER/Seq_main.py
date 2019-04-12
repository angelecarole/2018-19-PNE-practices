from Seq import Seq

#  create the sequences
s1 = Seq("AGTA")
l1 = s1.len()
print("Sequence 1: Len: {}".format(l1))
s2 = s1.complement()
l2 = s2.len()
print("Sequence 2: len: {}".format(l2))
nA = s1.count('A')
nT = s1.count('T')
nC = s1.count('C')
nG = s1.count('G')
print(" Bases Count: A:{}, T:{}, C:{}, G: {}".format(nA, nT, nC, nG ))

# Count the percentages
my_out2 = s1.perc()
print (my_out2)


"""

s2 = Seq("GTCCCTTTAACGATTTAG")
s3 = s1.complement()
s3 = Seq(s3)
s4 = s3.reverse()
s4 = Seq(s4)

# This is a list for organising the sequences
my_seq = [s1, s2, s3, s4]

number = 0

# Print the statistics requested
for sequence in my_seq:
    number += 1
    print("SEQUENCE: ", number)
    print("Length: ", sequence.len())
    print(sequence.count_base())
    print(sequence.perc())
"""
