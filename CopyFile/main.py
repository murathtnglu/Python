
def function(f):
    if f:
        copy=open("copy.txt","w")
        copy.write(f.read())
        return 1
    else:
        return 0



f=open("sequence.txt","r")

if function(f)==1:
    print("Dosya Acildi")
else:
    print("Dosya acilamadi")