# Voting age ke values define karte hain
PETURKSBOUIPO_AGE: int = 16  # Peturksbouipo ka voting age 16 hai
STANLAU_AGE: int = 25  # Stanlau ka voting age 25 hai
MAYENGUA_AGE: int = 48  # Mayengua ka voting age 48 hai

def main():
    # User se unki age puchhna
    age = int(input("How old are you? "))  # Age input lete hain aur integer mein convert karte hain

    # Peturksbouipo ke voting age ko check karna
    if age >= PETURKSBOUIPO_AGE:  # Agar age 16 ya zyada hai toh vote kar sakte hain
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:  # Agar age 16 se kam hai toh vote nahi kar sakte
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    
    # Stanlau ke voting age ko check karna
    if age >= STANLAU_AGE:  # Agar age 25 ya zyada hai toh vote kar sakte hain
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:  # Agar age 25 se kam hai toh vote nahi kar sakte
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    
    # Mayengua ke voting age ko check karna
    if age >= MAYENGUA_AGE:  # Agar age 48 ya zyada hai toh vote kar sakte hain
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:  # Agar age 48 se kam hai toh vote nahi kar sakte
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

# Ye line zaroori hai taake main() function chal sake jab file run ki jaye
if __name__ == '__main__':
    main()
