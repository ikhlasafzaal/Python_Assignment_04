def main():
    
    # User say side input lene ka prompt
    side1 : float = float(input("What is lenght of 1?"))
    side2 : float = float(input("What is lenght of 2?"))
    side3 : float = float(input("What is lenght of 3?"))

    # perimeter calculate kar rahay hain jo teeno side ka sum hoga
    lenght = side1 + side2 + side3

    # Triange ka perimeter print kar rahay hain
    print(f"The perimeter of the triangle is {lenght}")

# agar program ko directly run kiya jaye to function execute ho
if __name__ == '__main__':
    main()