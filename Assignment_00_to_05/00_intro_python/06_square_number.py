def main():

    # User say number input lena
    num = float(input("Type the number and see it sqaure: "))

    # Number ka square calculate krna ( number ko 2 k sath multiply karna)
    square = num ** 2

    # Number or Square ko print krna
    print(f" Number {num} Square is : {square}")


# agar program directly run ho raha hai to function execute ho
if __name__ == '__main__':
    main()