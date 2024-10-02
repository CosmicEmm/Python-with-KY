print("Hello World")
print((1+2)*8)
print(1 > 0.5 and 2 < 5)
x = [1,2,3,4,5]
x[2]= 9
y = x
print(y)

t = (0,0,0,0,2)
t = (0,0,0,0,1)
print(t)

# Complex Numbers
z= complex(1,3)
print(z)

h=(1,5,6,7)
print(h[2])
real_madrid={23:"Kroos", 23: "MJ", 10:"Modric", 7:"Ronaldo"}
print(real_madrid[23])
print(["BBC"]+["MSN"])
d= (1,2,3)
d=(1,2,3,4)
print(d)
x = "Real Madrid"
print(x)
x +=" are kings of Europe"
print(x)
gfg = {1,2,3,4,5}
gfg.add(9)
print(gfg)
gfg.add(10)
print(gfg)
a = (1,2,3,4)
print(a)
a = (1,2,3)
print(a)

# Using Conditionals
like_video = input("Did you like the video? ")
like_kylie = input("Do you like Kylie? ")

if like_video.upper() == "YES" and like_kylie.upper() == "YES":
    print("You like girls who are beautiful as well as smart")
elif like_video.upper() == "NO" and like_kylie.upper() == "YES":
    print("Admit it. You only watch her videos because she's cute")
else:
    print("That's cap. I don't believe it for a second")

animals_rating = float(input("How do you rate Animals by Pink Floyd? "))
if animals_rating >= 8:
    print("Listen on repeat")
    print("Share on social media")
    print("Obsess over it")
elif animals_rating >= 5:
    print("Give it another chance")
    print("Trust me. It'll build on you")
elif animals_rating >= 3:
    print("We need to have a conversation asap")
    print("Did you take your daily dose?")
else:
    print("Meet me in the parking lot after work")

# Conditionals don't always have to be a Boolean expression
vinicius = 0
if vinicius:
    print("Vini BallondOro")
else:
    print("Jude BallondOro")