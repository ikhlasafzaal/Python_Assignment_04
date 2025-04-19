# variable inches ko feet k andar convert karne k liye constant value set kar rahay hain
inches_in_feet = 12

# main function jahan hum feet ko inches main convert karengy
def main():
    # User say feet ka size poch rahay hain or float main convert kar rahay hain
    feet = float(input("Enter your feet size"))

    # feet ko inches main convert kar rahay hain
    inches = feet * inches_in_feet

    # yahan final result print kar rahay hain
    print(f"That is , {inches} inches")


# agar program directly run hoga to function execute ho
if __name__ == '__main__':
    main()