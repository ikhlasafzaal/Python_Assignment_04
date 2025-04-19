# random module ko import kar rahe hain taake hum random numbers generate kar saken
import random

# Constants define kar rahe hain - 
# N_NUMBERS ka matlab hai kitne random numbers print karne hain (10 numbers)
# MIN_VALUE aur MAX_VALUE define kar rahe hain jo range hai (1 se 100 tak)
N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    # Loop chalega 10 baar (jitne numbers hum print karna chahte hain)
    for _ in range(N_NUMBERS):
        # Har iteration mein ek random number generate karenge jo 1 se 100 ke beech ho
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        # Generated random number ko print karenge ek hi line mein space ke saath
        print(random_number, end=" ")

# Is line ka use kar rahe hain taake main() function tab chale jab yeh file run ho
if __name__ == '__main__':
    main()
