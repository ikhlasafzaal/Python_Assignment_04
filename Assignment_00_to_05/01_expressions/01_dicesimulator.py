# random number generate karne k liye
import random

# Dice ko 3 dafa roll karne ka function
def roll_dice():
    # 1,6 tak random number generate karne k liye
    return random.randint(1,6)

# 3 dafa loop chalega
for i in range(3):
    # first time  ka result
    die1 = roll_dice()
    # sec time ka result
    die2 = roll_dice()

    # final result
    print(f"Roll : {i+1} Dice 1 = {die1} , dice 2 = {die2}")

# agar program directly run hoga to function execute hoga
if __name__ == '__main__':
    roll_dice()