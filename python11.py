#Create a simple guess-the-number game: 
#1. Generate a random number between 1 and 50. 
#2. Allow the user to guess the number. 
#3. Provide feedback “guess is right or guess is wrong” until the user guesses correctly.
import random

def guess_the_number():
    # Step 1: Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 50.")
    
    while True:
        # Step 2: Allow the user to guess the number
        guess = int(input("Enter your guess: "))
        
        # Step 3: Provide feedback
        if guess < secret_number:
            print("Your guess is too low. Try again!")
        elif guess > secret_number:
            print("Your guess is too high. Try again!")
        else:
            print("Congratulations! Your guess is right!")
            break

# Start the game
guess_the_number()
