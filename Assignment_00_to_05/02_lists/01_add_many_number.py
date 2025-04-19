def sum_numbers(numbers):

    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    
    total = 0  # Total ko 0 se initialize karte hain
    for number in numbers:  # Har number ko list se check karte hain
        total += number  # Number ko total mein add karte hain
    return total  # Total return karte hain

list_sum_number = [20, 30, 40]  # List of numbers
result = sum_numbers(list_sum_number)  # Function ko call kar rahe hain

print(result)  # Result print kar rahe hain
