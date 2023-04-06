# George Tannous 1971969
# 11.27
roster = {}

for i in range(5):
    jersey_number = int(input("Enter player {}'s jersey number:\n".format(i+1)))
    rating = int(input("Enter player {}'s rating:\n".format(i+1)))
    print()
    roster[jersey_number] = rating

sorted_roster = sorted(roster.items())
print("ROSTER")
for jersey_number, rating in sorted_roster:
    print("Jersey number: {}, Rating: {}".format(jersey_number, rating))

menu = """
MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
"""

while True:
    print(menu)
    option = input("Choose an option:\n")
    if option == "o":
        print("\nROSTER")
        for jersey_number, rating in sorted_roster:
            print("Jersey number: {}, Rating: {}".format(jersey_number, rating))
    elif option == "a":
        jersey_number = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        roster[jersey_number] = rating
        sorted_roster = sorted(roster.items())
    elif option == "d":
        jersey_number = int(input("Enter a jersey number:\n"))
        if jersey_number in roster:
            del roster[jersey_number]
            sorted_roster = sorted(roster.items())
    elif option == "u":
        jersey_number = int(input("Enter a jersey number:\n"))
        if jersey_number in roster:
            rating = int(input("Enter a new rating for player:\n"))
            roster[jersey_number] = rating
            sorted_roster = sorted(roster.items())
    elif option == "r":
        rating_threshold = int(input("Enter a rating:\n"))
        print("\nABOVE {}".format(rating_threshold))
        for jersey_number, rating in sorted_roster:
            if rating > rating_threshold:
                print("Jersey number: {}, Rating: {}".format(jersey_number, rating))
    elif option == "q":

        break
