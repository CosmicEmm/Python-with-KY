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
print(naples_beach.uppercase())

#Write a function that goes through all of the beaches and returns the ones that are 