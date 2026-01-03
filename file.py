f = open("names.txt")

""" i want to read a file"""
# print(f.read())

""" i want to read first 4 characters """
# print(f.read(4))

""" i want to read first line """
# print(f.readline())

""" i want to read first And second line """
# print(f.readline())
# print(f.readline())

""" i want to read a full file using for loop """
for i in f:
    print(i)
