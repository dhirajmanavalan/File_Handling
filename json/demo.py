import csv
import json

file = "names.json"

# with open("json/names.json","r") as json_data:
#     file_data = json.load(json_data)
#     # print(file_data)

#     load_data = file_data["names"]
#     for i in load_data:
#         name = (i["firstname"])
#         age = (i["age"])
#         print(name,age)


"""Create new json file"""


# def write_json(data, filename="json/dhi.json"):
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)
        
# with open("json/names.json","r") as f1:
#     data = json.load(f1)
#     write_json(data)


'''how to append json file'''
# def write_json(data,filename = "json/dhi.json"):
#     with open(filename,"w") as json_file:
#         json.dump(data,json_file,indent=4)
        
# with open("json/dhi.json") as f:
#     data = json.load(f)
#     values = data["names"]
#     y = { "firstname" : "dhiraaa" , "age" : "25" }
    
#     values.append(y)
    
# write_json(data)

'''how to convert json to csv file'''

with open("json/names.json","r") as f:
    data = json.load(f)
    names = data["names"]
    
with open ("json/dhi.csv","w") as csv_file:
    fieldname = names[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldname)
    writer.writeheader()

for i in names:
    writer.writerow(i)