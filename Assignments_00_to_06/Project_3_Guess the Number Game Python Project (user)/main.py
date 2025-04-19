import random

def guess_the_number():
    # Welcome message
    print("Welcome to 'Guess the Number'!")
    print("You need to guess the number I am thinking of.")
    
    # Computer randomly selects a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of guesses
    guesses = 0
    
    # Main game loop
    while True:
        # Get the user's guess
        user_guess = int(input("\nEnter your guess (between 1 and 100): "))
        guesses += 1
        
        # Check if the guess is correct, too high, or too low
        if user_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        elif user_guess > number_to_guess:
            print("Your guess is too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guesses} tries.")
            break  # Exit the loop when the user guesses correctly

# Run the game
guess_the_number()
