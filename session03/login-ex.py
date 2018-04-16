import getpass

while True:

    username = input("what is your username?")
    password = getpass.getpass("what is your password")

    if username != str("c4e"):
        print("wrong username")
    else:
        if password!= "codethechange":
            print("wrong password")
        else:
            print("welcome")
