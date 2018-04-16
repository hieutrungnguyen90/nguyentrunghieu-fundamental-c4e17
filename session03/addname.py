hobbies = ["death note", "netflix", "teaching"]

addition = str(input("name an additional hobby: "))
hobbies.append(addition)
print(*hobbies, sep = ", ")
