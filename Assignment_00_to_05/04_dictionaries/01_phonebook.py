def main():
    # Phonebook ka dictionary banaya jata hai jisme names aur numbers store honge.
    phonebook = {}

    while True:
        # User se name input lene ke liye prompt diya jata hai.
        name = input("Name: ")

        # Agar user ne blank input diya (yaani koi name nahi diya), toh loop break ho jayega.
        if name == "":
            break
        
        # Agar user ne koi name diya, toh uske liye number input karne ko kaha jata hai.
        number = input("Number: ")

        # Phonebook dictionary mein name ko key aur number ko value ke roop mein store kiya jata hai.
        phonebook[name] = number

    # Ab phonebook ke andar saare names aur numbers ko print kiya jata hai.
    for name, number in phonebook.items():
        # F-string ka use karke name aur number ko format karke print kiya jata hai.
        print(f"{name} -> {number}")

# Agar yeh file direct run ki jaye, toh main() function ko call karenge.
if __name__ == '__main__':
    main()
