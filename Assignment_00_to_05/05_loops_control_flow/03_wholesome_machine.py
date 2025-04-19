def main():
    # Hum yeh affirmation define karte hain jo user ko type karna hoga
    affirmation = "I am capable of doing anything I put my mind to."
    
    # Infinite loop banate hain jo tab tak chalega jab tak user sahi affirmation type nahi karega
    while True:
        # User se input lene ka prompt dikhate hain
        user_input = input("Please type the following affirmation: " + affirmation + " ")
        
        # Agar user ka input sahi hai, to loop break karenge aur success message dikhayenge
        if user_input == affirmation:
            print("That's right! :)")
            break  # Correct input hone par loop ko break kar denge
        
        # Agar input galat hai, to message dikhayenge aur loop dobara chalega
        else:
            print("Hmmm That was not the affirmation.")
    
# Ye line zaroori hai jisme hum main() function ko call karte hain
if __name__ == '__main__':
    main()
