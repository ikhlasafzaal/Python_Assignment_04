def main():
    # Yahan hum for loop ka use kar rahe hain jo 10 se lekar 1 tak countdown karega.
    # range(10, 0, -1) ka matlab hai: 10 se shuru karo, 0 tak jao (0 ko include nahi karega), aur har iteration mein 1 ka step kam karo.
    for i in range(10, 0, -1):
        # Har number ko print kar rahe hain. end=" " ka matlab hai ke har number ke baad space print hoga,
        # taake numbers ek hi line mein print ho jayein.
        print(i, end=" ")  
    
    # Jab loop khatam ho jata hai, to "Liftoff!" print hota hai.
    # Yeh string space ke baghair next line mein print hoga, kyun ke print() ka default behavior hai new line print karna.
    print("Liftoff!")  

# Yeh line ensure karti hai ke jab script run ho, to main function execute ho.
# Agar yeh code directly run ho raha hai (matlab file directly execute ho rahi hai), tab main() function ko call kiya jata hai.
if __name__ == '__main__':
    main()
