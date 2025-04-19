import random

NUM_ROUNDS = 5  # Kitne rounds hone hain

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    # Pehla random number generate karte hain jisse game start hoga
    current_number = random.randint(1, 100)
    
    # Game ka main loop jo NUM_ROUNDS tak chalega
    for round_num in range(1, NUM_ROUNDS + 1):  # **Loop** - 5 rounds chalenge
        print(f"Round {round_num}")  # Har round ka number print karna
        print(f"The current number is {current_number}.")  # Abhi jo number hai, wo print karna
        
        # User se poochna ke agla number higher ya lower hoga
        guess = input("Do you think the next number will be 'higher' or 'lower'? ").lower()  # **Input** - User se input lena
        
        # Agla random number generate karte hain
        next_number = random.randint(1, 100)
        
        # **Condition (if-else)** - Agar user ka guess sahi hai ya nahi
        if (guess == 'higher' and next_number > current_number) or (guess == 'lower' and next_number < current_number):
            print(f"Correct! The next number was {next_number}.")  # Agar guess sahi ho to yeh print hoga
        else:
            print(f"Wrong! The next number was {next_number}.")  # Agar guess galat ho to yeh print hoga
        
        # Agle round ke liye current number ko update karte hain
        current_number = next_number
        
        print('--------------------------------')  # Har round ke baad ek separator print karte hain
    
    print("Game over! Thanks for playing.")  # Game khatam hone par thanks ka message dena

if __name__ == "__main__":
    main()
