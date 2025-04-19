import random  # Random number generate karne ke liye random module ko import kar rahe hain

def main():
    # Ek random number generate kar rahe hain jo 0 se 99 ke beech hoga
    number_to_guess = random.randint(0, 99)
    
    print("Main ek number soch raha hoon jo 0 se 99 ke beech hai... Isay guess karo!")
    
    # Guess karne ka loop start kar rahe hain
    while True:
        # User se guess lene ke liye input() ka use kar rahe hain, aur usay integer mein convert kar rahe hain
        user_guess = int(input("Enter a guess: "))
        
        # Agar user ka guess zyada hai, toh yeh message print hoga
        if user_guess > number_to_guess:
            print("Your guess is too high")
        # Agar user ka guess kam hai, toh yeh message print hoga
        elif user_guess < number_to_guess:
            print("Your guess is too low")
        # Agar guess sahi hai, toh congratulatory message show karenge aur loop ko break karenge
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break  # Jab sahi number guess kar lenge toh loop se bahar aa jayenge

# Yeh line ensure karti hai ke main function script ke run hone par chal jayega
if __name__ == '__main__':
    main()
