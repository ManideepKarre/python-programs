def greet():
    print("Hello Bro")

def greet(mani):
    print(f"hello {mani}")

def add(a,b):
    return a + b

result = add(5,3)
print(result)

def check_age(age):
    if age >= 18:
        print("you are major")
    else:
        print("you are minor")

age = int(input("enter your age:"))
check_age(age)
