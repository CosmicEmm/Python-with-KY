word = input("Channel Name: ")
madlib = "Subscribe to " + word
print(madlib)

# .format method
player = input("Who scored the winning goal in the World Cup? ")
national_team = input("Which team did he play for? ")
opposition_team = input("Which team did he score against? ")
year = input("What year did the World Cup happen? ")
football_heritage = "{P} of {NT} scored the winning goal against {OT} in the group stage of \
World Cup {Y}.".format(P = player, NT = national_team, OT = opposition_team, Y = year)
print(football_heritage)

# building a madlib using the .format method
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")
madlib = "Computer Programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay blessed \
and {verb2} like you are {famous_person}.".format(adj=adj, verb1=verb1, verb2=verb2, famous_person=famous_person)
print(madlib)


