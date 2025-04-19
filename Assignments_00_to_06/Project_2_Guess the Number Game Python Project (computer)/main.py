import random  # Random module import kar rahe hain taake hum random number generate kar sakein

# Step 1: Game ka main function define karte hain
def guess_the_number():
    print("Welcome to the Guess the Number Game!")  # User ko game mein welcome karne ka message
    
    # Step 2: Computer ek random number select karega jo 1 aur 100 ke beech hoga
    number_to_guess = random.randint(1, 100)  # random number generate kar rahe hain
    
    # Step 3: Attempts count karne ke liye ek variable initialize kar rahe hain
    attempts = 0  # Attempts start kar rahe hain 0 se
    
    # Step 4: While loop ke through game continue rakhenge jab tak user correct guess nahi karta
    while True:
        try:
            # Step 5: User se input le rahe hain, jisme wo guess kar sakta hai
            guess = int(input("Guess a number between 1 and 100: "))  # Guess ko integer mein convert kar rahe hain
            
            # Step 6: Har guess ke saath attempts ko 1 badha rahe hain
            attempts += 1  # Ek attempt aur add kar rahe hain
            
            # Step 7: Check karte hain agar guess sahi hai, zyada hai, ya kam hai
            if guess < number_to_guess:
                print("Too low! Try again.")  # Agar guess kam hai
            elif guess > number_to_guess:
                print("Too high! Try again.")  # Agar guess zyada hai
            else:
                # Agar guess bilkul sahi hai, to game win ho gayi hai
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.") 
                break  # Jab sahi guess mil jaaye, to loop ko break kar dete hain
                
        except ValueError:
            # Step 8: Agar user ne koi galat input diya ho, jaise non-integer value, to error handle kar rahe hain
            print("Please enter a valid number.")  # User ko bata rahe hain ke valid number enter karein

# Step 9: Game ko start kar rahe hain
guess_the_number()  # Function ko call kar ke game shuru kar rahe hain
