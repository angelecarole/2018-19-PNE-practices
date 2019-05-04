
my_file = open("filedna.py")
my_dna = my_file.read()

dna_count = my_dna.count("A") + my_dna.count("T") + my_dna.count("G") + my_dna.count("C")
print(dna_count)
print(my_dna.count("A") )
print(my_dna.count("T"))
print(my_dna.count("G"))
print(my_dna.count("C"))
