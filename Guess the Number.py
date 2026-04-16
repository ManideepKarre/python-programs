import random 

number = random.randint(1, 100)

for attempt in range(1,4):
    guess = int(input(f"Attempt {attempt}- Guess a number (1-100): "))

#exit condition
    if guess > 100:
        print("Invalid input! Exiting Game")
        break
    

#for i in range(4): #give user 3 chances 
  #  guess = int(input("Guess a number (1-100): "))

    if guess == number:
        print("Correct you guessed in {attempt} Tries Play Again")
        break
    elif guess< number:
        print("Too Low ")
        break
    else:
        print("too high")


else:
    print("You lost the chance the number is ", number)
      
