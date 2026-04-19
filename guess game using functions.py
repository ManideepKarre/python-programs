import random

def get_secret_number():
    return random.randint(1,100)

def check_guess(secret,guess):
    if guess > 100:
        return "exit"
    elif guess == secret:
        return "correct"
    elif guess < secret :
        return "low"
    else:
        return "high"

def play_game():
    secret = get_secret_number()

    for attempt in range(1,4):
        guess = int(input(f"attempt {attempt}- guess a number (1-100): "))
        result = check_guess(secret,guess)

        if result == "exit":
            print("invalid input. Exiting game...")
            break
        elif result =="correct":
            print(f"correct! you guessed it in {attempt} tries")
            break
        elif result == "low":
            print("too low")
        elif result =="high":
            print("Too High")
        
    else:
        print(f"you lost! the number was {secret}.. Try again you may win..")
    
play_game()