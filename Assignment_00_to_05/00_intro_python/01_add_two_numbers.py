def main():
    print("This Program add two number")

    # user to enter the first number.
    first_number = input("Enter your first number : ")

    # convert it to an integer.
    first_number = int(first_number)

    #  user to enter the second number.
    sec_number = input("Enter your second number : ")

    #  convert it to an integer.
    sec_number = int(sec_number)

    # Calculate the sum of the two numbers.
    total_sum = first_number + sec_number

    # Print the total sum with an appropriate message.
    print(f"The sum of {first_number} and {sec_number} = {total_sum}")

if __name__ == '__main__':
 main()