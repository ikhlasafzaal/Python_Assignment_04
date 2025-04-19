# import math humain math ke advanced functions aur constants ka access deta hai,
#  jo humare code ko zyada powerful aur efficient banata hai!
import math

def main():
   
   # user say AB oR AC ki lenght ka input lena
   ab = float(input("Enter the Lenght of AB: "))
   ac = float(input("Enter the Lenght of AC:  "))

   # Pytha theorem ka use kar kay BC (Hypotenuse) calculate karna
   bc = math.sqrt(ab **2 + ac **2)# BC ka square root lena
 
   # final result print krena
   print("The result of BC (The hypotenuse) is:",bc)

# Agar program directly run ho to function execute ho.
if __name__ == '__main__':
   main()