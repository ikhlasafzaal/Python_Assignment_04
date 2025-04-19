def main():
    # Loop ka istemal karenge jo pehle 20 even numbers ko print karega
    for i in range(0, 40, 2):  # range(0, 40, 2) se hum 0 se lekar 39 tak ke even numbers ko generate karenge.
        print(i, end=" ")  # Har number ke baad space print karenge

# Ye line zaroori hai jisme hum main() function ko call karte hain.
if __name__ == '__main__':
    main()
