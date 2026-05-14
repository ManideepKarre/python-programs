import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower() #break the while loop. not manual quit
    if user_input == "q":
        break 
    
    if user_input not in options: 
        print('Invalid input. Please type Rock, Paper or Scissors.')            #not is used for reversing 
        continue 
    random_number = random.choice(options)  #cleaner than randint
    #rock : 0, paper : 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    winning_combos ={
        "rock":"scissors",
        "scissors" : "paper",
        "paper" : "rock"
    }

    if user_input == computer_pick :
        print("Its a tie!")
        ties += 1
        
    elif winning_combos[user_input]== computer_pick:
        print("You Won!")
        user_wins += 1
        
    else:
        print("You Lost!")
        computer_wins +=1

print(f"\nYou won: {user_wins}, times | Computer won : {computer_pick} times | ties : {ties}")


print("GoodBye!")    



