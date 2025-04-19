def main():
    # Har planet ke liye gravity percentage ka data, jo Earth ke comparison mein hai
    gravity_percentages = {
        "Mercury": 37.6,    # Mercury par gravity Earth ke 37.6% hai
        "Venus": 88.9,      # Venus par gravity Earth ke 88.9% hai
        "Mars": 37.8,       # Mars par gravity Earth ke 37.8% hai
        "Jupiter": 236.0,   # Jupiter par gravity Earth ke 236.0% hai
        "Saturn": 108.1,    # Saturn par gravity Earth ke 108.1% hai
        "Uranus": 81.5,     # Uranus par gravity Earth ke 81.5% hai
        "Neptune": 114.0    # Neptune par gravity Earth ke 114.0% hai
    }
    
    # User se Earth pe unka weight lene ka prompt
    earth_weight = float(input("Enter a weight on Earth: "))  # Weight ko float mein convert karte hain
    
    # User se planet ka naam lene ka prompt
    planet = input("Enter a planet: ").capitalize()  # Planet ka naam capitalize karna zaroori hai, jise first letter capital ho
    
    # Agar user ne valid planet ka naam diya ho, to weight calculate karte hain
    if planet in gravity_percentages:
        # Planet ki gravity percentage se Earth weight ko multiply karte hain aur percentage ka adjustment karte hain
        planet_weight = earth_weight * gravity_percentages[planet] / 100
        
        # Result ko 2 decimal places tak round karte hain aur print karte hain
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")  # Rounded weight print karte hain
    else:
        # Agar planet ka naam galat diya ho, to user ko error message dena
        print("Invalid planet name. Please enter a valid planet.")  # Galat planet name ka error

# Jab ye script direct run hoti hai, to main() function call hota hai
if __name__ == "__main__":
    main()
