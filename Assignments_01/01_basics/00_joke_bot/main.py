# Constants for prompt, joke, and sorry message
PROMPT = "What do you want?"  # User se input lene ka prompt message
JOKE = """Here's a joke for you!
Sophia was heading to the grocery store. A programmer told her: "Get a liter of milk, and if they have eggs, get 12."
Sophia returned with 13 liters of milk. The programmer asked, "Why did you get 13, not 12?"
Sophia replied, "Because they had eggs!"  # Yeh joke user ko dikhayi jayegi agar wo "Joke" dalein"""

SORRY = "Sorry I only tell jokes"  # Agar user kuch aur input kare, toh sorry message dikhayi jayegi

def main():
    # User se input lene ke liye prompt
    user_input = input(PROMPT + " ")  # User se input lene ke liye message display karega
    
    # Agar user "Joke" input kare toh joke print hoga
    if user_input == "Joke":  # Agar user ne "Joke" dala ho
        print(JOKE)  # Joke print hoga
    else:
        print(SORRY)  # Agar user ne kuch aur dala ho, toh sorry message print hoga

# Yeh line ensure karti hai ke main() function tab chale jab script execute ho
if __name__ == '__main__':
    main()
