def main():
    # User se ek number lena
    curr_value = int(input("Enter a number: "))  # Input ko integer mein convert karna

    # Jab tak curr_value 100 se kam hai, loop chalana
    while curr_value < 100:
        curr_value *= 2  # curr_value ko double karna
        print(curr_value, end=" ")  # Doubled value ko print karna, space ke saath

# Is line ko ensure karne ke liye ke main function tab run ho jab script direct execute ho
if __name__ == '__main__':
    main()
