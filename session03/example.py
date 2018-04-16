# # names = []
# # print(names)
# # print(type(names))
#
# name =["Canh]"]
# print(names)
#
names = ["Canh", "Hieu", "Duc Anh","Don"]
# # print(names)
# # Create
# # names.append("Nguyen")
# # print(names)
#
# names.append("new_name")
# print(names)
# Read

print(names[-1])

names[-1] ="Hieu dep trai"
print(names)

print(names[2])

print(len(names)) #len = length
for i in range(4):
    print(names[i])

#foreach
no = 1
for name in names:
    #print(no,". " ,name, sep ="")
    #string format
    message = "{0}. {1}".format(no, name)
    print(message)
    no += 1 # +=` --> no = no +1`
