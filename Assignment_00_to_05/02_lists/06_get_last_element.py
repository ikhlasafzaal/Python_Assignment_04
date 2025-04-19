# Yeh function list ka last element print karega
def get_last_element(lst):
    """
    Provided list ka last element print karega.
    """
    # Pehli tareeqa: List ka length lene ke baad last element print karna
    print(lst[len(lst) - 1])

    # Doosra tareeqa: Negative index ka use kar ke last element print karna
    # print(lst[-1])  # Yeh bhi kaam karega aur zyada asaan hai

# Yeh function user se input le kar ek list banata hai
def get_lst():
    """
    User se ek ek karke elements lene ke baad list return karta hai.
    """
    lst = []  # Khali list banayi
    # Pehla input lena (English mein)
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Jab tak user kuch daalta rahe
        lst.append(elem)  # Jo input diya, usko list mein daal dena
        # Agla input lena
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst  # Final list ko return karna

# Yeh main function hai jisme hum sab kuch run karenge
def main():
    # User se list lena
    lst = get_lst()
    
    # List ka last element print karwana
    get_last_element(lst)

# Yeh line ensure karti hai ke jab program run ho, toh main() function chale
if __name__ == '__main__':
    main()  # Program ko start karna
