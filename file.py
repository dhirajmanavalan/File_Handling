# f = open("names.txt")

"""i want to read a file"""
# print(f.read())

""" i want to read first 4 characters """
# print(f.read(4))

""" i want to read first line """
# print(f.readline())

""" i want to read first And second line """
# print(f.readline())
# print(f.readline())

""" i want to read a full file using for loop """
# for i in f:
#     print(i)

# f.close()

"""If my file is not there """

# try:
#     f = open(file_name.txt)
# except:
#     print("The file is not there..")
# finally:
#     f.close()

"""Adding two files... --> Append -creates the file if it doesn't exist"""

# a = open("names.txt", "a")
# f = a.write("\nBrunoo")
# a.close()

# f = open("names.txt")
# print(f.read())
# f.close()


'''Write --> overwrite'''

# a = open("context.txt", "w")
# f = a.write("\nI deleteddd all files")
# a.close()

# f = open("context.txt")
# print(f.read())
# f.close()

'''Two ways to create a new file'''
'''Open a file for writing, creates the file if it does not exist'''