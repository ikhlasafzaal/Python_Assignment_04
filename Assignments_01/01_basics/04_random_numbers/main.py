import random  # Random numbers generate karne ke liye random module ko import kar rahe hain

# Constants define kar rahe hain jo numbers ki quantity aur unka range set karenge
N_NUMBERS: int = 10  # 10 random numbers generate karne hain
MIN_VALUE: int = 1  # Minimum value jo 1 hai
MAX_VALUE: int = 100  # Maximum value jo 100 hai

def main():
    # For loop ke zariye 10 random numbers generate karenge
    for _ in range(N_NUMBERS):  # _ ka matlab hai variable ki value ko use nahi karenge
        # random.randint(min, max) function se 1 se 100 ke beech random number generate hoga
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # end=" " ka matlab hai numbers ke beech space laga kar print hoga

# Python boilerplate to ensure main function run ho jab script execute ho
if __name__ == '__main__':
    main()
