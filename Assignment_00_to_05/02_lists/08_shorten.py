# Yeh variable list ke maximum size ko define karta hai
MAX_SIZE = 3

# Yeh function list ko shorten karega
def shorten(lst):
    # Jab tak list ki length MAX_SIZE se lambi ho, items remove karte jayenge
    while len(lst) > MAX_SIZE:
        # List ke last item ko remove karna
        removed_item = lst.pop()
        # Jo item remove ho gaya, usse print karna
        print("Removed",removed_item)

# Yeh function user se list lene ke liye hai
def get_lst():
    """
    User se ek ek karke elements lene ke baad list return karta hai.
    """
    lst = []  # Khali list banayi
    # User se input lene ki shuruat
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Jab tak user kuch daal raha ho
        lst.append(elem)  # Entered element ko list mein daalna
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst  # Final list ko return karna

def main():
    # User se list lena
    lst = get_lst()
    # List ko shorten karna
    shorten(lst)
    # Final list ko print karna
    print("Final list:", lst)

# Yeh line ensure karti hai ke jab program run ho, toh main() function chale
if __name__ == '__main__':
    main()  # Program ko start karna
