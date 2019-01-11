import random
import sys
import time
class item:
    '''Make a weapon class, duh'''
    def __init__(self, name, cost, defbuf, atkbuf, accbuf, dodgebuf, hppotionbuf)
        self.name = name
        self.cost = cost
        self.defbuf = defbuf
        self.atkbuf = atkbuf
        self.accbut = accbuf
        self.dodgebuf = dodgebuf
        self.hppotionbuf = hppotionbuf
class character:
    '''Make a character class'''
    def __init__(self, name, hp, defense, attack, accuracy, dodge, healthpotions, gold, specialskill, specialskillnum):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.accuracy = accuracy
        self.dodge = dodge
        self.healthpotions = healthpotions
batman = character("Batman", 285, 28, 57, 50, 33, 3, 0, "Batmobile", 1)
wade = character("Wade", 275, 37, 64, 77, 1, 5, 0, "Iron Giant", 1)
bilbo = character("Bilbo", 250, 22, 48, 80, 38, 1, 0, "Gandalf", 1)
sbot = character("Stormtrooper", 55, 7, 40, 15, 50, 0, 0, "", 0)
mbot = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
hbot = character("Dementor", 105, 40, 52, 80, 30, 0, "", 0)
sbot1 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, 0, "", 0)
sbot2 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, "", 0)
sbot3 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, 0, "", 0)
sbot4 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, "", 0)
mbot1 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
mbot2 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
mbot3 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
mbot4 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
hbot1 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
hbot2 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
hbot3 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
hbot4 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
def shop():

def healthpotion(user1):
    if user.healthpotions > 0:
        magenta = input("Would you like to take a health potion?")
        if magenta == "y" or magenta == "yes":
           print("You used a health potion! Gain 40 health immediately! Now you won't die as fast!")
           user.hp = user.hp + 40
           user.healthpotions -= 1
        else:
           print("Okay then. I hope you die next round!")
print("Welcome to the Challenger, Nooblet! Are you ready to take on some of the greatest nemises in all of existence? No? Well that sucks, because you're gonna do it anyways¯\_(ツ)_/¯. At least you have some valuable allies. Enjoy!")
time.sleep(3)
print("The rules of this game are simple. You choose a character and adventure through the dungeon. There are a total of 5 rooms, each with a varying level of difficulty and a different enemy to face.")
print("Should you die within the rooms, there's no going back! If you somehow make it through the rooms, you will face a final boss. They all have special abilities and are very strong, so get ready to have some funnn!")
print("You will earn gold and can enter the shop after every fight. You can buy things like weapons, potions, and other similar items that will help you win(or maybe not). Guess you'll have to find out!")
user = input("Choose a character: Wade, Bilbo, or Batman: ")
if user == "Wade":
    user = wade
elif user == "Bilbo":
    user = bilbo
elif user == "Batman":
    user = batman
else:
    print("That is an invalid character. Try again!")
def fighting(self, other):

    while user.hp > 0 and other.hp > 0:

        fight(self, other)
        time.sleep(2)
        showstat(self, other)
        time.sleep(2)
        fight2(other, self)
        time.sleep(2)
        showstat(self, other)
        time.sleep(2)
        if user.hp < 0:
            print("Oh no, you died! Sucks to suck!")
            quit()
        if other.hp < 0:
            print("Looks like you won! Cool.")
            break
red = random.randint(1, 100)
blue = random.randint(1, 100)
green = [hbot, mbot, sbot, sbot1, sbot2, sbot3, sbot4, mbot1, mbot2, mbot3, mbot4, hbot1, hbot2, hbot3, hbot4]
bot1 = random.choice(green)


def showstat(self, other):
    print(f"You have:{self.hp} hp, {self.defense} defense, {self.attack} attack, {self.accuracy} accuracy, and {self.dodge} evasiveness.")
    print(f"Your enemy has:{other.hp} hp, {other.defense} defense, {other.attack} attack, {other.accuracy} accuracy, and {other.dodge} evasiveness.")
def fight(self, other):
    red = random.randint(1, 100)
    blue = random.randint(1, 100)
    yellow = self.attack - other.defense
    if yellow < 0:
        yellow == 0
    elif red < self.accuracy and blue > other.dodge:
        print(f"{self.name} attacks {other.name}! The attack is super effective! It deals {yellow} damage! What a hit!")
        other.hp = other.hp - yellow
        ("/n")
    else:
        print(f"{other.name} dodged the attack! Better luck next time, {self.name}!")
def fight2(other, self):
    red = random.randint(1, 100)
    blue = random.randint(1, 100)
    orange = other.attack - self.defense
    if red < self.accuracy and blue > other.dodge:
        print(f"{other.name} attacks {self.name}! The attack is super effective! It deals {other.attack - self.defense} damage! What a hit!")
        self.hp = self.hp - orange

    else:
        print(f"{self.name} dodged the attack! Better luck next time, {other.name}!")
def chooseroom(self, other):
    room = input("Choose a room, 1, 2, 3")
    if room == "1" or room == "2" or room == "3":
        print(f'Uh oh! Like we have a fight breaking out! The fighters are: {self.name} and {other.name}!')
        showstat(self, other)
        fighting(self, other)
    else:
        print("Choose again. Sorry, I didn't get that.")

#healthpotion(user)
green.remove(bot1)
bot2 = random.choice(green)
green.remove(bot2)
bot3 = random.choice(green)
green.remove(bot3)
bot4 = random.choice(green)
green.remove(bot4)
bot5 = random.choice(green)
green.remove(bot5)
chooseroom(user, bot1)
healthpotion(user)
chooseroom(user, bot2)
healthpotion(user)
chooseroom(user, bot3)
healthpotion(user)
chooseroom(user, bot4)
healthpotion(user)
chooseroom(user, bot5)
healthpotion(user)
#showstat(user, bot1)
#fight(user, bot1)
#fight2(user, bot1)
#showstat(user, bot2)
#print("Welcome to the dungeon, challenger! Here you will face some of the most amazing and powerful characters of all time. If you get the hardest boss of all, you're probably screwed. A little, anyways.")




