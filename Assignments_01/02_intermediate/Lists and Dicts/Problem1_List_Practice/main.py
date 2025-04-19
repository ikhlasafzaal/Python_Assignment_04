def main():
    # Step 1: Create a list called fruit_list with the given fruits
    # Humne fruit_list naam ki list banayi hai jisme 5 fruits hain
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Step 2: Print the length of the list
    # Yeh line list ki length (elements ka count) print karegi
    print("Length of the fruit list:", len(fruit_list))

    # Step 3: Add 'mango' at the end of the list
    # Ab hum 'mango' fruit ko list ke end mein add karenge
    fruit_list.append('mango')

    # Step 4: Print the updated list
    # Yeh line updated list ko print karegi jisme 'mango' add ho gaya hai
    print("Updated fruit list:", fruit_list)

# Call the main function to run the program
# Agar yeh script directly run ho, toh main function ko call karenge
if __name__ == "__main__":
    main()
