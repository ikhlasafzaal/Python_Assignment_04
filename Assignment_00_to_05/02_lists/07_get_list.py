def main():
    # Yeh ek khaali list hai jisme hum user ke inputs store karenge
    values = []

    # Yeh loop tab tak chalega jab tak user kuch na daale
    while True:
        # User se input lena (English mein)
        value = input("Enter a value,stop to press enter : ")

        # Agar user ne kuch nahi likha aur bas Enter press kiya, toh loop stop ho jayega
        if value == "":
            break
        
        # Agar user ne kuch likha, toh wo value list mein add karenge
        values.append(value)

    # Jab loop ruk jaye, hum final list ko print karenge
    print("Here's the list:", values)

# Program ko start karna
if __name__ == '__main__':
    main()
