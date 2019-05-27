from Seq import Seq

sequence1 = Seq('AGTC')
sequence2 = Seq('GGT')
sequence3 = sequence1.complement()
sequence4 = sequence3.reverse()


#Main program

#operation for sequence 1
print("Sequence 1: ", sequence1.strbase)
print("  Length: ", sequence1.len())
print("  Bases count: ", 'A:', sequence1.count('A'), 'G:', sequence1.count('G'), 'T:', sequence1.count('T'), 'C:', sequence1.count('C'))
print("  Bases percentages: ", 'A:', sequence1.perc('A'), 'G:', sequence1.perc('G'), 'T:', sequence1.perc('T'), 'C:', sequence1.perc('C'))

#operation for sequence 2
print("Sequence 2: ", sequence2.strbase)
print("  Length: ", sequence2.len())
print("  Bases count: ", 'A:', sequence2.count('A'), 'G:', sequence2.count('G'), 'T:', sequence2.count('T'), 'C:', sequence2.count('C'))
print("  Bases percentages: ", 'A:', sequence2.perc('A'), 'G:', sequence2.perc('G'), 'T:', sequence2.perc('T'), 'C:', sequence2.perc('C'))

#operation for sequence 3
print("Sequence 3: ", sequence3.strbase)
print("  Length: ", sequence3.len())
print("  Bases count: ", 'A:', sequence3.count('A'), 'G:', sequence3.count('G'), 'T:', sequence3.count('T'), 'C:', sequence3.count('C'))
print("  Bases percentages: ", 'A:', sequence3.perc('A'), 'G:', sequence3.perc('G'), 'T:', sequence3.perc('T'), 'C:', sequence3.perc('C'))

#operation for sequence 4
print("Sequence 4: ", sequence4.strbase)
print("  Length: ", sequence4.len())
print("  Bases count: ", 'A:', sequence4.count('A'), 'G:', sequence4.count('G'), 'T:', sequence4.count('T'), 'C:', sequence4.count('C'))
print("  Bases percentages: ", 'A:', sequence4.perc('A'), 'G:', sequence4.perc('G'), 'T:', sequence4.perc('T'), 'C:', sequence4.perc('C'))