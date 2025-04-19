def main():
    # User se year input lena
    year = int(input("Enter a year: "))
    
    # Leap year ke liye conditions check karna
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")  # Agar year leap year hai
    else:
        print("That's not a leap year.")  # Agar year leap year nahi hai

# Ye line zaroori hai taake main() function chal sake jab file run ki jaye
if __name__ == '__main__':
    main()
