# Constants for gravity of planets compared to Earth
# Har planet ki gravity ko Earth ke hisaab se define kiya gaya hai
MERCURY_GRAVITY = 0.376  # Mercury ki gravity Earth ki 37.6% hai
VENUS_GRAVITY = 0.889    # Venus ki gravity Earth ki 88.9% hai
MARS_GRAVITY = 0.378     # Mars ki gravity Earth ki 37.8% hai
JUPITER_GRAVITY = 2.36   # Jupiter ki gravity Earth ki 236% hai
SATURN_GRAVITY = 1.081   # Saturn ki gravity Earth ki 108.1% hai
URANUS_GRAVITY = 0.815   # Uranus ki gravity Earth ki 81.5% hai
NEPTUNE_GRAVITY = 1.14   # Neptune ki gravity Earth ki 114% hai
EARTH_GRAVITY = 1.0      # Earth ki gravity ko 1 define kiya gaya hai

# Mars Weight Calculation Function
def mars_weight():
    # Step 1: User se Earth ka weight input lene ka process
    # Input ko float mein convert karte hain, taki calculation kar sakein
    earth_weight = float(input("Enter a weight on Earth: "))  

    # Step 2: Mars ka equivalent weight calculate karna
    # Mars ki gravity constant ko 0.378 set kiya gaya hai
    MARS_MULTIPLE = 0.378  # Mars ki gravity Earth ki 37.8% hai
    mars_weight = earth_weight * MARS_MULTIPLE  # Earth weight ko Mars gravity ke saath multiply karte hain

    # Step 3: Result ko 2 decimal places tak round karte hain, taki output clean ho
    rounded_mars_weight = round(mars_weight, 2)

    # Step 4: Mars ka equivalent weight print karte hain
    print(f"The equivalent weight on Mars: {rounded_mars_weight}")


# Planetary Weight Calculation Function
def planetary_weight():
    # Step 1: User se Earth ka weight input lena
    earth_weight = float(input("Enter a weight on Earth: "))  # Earth ka weight input mein lena

    # Step 2: User se planet ka naam lena
    # `.capitalize()` use karke ensure karte hain ke planet ka naam capital letter se start ho
    planet = input("Enter a planet: ").capitalize()  

    # Step 3: Selected planet ke liye gravity constant ka determine karna
    if planet == "Mercury":  # Agar planet Mercury hai toh gravity constant select karo
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":  # Agar planet Venus hai toh gravity constant select karo
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":   # Agar planet Mars hai toh gravity constant select karo
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":  # Agar planet Jupiter hai toh gravity constant select karo
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":  # Agar planet Saturn hai toh gravity constant select karo
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":  # Agar planet Uranus hai toh gravity constant select karo
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":  # Agar planet Neptune hai toh gravity constant select karo
        gravity_constant = NEPTUNE_GRAVITY
    else:
        # Agar user ne incorrect planet name diya hai toh error message dena
        print("Invalid planet name.")
        return  # Agar planet naam invalid ho toh function ko exit karte hain

    # Step 4: Planet ke weight ka calculation
    planetary_weight = earth_weight * gravity_constant  # Earth weight ko planet ki gravity constant ke saath multiply karte hain

    # Step 5: Result ko 2 decimal places tak round karte hain
    rounded_planetary_weight = round(planetary_weight, 2)

    # Step 6: Planet ka equivalent weight print karte hain
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")


# Main function jisme program ka starting point hota hai
def main():
    # User ko choose karne ke liye options dete hain
    print("Choose a program to run:")  # User se program choose karne ke liye poochte hain
    print("1. Mars Weight")  # Option 1: Mars weight calculate karne ke liye
    print("2. Planetary Weight")  # Option 2: Kisi bhi planet ka weight calculate karne ke liye

    # User se choice input lene ka process
    choice = input("Enter 1 or 2: ")

    # Agar user ne 1 choose kiya ho toh Mars weight function call karte hain
    if choice == "1":
        mars_weight()  # Mars ka weight calculate karne ke liye
    # Agar user ne 2 choose kiya ho toh Planetary weight function call karte hain
    elif choice == "2":
        planetary_weight()  # Kisi bhi planet ka weight calculate karne ke liye
    else:
        # Agar user ne koi invalid input diya ho toh error message show karte hain
        print("Invalid choice. Please enter 1 or 2.")


# Ye line program ko run karne ke liye entry point ka kaam karti hai
if __name__ == "__main__":
    main()
