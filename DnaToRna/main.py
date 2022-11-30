
def dnatorna(code):
    rnacode=dnacode

    while code != "u":
        for i in range(len(rnacode)):
            if  dnacode[i].lower() =="a":
                rnacode[i] = "u"

            elif dnacode[i].lower() =="t":
                rnacode[i] = "a"

            elif dnacode[i].lower()=="g":
                rnacode[i]="c"

            elif dnacode[i].lower() == "c":
                rnacode[i] = "g"

        return rnacode




dnacode=[]

code = input("Enter dna code : ")

for i in range(len(code)):
    dnacode.append(code[i])

print(dnatorna(code))