name = input("What's your name?")
age= int(input("How olde are you"))

print(f"Hello  {name} ardham ayithundhi ha")
print("you are " +str( age) + " years")
print(f"you are {age} years old")
if age >=18:
    print("Cong you are major")
else:
    print("pukka mi thammudu tho adukoku")

while True:
    age= int(input("enter your age: "))
    if age>=20:
        print("you need to help you parents")
    elif age<=17:
            print("Dengutha bittlu chusthy")
    else:
        print("Kotukute thondharaga paduthadhi")
    
    again = input("Malli adugu (yes/no): ")
    if again.lower()!="yes":
        break


name= input("Ni Peru Chpu thammudu: ")

while True:
     try:
          age = int(input("ni age entha chpu nean chptha nuv bittlu chudal ha odh ha ani: "))
          break
     except ValueError:
          print("Arey Lanjakoduka ni age chpu bey ")
print(f"Thammudu {name} nachinav ra")
print(f"ni modda {age} eni years nuchi undhi ")

if age>=19:
     print("Bittlu chudali ani undhi ha?")
else:
     print("arey nik videos chupiyali ani undhi kani ni modda ki antha age ledhu")

while True:
     try: 
        age = int(input("Malli nik chance isthuna : "))
     except ValueError:
          print("Are malli ochinav ha?")
          continue
     if age>=20:
          print("Are mi Amma Nanna ni avaru chuskutar ra?")
     elif age>19:
          print("Are nik 2 minutes lo padipothadhi ra lite thisko")
     else:
          print("Po chudu po inka ")
     again = input("Malli inko sari osthav ha? (yes/no): ")
     if again.lower()!="yes":
          print("Dengey Kotukuney Lanjakoduka")
          break

