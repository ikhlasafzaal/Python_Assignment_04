def get_user_numbers():
    """
    Ek khali list create karte hain.
    User se numbers input lete hain aur unko list mein store karte hain.
    Jab tak user blank line nahi deta, input lene ka process chalti rehti hai.
    Jab user blank input dega, tab loop band karte hain aur list ko return karte hain.
    """
    user_numbers = []  # Khali list banayi gayi hai
    while True:  # Yeh loop tab tak chalega jab tak user blank input nahi de deta
        user_input = input("Enter a number:(Enter to stop) ")  # User se number input liya jaata hai
        
        # Agar user blank input deta hai, toh loop break kar denge
        if user_input == "":
            break
        
        # User ke input ko integer mein convert karenge aur list mein add karenge
        num = int(user_input)
        user_numbers.append(num)  # List mein number add karte hain
    
    return user_numbers  # Final list ko return karte hain

def count_nums(num_lst):
    """
    Ek khali dictionary create karte hain.
    List ke har number ko loop karte hain.
    Agar number dictionary mein nahi hai, toh usko 1 se initialize karte hain.
    Agar number pehle se dictionary mein hai, toh uski value ko 1 se increment karte hain.
    """
    num_dict = {}  # Khali dictionary banayi gayi hai
    for num in num_lst:  # Har number ko list mein se process karte hain
        if num not in num_dict:  # Agar number dictionary mein nahi hai
            num_dict[num] = 1  # Number ko dictionary mein add karte hain
        else:
            num_dict[num] += 1  # Agar number already hai, toh uski value ko increment karte hain
    
    return num_dict  # Dictionary ko return karte hain

def print_counts(num_dict):
    """
    Dictionary ke har key-value pair ko print karte hain.
    Har number ke liye yeh batate hain ki wo number list mein kitni baar aaya hai.
    """
    for num in num_dict:  # Har key (number) ko dictionary mein se process karte hain
        print(str(num) + " appears " + str(num_dict[num]) + " times.")  # Number aur uski count print karte hain

def main():
    """
    User se numbers input karte hain aur unki count print karte hain.
    User jab tak numbers deta hai, tab tak input liya jata hai.
    Jab user blank input deta hai, toh list ke number ke counts print kar diye jaate hain.
    """
    user_numbers = get_user_numbers()  # User se numbers liye ja rahe hain
    num_dict = count_nums(user_numbers)  # Numbers ke counts ko store kar rahe hain
    print_counts(num_dict)  # Dictionary ke counts ko print karte hain

# Python boilerplate code. Agar yeh file direct run ki jaaye, toh main() function run hoga.
if __name__ == '__main__':
    main()
