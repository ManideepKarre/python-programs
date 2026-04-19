name = input("What's your name?")
age= int(input("How olde are you"))

print(f"Hello  {name} ")
print("you are " +str( age) + " years")
print(f"you are {age} years old")
if age >=18:
    print("you are major")
else:
    print("you are minor")

while True:
    age= int(input("enter your age: "))
    if age>=20:
        print("you need to help you parents")
    elif age<=17:
            print("wait for one more year")
    else:
        print("You cant go")
    
    again = input("Try again (yes/no): ")
    if again.lower()!="yes":
        break


name= input("Enter you name: ")

while True:
     try:
          age = int(input("what is you age: "))
          break
     except ValueError:
          print("What is your age man ")
print(f"Hey {name} you are good to go")
print(f"This is your {age}  ")

if age>=19:
     print("What are you looking for Major")
else:
     print("You are just an Major")

while True:
     try: 
        age = int(input("Try again: "))
     except ValueError:
          print(" You are good to go")
          continue
     if age>=20:
          print("You are about become a vauled person ")
     elif age>19:
          print("Just wait for more one Year")
     else:
          print("You are good to go")
     again = input("You can try once (yes/no): ")
     if again.lower()!="yes":
          print("Nothing Else")
          break

