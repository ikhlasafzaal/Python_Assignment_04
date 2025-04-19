import random  # Random module ko import kar rahe hain taake hum randomly word choose kar sakein
import string  # String module ko import kar rahe hain taake hum letters ke saath kaam kar sakein

# Dictionary of words categorized by topics (Jaise animals, countries, fruits)
word_dict = {
    'animals': ['dog', 'cat', 'elephant', 'tiger', 'lion'],
    'countries': ['india', 'france', 'germany', 'spain', 'japan'],
    'fruits': ['apple', 'banana', 'orange', 'grape', 'mango']
}

# Function jo ek random word choose karti hai dictionary se
def get_random_word():
    # Pehle ek random category choose karte hain (jaise animals, countries ya fruits)
    category = random.choice(list(word_dict.keys()))  
    # Us category se ek random word choose karte hain
    word = random.choice(word_dict[category])  
    return word  # Return karte hain selected word ko

# Function jo word ko display karte hai aur hidden letters ko show karti hai
def display_word(word, guessed_letters):
    display = ''  # Ek empty string initialize karte hain jisme word ka updated version store hoga
    for letter in word:
        # Agar letter user ne guess kar liya ho toh us letter ko display karenge
        if letter in guessed_letters:
            display += letter + ' '  # Letter ke baad space denge
        else:
            # Agar letter guess nahi kiya gaya ho toh underscore show karenge
            display += '_ '  # Underscore ko space ke saath show karenge
    return display.strip()  # Jo final word ka state hai usse return karenge

# Main Hangman Game function
def hangman_game():
    print("Welcome to Hangman!")  # Game ka welcome message
    
    # Ek random word choose kar rahe hain dictionary se
    word = get_random_word()  
    
    # Game ke liye initial variables setup kar rahe hain
    guessed_letters = []  # List jisme user ke guessed letters honge
    wrong_guesses = 0  # Wrong guesses ka count
    max_attempts = 6  # Maximum allowed wrong guesses (Hangman ka standard)
    
    print("Try to guess the word!")  # User ko batane ka message
    
    # Jab tak wrong guesses ki limit cross nahi hoti, game continue karega
    while wrong_guesses < max_attempts:
        # Abhi tak jo word ka state hai, wo display karenge
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {max_attempts - wrong_guesses}")  # Batayein kitne wrong guesses abhi allowed hain
        
        # User se ek letter guess karne ko keh rahe hain
        guess = input("Enter a letter: ").lower()  # Input ko lower case mein convert kar rahe hain
        
        # Input ko validate karte hain, check karte hain ke user ne sirf ek valid letter diya ho
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single valid letter.")  # Agar input valid nahi hai
            continue  # User ko dobara guess karne ka mauka dete hain
        
        # Agar user ne pehle hi yeh letter guess kiya ho, toh warn karte hain
        if guess in guessed_letters:
            print("You've already guessed that letter.")  
            continue  # Dobara guess karne ko kehte hain
        
        # Agar letter pehle nahi guess kiya gaya, toh usse guessed_letters mein add karte hain
        guessed_letters.append(guess)
        
        # Agar guess sahi ho, toh user ko batate hain ke uska guess correct tha
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            # Agar guess galat ho, toh wrong guesses ka count badhate hain
            print(f"Oops! '{guess}' is not in the word.")
            wrong_guesses += 1
        
        # Agar user ne saare letters sahi guess kar diye hain, toh game win ho jayega
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break  # Game ko end karte hain
        
    else:
        # Agar user ne wrong guesses ki limit cross kar li ho, toh game over ho jayega
        print(f"\nGame over! The word was: {word}")

# Game ko start karne ke liye main block
if __name__ == "__main__":
    hangman_game()
