import random  # Random module ko import kar rahe hain

# User ka choice lene wali function
def get_user_choice():
    while True:
        # User se input lene ka prompt, aur input ko lowercase mein convert kar rahe hain
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        # Agar user ne valid option diya ho toh usse return karenge
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            # Agar user ne galat choice diya ho toh isko bataenge aur dobara input lene ko kahenge
            print("Invalid choice. Please try again.")

# Computer ka choice randomly generate karne wali function
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])  # Randomly computer ka choice select karna

# Winner decide karne wali function
def determine_winner(user_choice, computer_choice):
    # Agar user aur computer ka choice same ho, toh tie hai
    if user_choice == computer_choice:
        return "It's a tie!"
    # Agar user jeet gaya ho
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        # Agar computer jeet gaya ho
        return "Computer wins!"

# Main function jo game ko chalata hai
def play_game():
    print("Welcome to Rock, Paper, Scissors!")  # User ko welcome message dikhana
    
    # User ka choice lene ke liye function call karna
    user_choice = get_user_choice()
    
    # Computer ka choice randomly select karne ke liye function call karna
    computer_choice = get_computer_choice()
    
    # User aur computer ka choice print karna
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Winner ka result determine karna aur print karna
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Agar yeh script directly chalai ja rahi ho toh game start karna
if __name__ == "__main__":
    play_game()
