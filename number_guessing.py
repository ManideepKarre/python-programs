import random              #importing a module




range_of_top = input("Type a number: ")    

if range_of_top.isdigit():                               #we are using isdigit because the input is stored in string and we need to convert it into number
    range_of_top = int(range_of_top)

    if range_of_top <=0:
        print("Please type a number lager than 0 next time!")
        quit()
else:
    print('Please enter a number larger than 0 next time.')
    quit()

r = random.randrange(0,100)  #giving the range 

#or random.randint(5,101) #we include the stop number 

guesss = 0
while True:
    guesss += 1               #to make the guess that it was guessed in this many attempts
    user_g = input("Make a guess: ")
    if user_g.isdigit():
        user_g = int(user_g)
    else:
        print('Please Enter a number next time.')
        continue

    if user_g == r :                             #first we check this if it fails
        print("you nailed it!")
        break
    
    elif user_g > r :                             #we will check with elif if it fails
        print("You are above the number")
    else:                                       #then this should work.
        print("You are below the number")

print(f"you guessed in {guesss} attempts.")
