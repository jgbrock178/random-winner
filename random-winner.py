import csv
import random

entrants = []

# Load in all entrants from CSV file.
with open('entrants.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        entrant = {
            "name": row["name"],
            "id": row["id"]
        }
        entrants.append(entrant)

random.shuffle(entrants)

i = 0
end = " "
for entrant in entrants:
    print(entrant["id"], end=end)
    i = i + 1
    if i == 9:
        end = "\n"
        i = -1
    else:
        end = " "
        
print("\n\n\n")
print("Loaded in " + str(len(entrants)) + " entrants and shuffled.")

try:
    seed = int(input("Enter seed: "))
except ValueError:
    print("That's not an integer. Try again.")

input("Seed set.\n\nPress enter to choose a winner...")

random.seed(seed)
winner = random.choice(entrants)

length = len(winner["name"]) + 20

print("\n╭" + "─" * length + "╮")
print("│\033[5;31m" + "CONGRATULATIONS".center(length, " ") + "\033[0;0m│")
print("│" + " " * length + "│")
print("│\033[0;34m" + winner["name"].center(length, " ") + "\033[0;0m│")
print("│\033[0;33m" + winner["id"].center(length, " ") + "\033[0;0m│")
print("│" + " " * length + "│")
print("╰" + "─" * length + "╯")
print()
print("See https://github.com/jgbrock178/random-winner for code.".center(length + 2, " "))