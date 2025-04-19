import random
def main():
 
 # Dice k random numbers generate karna
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)

  # Dice ka sum nikalana
  sum = dice1 + dice2

# Dice k individual result or sum ko print karna
  print(f"Dice 1 result is : {dice1}")
  print(f"Dice 2 result is : {dice2}")
  print(f"The Total sum is : {sum}")


if __name__ == '__main__':
   main()