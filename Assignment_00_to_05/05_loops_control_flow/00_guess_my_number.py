import random

def main():
    # Random number ko 0 se 99 ke beech select kiya jata hai
    secret_number = random.randint(0, 99)
    
    while True:
        # User se guess lene ke liye prompt diya jata hai
        guess = int(input("Enter a guess: "))
        
        # Agar user ka guess secret_number se zyada hai
        if guess > secret_number:
            print("Your guess is too high")
        
        # Agar user ka guess secret_number se kam hai
        elif guess < secret_number:
            print("Your guess is too low")
        
        # Agar user ka guess secret_number ke barabar hai
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Game ko exit karte hain jab guess sahi ho jata hai

# Python boilerplate.
if __name__ == '__main__':
    main()
