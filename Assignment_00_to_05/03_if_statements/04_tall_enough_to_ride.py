def main():
    # Minimum height requirement
    MIN_HEIGHT = 50
    
    # User se height puchhna
    height = float(input("How tall are you? "))
    
    # Check karna ki user ki height minimum requirement se zyada hai ya nahi
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# Ye line zaroori hai taake main() function chal sake jab file run ki jaye
if __name__ == '__main__':
    main()
