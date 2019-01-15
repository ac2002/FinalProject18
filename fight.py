import random
import sys
import time
class item:
    '''Make a weapon class'''
    def __init__(self, name, cost, atkbuf, accbuf, dodgebuf, hppotionbuf):
        self.name = name
        self.cost = cost
        self.atkbuf = atkbuf
        self.accbuf = accbuf
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
        self.gold = gold

speedforce = item("Speed Force Potion", 40, 0, 5, 15, 0)
helpotion = item("Health Potion", 15, 0, 0, 0, 1)
bea = item("Bea", 25, 4, 22, 0, 0)
arthur = item("Arthur", 35, 15, 30, 1, 0)
batarang = item("Batarang", 10, 3, 7, 0, 0)
berserker = item("Berserker Scroll", 95, 50, 0, 0, 0)
club = item("Club", 8, 1, 0, 0, 0)
dragonbreath = item("Dragon's Breath", 175, 100, 40, 0, 0)
oompaloompa = item("Oompa Loompa", 250, 150, 55, 22, 1)
batman = character("Batman", 285, 15, 57, 50, 33, 3, 500, "Batmobile", 1)
wade = character("Deadpool", 275, 12, 64, 77, 37, 1, 0, "Iron Giant", 1)
bilbo = character("Bilbo", 250, 10, 48, 80, 38, 1, 0, "Gandalf", 1)
sbot = character("Stormtrooper", 55, 7, 40, 15, 20, 0, 0, "", 0)
mbot = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
hbot = character("Dementor", 105, 10, 32, 80, 15, 0, 0, "", 0)
sbot1 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, 0, "", 0)
sbot2 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, 0, "", 0)
sbot3 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, 0, "", 0)
sbot4 = character("Stormtrooper", 55, 7, 31, 15, 50, 0, 0, "", 0)
mbot1 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
mbot2 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
mbot3 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
mbot4 = character("Sixer", 75, 12, 45, 70, 25, 0, 0, "", 0)
hbot1 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
hbot2 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
hbot3 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
hbot4 = character("Dementor", 105, 40, 47, 80, 30, 0, 0, "", 0)
items = [speedforce, helpotion, bea, arthur, batarang, berserker, club, dragonbreath, oompaloompa]
def addstat(self, item):
    self.gold = self.gold - item.cost
    print(f"You now have {self.gold} gold")
    self.attack = self.attack + item.atkbuf
    print(f"You gained {item.atkbuf} attack. You now have {self.attack} attack")
    self.accuracy = self.accuracy + item.accbuf
    print(f"You gained {item.accbuf} accuracy. You now have {self.accuracy} accuracy")
    self.dodge = self.dodge + item.dodgebuf
    print(f"You gained {item.dodgebuf} elusiveness. You now have {self.dodge} elusiveness")
    self.healthpotions = self.healthpotions + item.hppotionbuf
    print(f"You gained {item.hppotionbuf} healthpotions. You now have {self.healthpotions} healthpotions.")
def shop(self):
    print("You now visit the shop!")
    print("Be careful though! You can only buy one item per round, and if you mistype by accident, you're screwed! Type the item exactly as it appears, or the shopkeeper will throw you out!")

    time.sleep(1)
    print(f"You have {self.gold} gold.")
    print("You can buy: ")
    for x in items:
        print(f"{x.name} which costs {x.cost}")
    itembought = input("So, would you like to buy anything?").lower()
    if itembought == "speed force potion" and self.gold >= speedforce.cost:
        print("You bought the Speed Force Potion! Congrats!")
        addstat(user, speedforce)
    elif itembought == "helpotion" and self.gold >= helpotion.cost:
        print("You bought a health potion! Nice!")
        addstat(user, helpotion)
    elif itembought == "bea" and self.gold >= bea.cost:
        print("You bought Bea the sword! Cool!")
        addstat(user, bea)
        items.remove(bea)
    elif itembought == "arthur" and self.gold >= arthur.cost:
        print("You bought Arthur the other sword! Awesome!")
        addstat(user, arthur)
        items.remove(arthur)
    elif itembought == "batarang" and self.gold >= batarang.cost:
        print("You bought a Batarang! Dope!")
        addstat(user, batarang)
        items.remove(batarang)
    elif itembought == "berserker scroll" and self.gold >= berserker.cost:
        print("You bought a Berserker Scroll! Cool!")
        addstat(user, berserker)
        itmes.remove(berserker)
    elif itembought == "club" and self.gold >= club.cost:
        print("You bought a club! Cool!")
        addstat(user, club)
        items.remove(club)
    elif itembought == "dragon's breath" and self.gold >= dragonbreath.cost:
        print("You bought the Dragon's Breath! Cool!")
        addstat(user, dragonbreath)
        items.remove(dragonbreath)
    elif itembought == "oompa loompa" and self.gold >= oompaloompa.cost:
        print("You bought a pet Oompa Loompa! Cool!")
        addstat(user, oompaloompa)
        items.remobe(oompaloompa)
    elif itembought == "I just wanna win":
        print("Your wish is granted. You win! Congratulations!")
        sys.exit()
    else:
        print("That is invalid, so sucks to be you. I hope you die next round! Type better next time! :)")



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
print("Oh lmao I forgot one last thing these enemies are reincarnations of their movie selves. We all know that zombies don't die fast. As such, they will attack you even after you kill them. You just have to dodge it, I guess.")
user = input("Choose a character: Wade, Bilbo, or Batman: ").title()
if user == "Wade":
    user = wade
elif user == "Bilbo":
    user = bilbo
elif user == "Batman":
    user = batman
else:
    print("That is an invalid character. Try again!")

def fighting(self, other):

    while self.hp > 0 and other.hp > 0:

        fight(self, other)
        time.sleep(0)
        showstat(self, other)
        time.sleep(0)
        fight2(other, self)
        time.sleep(0)
        showstat(self, other)
        time.sleep(0)
        if self.hp < 0:
            print("Oh no, you died! Sucks to suck!")
            quit()
        if other.hp < 0:
            print("Looks like you won! Cool.")
            print(f"You have {self.healthpotions} healthpotions.")
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
    room = input("Choose a room, 1, 2, 3: ")
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
print("You got 40 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 40
healthpotion(user)
shop(user)
chooseroom(user, bot2)
print("You got 60 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 60
healthpotion(user)
shop(user)
chooseroom(user, bot3)
print("You got 75 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 75
healthpotion(user)
shop(user)
chooseroom(user, bot4)
print("You got 90 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 90
healthpotion(user)
shop(user)
chooseroom(user, bot5)
print("You got 125 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 125
healthpotion(user)
shop(user)
#showstat(user, bot1)
#fight(user, bot1)
#fight2(user, bot1)
#showstat(user, bot2)
#print("Welcome to the dungeon, challenger! Here you will face some of the most amazing and powerful characters of all time. If you get the hardest boss of all, you're probably screwed. A little, anyways.")




