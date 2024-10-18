class Coast:
    location = "Cape Cod"
    water_color = "turqoise"

#after creating the class (new object), we create instances of that object to access its data and functions.
cape_cod_coast = Coast()
coast_2 = Coast()
#we can access the object attributes by using a period.
print(cape_cod_coast.location, coast_2.location)
print(cape_cod_coast.water_color)
#we can change the attributes of a class
cape_cod_coast.location = "Cancun"
#changing cape cod location won't affect beach_2 as beach_2 is an object with its own attributes.
print(cape_cod_coast.location, coast_2.location)

#Initialization Function
class Beach():
    open_for_public = True #class variable: all object instances have it in common
    def __init__(self, location, water_color, temperature): #self represents the instance of a class and binds the attributes with the\
        #given arguments
        self.location = location #instance variable: specific to each instance of the object
        self.water_color = water_color
        self.temperature = temperature
        self.heat_rating = "hot" if temperature > 80 else "cool"

#these various objects have their own properties but they're tied together by the same class.
naples_beach = Beach("Naples", "dark blue", 90) #self doesn't take any arguments
california_beach = Beach("California", "crystal blue", 70)

print(naples_beach.location, california_beach.location)
print(naples_beach.water_color, california_beach.water_color)
print(naples_beach.heat_rating, california_beach.heat_rating)
print(naples_beach.open_for_public, california_beach.open_for_public)

#Adding a Method in a Class
class Beach():
    open_for_public = True 
    def __init__(self, location, water_color, temperature):
        self.location = location
        self.water_color = water_color
        self.temperature = temperature
        self.heat_rating = "hot" if temperature > 80 else "cool"
        self.parts = ["water", "sand"] #instance variable

    #Instance Method: If we use instance variables inside a method, such methods are called instance methods. It must have\
    #  a self parameter to refer to the current object.
    def add_part(self, part):
        self.parts.append(part)
    
    def uppercase(self):
        return self.heat_rating.upper()


naples_beach = Beach("Naples", "dark blue", 90) 
california_beach = Beach("California", "crystal blue", 70)

print(naples_beach.parts, california_beach.parts)
print(naples_beach.heat_rating, california_beach.heat_rating)
#calling a method works the same way as calling an attribute i.e. by using a period
california_beach.add_part("rock")
print(naples_beach.parts, california_beach.parts)
print(naples_beach.uppercase()) #to get the return value of a method, call it with parenthesis

#Write a function that goes through all of the beaches and returns the ones that are hot and not rocky.
def exercise():
    sicily_beach = Beach("Italy", "Green", 90)
    sicily_beach.add_part("rock")
    miami_beach = Beach("USA", "Orange", 90)
    london_beach = Beach("England", "Grey", 60)
    istanbul_beach = Beach("Turkey", "Maroon", 85)
    amsterdam_beach = Beach("Netherlands", "Blue", 65)
    amsterdam_beach.add_part("rock")
    hot_not_rocky = []
    for beach in [sicily_beach, miami_beach, london_beach, istanbul_beach, amsterdam_beach]:
        if beach.heat_rating == "hot" and "rock" not in beach.parts:
            hot_not_rocky.append(beach)
    return hot_not_rocky

if __name__ == "__main__":
    beaches = exercise() #exercise() returns the list: [miami_beach, istanbul_beach] and assigns it to beaches.
    #we can't simply print(beaches) as when we try to print an object directly in Python, it shows its memory location by default. To get a \
    #human-readable description of the object, we also need to specify an attribute.
    print([beach.location for beach in beaches])

class Pokemon():
    type = "Fire"
    weakness = "Water"
    def __init__(self, master, special_move, color, hp, evolution):
        self.master = master
        self.special_move = special_move
        self.color = color
        self.hp = hp
        self.status = "Legendary" if hp > 150 else "Ordinary"
        self.evolutions = evolution
    
    def forms(self):
        return len(self.evolutions)

charizard = Pokemon("Ash", "Canon Blast", "Orange", 160, ["Charmander", "Charmeleon", "Charizard"])
typlosion = Pokemon("Ash", "Fire Storm", "Dark Green", 152, ["Cyndaquill", "Quilava", "Typhlosion"])
houndoom = Pokemon("Gary", "Fire Fang", "Black", 90, ["Houndour", "Houndoom"])
moltres = Pokemon("Anonymous", "Fiery Wrath", "Tangerine", 220, [])

print(charizard.status, houndoom.status)
print(typlosion.type, houndoom.type)
print(f"Moltres's HP reaches a staggering {moltres.hp} when it uses its special move '{moltres.special_move}'")
print(charizard.forms(), houndoom.forms(), moltres.forms())
#write a function that goes through all of the pokemons and returns the ones whose master is "Ash" and they have more than one evolved form.
def selection():
    charizard = Pokemon("Ash", "Canon Blast", "Orange", 160, ["Charmander", "Charmeleon", "Charizard"])
    typlosion = Pokemon("Ash", "Fire Storm", "Dark Green", 152, ["Cyndaquill", "Quilava", "Typhlosion"])
    houndoom = Pokemon("Gary", "Fire Fang", "Black", 90, ["Houndour", "Houndoom"])
    moltres = Pokemon("Anonymous", "Fiery Wrath", "Tangerine", 220, [])
    output = []
    for pokemon in [charizard, typlosion, houndoom, moltres]:
        if pokemon.master == "Ash" and pokemon.forms() > 1: #to get the return value of the Method 'forms', call it with a parenthesis
            output.append(pokemon)
    return output

if __name__ == '__main__': #checks if file is being run directly or through import
    pokemons = selection()
    print([member.special_move for member in pokemons])
else:
    print("Run from Import") #will only get executed when imported as module into another file

print("Classes Name: {}".format(__name__)) #when file is run directly, __name__ will be set to __main__, but when imported, it will be\
#set to the file's name(classes)

def main():
    print("Hello World")

if __name__ == '__main__':
    main()

