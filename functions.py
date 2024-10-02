def straw_hats(crew_member = "Luffy", origin = "East Blue", attributes = ["ambitious","haki"]):
    #code here gets executed when you call the function
    print(crew_member)
    if crew_member == "Luffy":
        print("The heir of Gold Roger")
    elif crew_member == "Zoro":
        print("The Greatest Swordsman in the world")
    elif crew_member == "Sanji":
        print("The Greatest Chef in the world")
    elif crew_member == "Robin":
        print("The Greatest Archeologist in the world")
    else:
        print("Member of the Straw Hat Crew")
    #\n is a type of escape character that will create a new line when used
    print(f"\n{crew_member} originates from {origin}")
    if "haki" in attributes:
        print("Wields the power of Haki")
    else:
        print("Wields the power of Devil Fruit")
    #any code below the return statement won't be executed
    return f"Whitebeard and {crew_member}"

straw_hats() #runs the function with default parameters
print("") #prints an empty line

#you can pass any data type into the function as an argument
y = straw_hats("Robin", "West Blue", ["dark-humor", "books", "beauty", "flowers"])
#The straw_hats function will run its block of code as usual, but only the value after the return keyword will get assigned to y.
print(f"{y} are headed towards Wano.")

#Print Function only prints out the block of code on the terminal
#In order to return the value from a function at a particular place and store it in a variable, we have to use the keyword 'return'
def addition(x):
    print("\nAdding 1 to x")
    return x + 1
a = addition(5)
print(a)

def grocery(items):
    return "fruits" in items
has_fruit = grocery(["veggies", "fruits", "beans"])
print(has_fruit)

def result(x):
    if x >= 40 and x <= 80:
        percent = (x/80)*100
        return (f"Pass. You have obtained {percent}% marks")
    elif x > 80:
        return "Your input is invalid"
    else:
        return "Fail"
p = result(70)
print(p)
