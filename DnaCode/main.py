

def makednacode(code):

    if code != "u":
        dna.append(code)
        print(dna)

    while code !="u":
        code = input("Enter Dna Code : ")
        if code=="a" or code=="t" or code=="g" or code=="c":
            dna.append(code)
            print(dna)

        elif code=="u":
            print(dna)
            break

        else:
            print("Invalid code...")
            print(dna)
            break


dna=[]

code=input("Enter Dna Code: ")

makednacode(code)