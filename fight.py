import random

class character:
    '''Make a character class'''
    def __init__(self, name, hp, defense, attack, accuracy, dodge):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.accuracy = accuracy
        self.dodge = dodge

batman = character("Batman", 132, 38, 57, 50, 32)
wade = character("Wade", 175, 57, 64, 77, 1)
bilbo = character("Bilbo", 120, 22, 48, 80, 65)
sbot = character("Stormtrooper", 55, 7, 22, 50, 50)
mbot = character("Sixer", 75, 20, 45, 70, 65)
hbot = character("Dementor", 105, 29, 47, 80, 85)
user = input("Choose a character: Wade, Bilbo, or Batman")
if user == "Wade":
    user = wade
elif user == "Bilbo":
    user = bilbo
elif user == "Batman":
    user = batman
else:
    print("That is an invalid character. Try again!")
red = random.randint(1, 100)
blue = random.randint(1, 100)
green = [hbot, mbot, sbot]
purple = random.choice(green)
def showstat(self):
    print(f'Uh oh! Like we have a fight breaking out! The fighters are: {self.name} and {purple.name}!')
    print(f"You have:{self.hp} hp, {self.defense} defense, {self.attack} attack, {self.accuracy} accuracy, and {self.dodge} evasiveness.")
    print(f"Your enemy has:{purple.hp} hp, {purple.defense} defense, {self.attack} attack, {self.accuracy} accuracy, and {self.dodge} evasiveness.")
def fight(self, other):
    if other == hbot:
        print("You encounter a dementor! It drains the life from you! Minus 5 hp and attack immediately!")
        self.attack -= 5
        self.hp -= 5
    if red < self.accuracy and blue > other.dodge:
        print(f"{self.name} attacks {other.name}! The attack is super effective! It deals {self.attack - other.defense} damage! What a hit!")
    else:
        print(f"{other.name} dodged the attack! Better luck next time, {self.name}!")
def fight2(other, self):
    if other == hbot:
        print("You encounter a dementor! It drains the life from you! Minus 5 hp and attack immediately!")
        self.attack -= 5
        self.hp -= 5
    elif red < self.accuracy and blue > other.dodge:
        print(f"{other.name} attacks {self.name}! The attack is super effective! It deals {other.attack - self.defense} damage! What a hit!")
    else:
        print(f"{self.name} dodged the attack! Better luck next time, {other.name}!")


showstat(user)
fight(user, purple)
fight2(purple, user)