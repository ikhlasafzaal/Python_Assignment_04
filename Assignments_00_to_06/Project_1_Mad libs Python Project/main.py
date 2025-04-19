# Step 1: User se inputs lena
print("Welcome to the Mad Libs Game!")  # Ye message user ko game mein welcome karne ke liye hai
name = input("Enter a name: ")  # Yahan user se ek naam poocha jaa raha hai
place = input("Enter a place: ")  # Yahan user se ek jagah ka naam poocha jaa raha hai
adjective1 = input("Enter an adjective: ")  # Yahan user se ek pehla adjective (kisi cheez ki quality) liya jaa raha hai
adjective2 = input("Enter another adjective: ")  # Dusra adjective liya jaa raha hai
animal = input("Enter an animal: ")  # Yahan user se ek animal ka naam liya jaa raha hai
verb1 = input("Enter a verb (past tense): ")  # Pehla verb (past tense mein) liya jaa raha hai
verb2 = input("Enter another verb (past tense): ")  # Dusra verb (past tense mein) liya jaa raha hai
color = input("Enter a color: ")  # Yahan color ka naam liya jaa raha hai
food = input("Enter a type of food: ")  # Yahan ek food item liya jaa raha hai
emotion = input("Enter an emotion: ")  # Yahan ek emotion (jaise khushi, gussa) liya jaa raha hai

# Step 2: Mad Libs ki kahani banana
# Yahan pe story ka template banaya jaa raha hai jisme user ke inputs ko f-strings ke zariye add kiya jaayega
story = f"""
Once upon a time, there was a person named {name} who lived in {place}. 
They were very {adjective1} and {adjective2}. One day, {name} went to the zoo 
and saw a {color} {animal} that {verb1} all the way across the zoo. 
Afterward, {name} decided to {verb2} and eat some {food}. 
They felt so {emotion} and couldn't stop laughing!
"""

# Step 3: Complete Mad Libs story print karna
# Yahan pe user ke input ke saath puri kahani ko print kiya jaa raha hai
print("\nHere's your Mad Libs story:")
print(story)
