def main():

    # user say first or second integer divided or divide value len
    first_number = int(input("Enter in integer to be divided: "))
    sec_number = int(input("Enter in integer to be divide: "))

    # division ka result or remainder calculate krna
    quotient = first_number // sec_number # quotient Nikalna
    remainder = first_number % sec_number # remainder Nikalna

    # final result print kiya
    print(f"The result of this division is: {quotient} with a remainder of : {remainder}")

if __name__ == '__main__':
    main()