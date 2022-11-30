
defusername = "myuser"
defuserpassword = "1234"


while (True):
    useranme=input("User name :")
    password =input("Password : ")

    if((defusername == useranme) and (defuserpassword == password)):
        print("Welcome User")
        break

    elif((defusername != useranme) and (defuserpassword == password)):
        print("Wrong Username..")

    elif ((defusername == useranme) and (defuserpassword != password)):
        print("Wrong Pass...")
        print("Change password : ")
        change = input()

        if(change == "Y"):
            newpassword=input("Enter New Password : ")
            defuserpassword=newpassword
            print("Password Changed")

        elif(change == "N"):
            useranme = input("User name :")
            password = input("Password : ")
            if ((defusername == useranme) and (defuserpassword == password)):
                print("Welcome User")
                break



    else:
        print("Try Again")
