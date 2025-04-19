def double_list():
    # original list
    numbers = [1, 2, 3, 4,5]

    # loop jo list k har element ko dekh k double kare ga
    for i in range(len(numbers)): # loop list ki lenght k according chalega.

        # numbers[i] se hum current element ko access kar rahe hain.
        numbers[i] = numbers[i] * 2 # or 2 say multiply kr eahay hain
     
     # final result print
    print(numbers)
# function ko call
double_list()

    