import random

# Constants
NUM_ROUNDS: int = 5  # Yeh variable define karta hai ke game mein kitne rounds khele jaayenge

# Function to play the game
def main():
    # Game ka shuruat ka message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    # Player ka score shuru mein 0 hoga
    score = 0

    # Yeh loop chal raha hai har round ke liye
    for round_number in range(1, NUM_ROUNDS + 1):
        # Player aur computer ke liye random numbers generate karna (1 se 100 ke beech)
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Player ka number show karwana
        print(f"Round {round_number}")
        print(f"Your number is {player_number}")
        
        # User se input lena ke kya unka number computer ke number se higher hai ya lower
        guess = input(f"Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Input validation loop
        while guess not in ['higher', 'lower']:  # Agar guess 'higher' ya 'lower' nahi hoga
            print("Please enter either 'higher' or 'lower'.")  # Yeh line user ko bataayegi ke galat input diya hai
            guess = input(f"Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Game logic: Agar guess sahi hai toh score +1 hoga
        # Agar player ka number higher hai aur unhone 'higher' bola, ya player ka number lower hai aur unhone 'lower' bola, toh player jeet gaya
        if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Score +1 hoga
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Round ke baad score show karna
        print(f"Your score is now {score}\n")

    # Jab game khatam ho jaye toh thanks ka message aur final score show karna
    print("Thanks for playing!")
    
    # Final score ke basis pe feedback dena
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")  # Agar player ne har round jeet liya ho
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")  # Agar player ne aadhe se zyada rounds jeet liye ho
    else:
        print("Better luck next time!")  # Agar player ne kam rounds jeetay, toh "Better luck next time!" ka feedback milta hai

# Yeh ensure karta hai ke jab yeh script directly chalayein, tab main function run ho
if __name__ == '__main__':
    main()
