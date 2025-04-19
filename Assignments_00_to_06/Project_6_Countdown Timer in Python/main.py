import time  # Time module ko import karte hain, jo time-related functions ke liye use hota hai

# Function banate hain jo countdown timer ko handle karega
def countdown_timer(seconds):
    # Jab tak seconds zyada hain, tab tak yeh loop chalega
    while seconds > 0:
        # divmod function use kar ke seconds ko minutes aur remaining seconds me convert karte hain
        mins, secs = divmod(seconds, 60)  # seconds ko minutes aur seconds me divide karte hain
        # f-string ka use kar ke MM:SS format me time print karte hain
        # '\r' use karke previous print ko overwrite karte hain, jisse har second naya time dikhai de
        print(f"\rTime Left: {mins:02}:{secs:02}", end="", flush=True)  # Time Left ka format display karte hain
        
        # time.sleep(1) se program ko 1 second ke liye pause karte hain, takay timer 1 second ka gap rakhe
        time.sleep(1)
        
        # Har bar seconds ko 1 se decrease karte hain
        seconds -= 1

    # Jab countdown complete ho jata hai (seconds = 0), yeh message print hota hai
    print("\nTime's up! ⏰")  # Time ke khatam hone ka message dikhate hain

# User se countdown time input lene ke liye
try:
    # User se input lete hain, aur usay integer me convert karte hain
    seconds = int(input("Enter countdown time in seconds: "))
    
    # Agar user ne positive number diya ho toh countdown timer ko call karte hain
    if seconds > 0:
        countdown_timer(seconds)  # Timer ko start karte hain
    else:
        print("Please enter a positive number.")  # Agar user ne 0 ya negative number diya ho toh warning
except ValueError:
    # Agar user ne invalid input diya ho, toh error handle karte hain
    print("Invalid input! Please enter a valid number.")  # Agar input galat ho toh message display karte hain
