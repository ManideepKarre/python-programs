#Day 4 

#list (core concept)
numbers =[1,2,3,4]
names= ["mani","Ravi","Ajay","Gopi"]

#Basic Operations
names.append("Kiran") #add
names.remove("Ravi") #delete
print(names[0]) #access
print(len(names)) #count

#how to loop through list

for name in names:
    print(names)

#Dictionaries like simplily using name rather than this look good

student= {
    "name" : "Mani",
    "age" : 20
}

#How to access values
print(student["name"])
print(student["age"])

#This are very important Dictionaries

students = [
    {"name": "Mani","age": 20},
    {"name": "Gopi","age": 22}

]
#now Loop through 

for s in students:
    print(s["name"],s["age"])

