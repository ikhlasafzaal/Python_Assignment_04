# High-Low Game

Welcome to the **High-Low Game**! This game challenges you to guess if your randomly generated number is higher or lower than the computer's number. The game is played over multiple rounds, and your score is updated based on how well you guess.

## Game Rules

1. In each round, both the player (you) and the computer are assigned a random number between 1 and 100 (inclusive).
2. You will then make a guess: you will predict if your number is higher or lower than the computer's number.
3. If your guess is correct, you gain a point.
4. The game ends after a set number of rounds (default: 5 rounds), and your final score is displayed.

## How to Play

1. The game will print out your number for each round.
2. You will be asked whether you think your number is **higher** or **lower** than the computer's number.
3. After each round, the computer's number is revealed, and your score is updated.
4. If you answer correctly, you gain a point.
5. At the end of the game, your performance is evaluated based on the number of correct guesses.

### Example Gameplay


## Project Structure

This project includes the following key features:

1. **Random Number Generation:** Both the player's and the computer's numbers are randomly generated each round.
2. **User Input:** The game asks the user to guess if their number is higher or lower than the computer's.
3. **Scorekeeping:** The game keeps track of the player's score and updates it after each round.
4. **Input Validation:** Ensures the player inputs only valid responses (either 'higher' or 'lower').
5. **Performance Feedback:** After all rounds are played, the player is given feedback based on their score.




## Code Overview

### Simple Solution

```python
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: Keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # Milestone 1: Generate the random numbers and print them out
        computer_num: int = random.randint(1, 100)
        your_num: int = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user input for their choice
        choice: str = input("Do you think your number is higher or lower than the computer's?: ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct: bool = choice == "higher" and your_num > computer_num
        lower_and_correct: bool = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # Milestone 5: Keep track of your score
            your_score += 1
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: Keep track of your score
        print("Your score is now", your_score)
        print()

    print("Thanks for playing!")


### Solution with Extensions (Input Validation & Performance Feedback)
python
Copy
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: Keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # Milestone 1: Generate the random numbers and print them out
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Extension 1: Ensure the player inputs a valid choice (higher or lower)
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either 'higher' or 'lower': ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # Milestone 5: Keep track of your score
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: Keep track of your score
        print("Your score is now", your_score)
        print()
    
    # Extension 2: Conditional ending messages based on performance
    print("Your final score is", your_score)

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
