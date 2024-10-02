# while loop: executes a block of code as long as a condition is true
number = 1
while number <= 8:
    print(number)
    number *= 2

# for loop: used to iterate over a sequence
name = "Einstein"
i = 1
for letters in name:
    print(letters)

players = ["Kroos", "Modric", "Zidane"]
for player in players:
    print(player + " Hala Madrid!")

# Nested For Loop: allows to create every single combination from the provided sequences
males = ("Luffy", "Zoro", "Sanji")
females = ("Nami", "Robin", "Hancock")
villians = ("Donflamingo", "Crocodile", "Blackbeard")
for male in males:
    for female in females:
        for villian in villians:
            print(f"{male} will rescue {female} from {villian}")

# Control Flow Statements are used to control the flow of a loop
# 1) Break Statement: breaks the flow of the loop before it has looped through all the items
# For Loop
menu = ["pizza", "burger", "lasagna", "pasta", "sandwich"]
for food_item in menu:
    print(food_item)
    if food_item == "pasta":
        break
# While Loop
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

even = 2
while even <= 20:
    print(f"{even} is an even number")
    if even == 14:
        break
    even += 2

# 2) Continue Statement: skips a particular iteration in the sequence and continues with the next in order
vices = ["lust", "gluttony", "envy", "greed", "pride", "sloth", "wrath"]
for vice in vices:
    if vice == "greed":
        continue
    print(vice)

