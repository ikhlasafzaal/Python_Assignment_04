def main():
    # Yahan hum for loop ka istemal kar rahe hain jisme range function ka use kar rahe hain
    # Jis se hum 10 se le kar 1 tak countdown kar sakte hain.
    # range(10, 0, -1) ka matlab hai: shuru karo 10 se, ruk jao 0 pe (0 ko include nahi karenge),
    # aur -1 ka matlab hai, har iteration mein 1 kam karo (backward counting).
    for i in range(10, 0, -1):
        print(i, end=" ")  # Har number ke baad ek space daal rahe hain taa ke numbers achay se print hon.
    
    print("Liftoff!")  # Jab countdown complete ho jaye, to 'Liftoff!' print karo

# Ye line ensure karti hai ke jab script run ho to main function call ho.
if __name__ == '__main__':
    main()
