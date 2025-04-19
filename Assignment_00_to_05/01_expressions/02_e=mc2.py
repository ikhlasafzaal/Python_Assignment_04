# speed of light ki value set kar rahay hain.
# speed of light in meter per sec
c = 299792458

# main function jahan hum mass ki energy nikalengy
def main():

    # User say maas in kg input lay rahay hai
    # mass ko float main convert karna
    mass = float(input("Enter kg of mass"))

    # energy ka formula apply kr rahay hain
    energe = mass * c**2 # mass ko speed of light say multiply kar rahay hain

# final energy ko print kar rahay hain
    print(f"energe = mass * C^2...\nmass = {mass} kg\nC = {c} m/s\n joules of energy!")

# agar yeh file directly run ho rahi ho to main function ko call karengy
if __name__ == '__main__':
    main()