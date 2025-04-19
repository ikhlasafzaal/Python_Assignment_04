def main():
    # Fruits aur unke prices ko store karne ke liye dictionary banayi jati hai.
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    # Total cost ko 0 se initialize kiya gaya hai, jisme hum fruits ka price add karenge.
    total_cost = 0

    # Har fruit ke liye loop chalaya jaata hai.
    for fruit_name in fruits:
        # Har fruit ka price dictionary se nikala jaata hai.
        price = fruits[fruit_name]
        
        # User se poocha jaata hai ke wo kitne quantity mein fruit khareedna chahte hain.
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        
        # Fruit ki total cost calculate ki jaati hai aur total_cost mein add ki jaati hai.
        total_cost += (price * amount_bought)
    
    # Final total cost ko print kiya jaata hai.
    print("Your total is $" + str(total_cost))


# Is function ko call karne ke liye agar yeh script directly run ho to main() function execute hoga.
if __name__ == '__main__':
    main()
