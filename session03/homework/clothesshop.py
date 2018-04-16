ouritems= ["T-shirt", "Sweater"]

Choice = str(input("Welcome to our shop, what do you want"))
if Choice == "R":
    for i in range(2):
        print(ouritems[i])

elif Choice == "C":
    Newitem= str(input("enter new item"))
    ouritems.append(Newitem)
    print(ouritems)

elif Choice == "U":
    ouritems[1] = str(input("enter new item"))
    print(ouritems)
