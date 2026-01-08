import csv

# with open("fleet.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["id", "name", "dob"])
#     writer.writerow([1, "dhiraj", 24])


with open("fleet.csv","r") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)
    