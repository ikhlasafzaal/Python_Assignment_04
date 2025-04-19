def main():

    # User se  fahrenheit temperature input lein
    # Input ko float type maon convert karein taake decimal value bhi handle ho sakein
    degrees_fahrenheit = float(input("Enter your temperature"))

    # Fahrenheit se celsius main convert karne ka formula
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    # Full precision k sath result print karein
    print(f"Temperature : {degrees_fahrenheit}F = {degrees_celsius}C")

    # yeh line ensure karti hai k main function sirf tab run ho jab program directly chalein, import na ho.
if __name__ == '__main__':
   main()