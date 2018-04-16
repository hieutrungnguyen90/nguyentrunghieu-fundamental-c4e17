c = input("enter a number for column")
r = input("enter a number for row")
for i in range(0,int(c)):
    for j in range(0, int(r)):
        if (i+j) % 2 != 0:
            print("0",end="")
        else:
            print("*", end="")
    print()
