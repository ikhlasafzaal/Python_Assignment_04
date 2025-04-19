# Function to access an element at a given index
def access_element(lst, index):
    # Step 1: Check agar index list ke range ke andar hai ya nahi
    # Agar index valid nahi hai (negative ya list ke size se bara hai), to error message return karenge
    if index < 0 or index >= len(lst):
        return "Index out of range!"  # Agar index range ke bahar hai, to error return karenge
    else:
        return lst[index]  # Agar index valid hai, to uss index pe jo element hai woh return karenge

# Function to modify an element at a given index
def modify_element(lst, index, new_value):
    # Step 2: Check agar index valid hai ya nahi
    if index < 0 or index >= len(lst):
        return "Index out of range!"  # Agar index valid nahi hai, to error return karenge
    else:
        lst[index] = new_value  # Agar index valid hai, to list ke uss index ko new_value se replace karenge
        return lst  # List ko modify karne ke baad updated list return karenge

# Function to slice the list from start index to end index (not including end index)
def slice_list(lst, start, end):
    # Step 3: Check agar indices valid hai ya nahi
    # Start index agar negative ho ya end index list ke size ke bahar ho to slice invalid hoga
    if start < 0 or end > len(lst) or start > end:
        return "Invalid indices!"  # Agar indices invalid hain, to error message return karenge
    else:
        return lst[start:end]  # Agar indices valid hain, to list ka slice return karenge

# Main function jisme program ka logic run hota hai
def main():
    # Step 4: List ko initialize karte hain
    # Yeh ek sample list hai jo numbers, strings aur float values ko mix karti hai
    sample_list = ['apple', 3, 'banana', 12.5, 'grape']

    # Print kar rahe hain initial list ko
    print("Initial List:", sample_list)

    # Step 5: Infinite loop start karte hain taake user ko baar baar option dena hai
    while True:
        # User ko ek operation select karne ke liye keh rahe hain
        print("\nSelect an operation:")
        print("1. Access an element")  # Option 1: List mein se element ko access karna
        print("2. Modify an element")  # Option 2: List mein element ko modify karna
        print("3. Slice the list")  # Option 3: List ko slice karna
        print("4. Exit")  # Option 4: Program ko exit karna

        # Step 6: User se operation ka choice lena
        choice = input("Enter the operation number (1/2/3/4): ")

        # Agar user ne option 1 select kiya ho, to access_element function call karenge
        if choice == '1':
            # User se index input lena
            index = int(input("Enter the index to access: "))  # Index ko integer mein convert karenge
            print("Element at index", index, ":", access_element(sample_list, index))  # Function call kar ke result print karenge

        # Agar user ne option 2 select kiya ho, to modify_element function call karenge
        elif choice == '2':
            # User se index aur naya value input lena
            index = int(input("Enter the index to modify: "))  # Index input
            new_value = input("Enter the new value: ")  # Naya value input
            print("Updated List:", modify_element(sample_list, index, new_value))  # Modified list print karenge

        # Agar user ne option 3 select kiya ho, to slice_list function call karenge
        elif choice == '3':
            # User se start aur end index input lena
            start = int(input("Enter the start index: "))  # Start index input
            end = int(input("Enter the end index: "))  # End index input
            print("Sliced List:", slice_list(sample_list, start, end))  # Sliced list print karenge

        # Agar user ne option 4 select kiya ho, to program exit karenge
        elif choice == '4':
            print("Exiting the game.")  # Exit message print karenge
            break  # Program se bahar nikal jaenge

        # Agar user ne koi invalid choice diya ho, to error message show karenge
        else:
            print("Invalid choice. Please try again.")  # Invalid choice ko handle karte hain

# Program ka entry point
# Ye line program ko start karne ke liye use hoti hai
if __name__ == "__main__":
    main()  # Main function ko call karte hain taake game run ho sake
