import random 

options = ["rock", "paper", "scissors"]
winning_combos = {
    "rock" :"scissors",
    "scissors" : "paper",
    "paper" : "rock"
}

def play_game(max_chances):
    user_wins = 0
    computer_wins = 0
    ties = 0

    for chance in range (1, max_chances + 1):
        print(f"\nChance {chance}/{max_chances}")

        while True :
            user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
            if user_input == "q":
                return False #signal to stop playing
            if user_input in options :
                break
            print("Invalid input. Please type Rock, Paper or Scissors.")

        computer_pick = random.choice(options)
        print(f"Computer picked {computer_pick}.")

        if user_input == computer_pick:
            print("It's a tie!")
            ties += 1
        elif winning_combos[user_input] == computer_pick :
            print("You won!")
            user_wins += 1
        else:
            print ("You lost!")
            computer_wins += 1

        print(f"Score -> You : {user_wins} | Computer : {computer_wins} | Ties : {ties}")

    #After all chance are used
    print(f"\n{'='*40}")
    print(f"Game Over! All {max_chances} chances used.")
    print(f"Final Score -> You : {user_wins} | Computer : {computer_wins} | ties : {ties}")

    if user_wins > computer_wins:
        print("Overall winner : You!")
    elif computer_wins > user_wins:
        print("Overall Winner: Computer!")
    else:
        print("Overall Result: it's a tie!")
    print('='*40)

    return True #signal that game finished normally
    

while True:
    print("\n------ ROCK PAPER SCISSORS--------")

    while True :
        try:
            max_chances = int(input('How many chances do you want to play? (e.g. 10): '))   
            if max_chances > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid Input. Please enter a whole number.")

    keep_playing = play_game(max_chances) 

    if not keep_playing:
        print('Thanks for Playing. GoodBye!')
        break

    again = input("\n Play again?(Y/N): ").lower()
    if again !="y":
        print("Thanks for playing. GoodBye!")
        break
                