"""Write a Python script that reads the “sequence.txt”.
In the file each line represents a DNA sequence or an RNA sequence. According to the sequence
type, the program must write the sequence to the “dna.txt” or “rna.txt” file.
Define a function that takes a sequence as a parameter. The function must return “DNA” or
“RNA” (string) according to the type of the sequence. Assume that no invalid sequences exist
in the file."""


def function(sequence):
    if "U" in sequence:
        return "RNA"
    else:
        return "DNA"


f = open("sequence.txt", "r")
dna = open("dna.txt", "w")
rna = open("rna.txt", "w")

for line in f:
    if function(line) == "DNA":
        dna.write(line)
    else:
        rna.write(line)

f.close()
dna.close()
rna.close()
