def main():
    # Pehle user se ek number input karte hain, jo integer format mein hona chahiye.
    # "input" function se hum string lete hain, aur "int()" function se usay integer mein convert karte hain.
    curr_value = int(input("Enter a number: "))
    
    # Yahan pe hum "while" loop use kar rahe hain. Yeh loop tab tak chalega jab tak curr_value 100 se kam hoga.
    # Jab curr_value 100 ya usse zyada ho jayega, tab loop ruk jayega.
    while curr_value < 100:
        # Har iteration mein, hum curr_value ko double karenge.
        # Example ke liye, agar curr_value 2 tha, toh ab wo 4 ho jayega.
        curr_value = curr_value * 2  # Yahan pe curr_value ko 2 se multiply kar rahe hain.
        
        # Har baar loop ke andar, hum doubled value ko print karte hain.
        # "end=' '" ka matlab hai ke har number ke baad space daalna hai taake numbers ek hi line mein dikhayen.
        print(curr_value, end=" ")

# Ye line required hai Python script ko execute karne ke liye.
# Jab hum python file run karte hain, yeh line ensure karti hai ke main() function call ho.
if __name__ == '__main__':
    main()
