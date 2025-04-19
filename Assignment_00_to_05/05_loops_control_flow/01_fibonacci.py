# Constant banate hain jo maximum value ko define karega
MAX_VALUE = 10000

def main():
    # Fibonacci sequence ke shuru ke do numbers
    a, b = 0, 1  # Fib(0) = 0 aur Fib(1) = 1
    
    # Pehla number print karte hain jo Fib(0) = 0 hai
    print(a, end=" ")
    
    # Loop mein jaakar har number print karenge jab tak b (Fibonacci number) MAX_VALUE se chhota ho
    while b < MAX_VALUE:
        print(b, end=" ")  # Har number ko ek space ke saath print karenge
        a, b = b, a + b  # Update karte hain a aur b ko (Fibonacci rule ke mutabiq)
    
    # Program ke end mein ek newline print karte hain taake output clean ho
    print()  

# Ye Python boilerplate hai jo program ko run karne ke liye zaroori hai.
if __name__ == '__main__':
    main()
