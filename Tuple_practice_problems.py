Student_data ={"name":"David","age":13,"marks":87}
# Convert the following dictionary into JSON formate
import json
Student_data ={"name":"David","age":13,"marks":87}
print(type(Student_data))
data = json.dumps(Student_data)
print(data)
print(type(data))

# Access the value of age from the given data
data = json.loads(data)
print(data["age"])

# Pretty print following JSON data
data = json.dumps(Student_data,indent=4,separators=(",","="))
print(data)

# Sort the following JSON keys and write them into a file
f = open("demo.json","w")
data = json.dumps(Student_data,indent=4,sort_keys=True)
f.write(data)

print("the data has been added to the file")


