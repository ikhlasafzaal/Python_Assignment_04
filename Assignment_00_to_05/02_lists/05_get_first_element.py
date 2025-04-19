# Yeh function list ka pehla element print karta hai
def get_first_element(lst):
    print(lst[0])  # List ke pehle item ko print karna

# Yeh function user se input leta hai aur ek list banata hai
def get_lst():
    lst = []  # Ek khaali list banai
    # User se input lene ka process start karte hain
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Jab tak user kuch type kar raha ho, list mein daalte jao
        lst.append(elem)  # Jo bhi cheez user ne likhi, wo list mein add karna
        elem = input("Please enter an element of the list or press enter to stop: ")  # Agla input
    return lst  # Final list ko return karna

# Yeh main function hai jo sab kuch chalayega
def main():
    lst = get_lst()  # User se list lene ka function call
    get_first_element(lst)  # List ka pehla element print karna

# Agar hum program run kar rahe hain, toh main() function ko call karte hain
if __name__ == '__main__':
    main()  # Program start karna
