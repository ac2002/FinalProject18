import random
#import sys
import time
class item:
    '''Make a weapon class to implement buffs to the character's stats'''
    def __init__(self, name, cost, atkbuf, accbuf, dodgebuf, hppotionbuf):
        self.name = name
        self.cost = cost
        self.atkbuf = atkbuf
        self.accbuf = accbuf
        self.dodgebuf = dodgebuf
        self.hppotionbuf = hppotionbuf
class character:
    '''Make a character class just makes the characters you know'''
    def __init__(self, name, hp, defense, attack, accuracy, dodge, healthpotions, gold):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.accuracy = accuracy
        self.dodge = dodge
        self.healthpotions = healthpotions
        self.gold = gold
class boss:
    '''Make a boss class these guys are a little different than the characters so i just made them a separate class'''
    def __init__(self, name, hp, defense, attack, accuracy, dodge, specialskill):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.accuracy = accuracy
        self.dodge = dodge
        self.specialskill = specialskill
dracula = boss("Dracula", 730, 9, 50, 70, 25, "Drain")
geicolizard = boss("The Geico Lizard", 520, 6, 38, 100, 90, "Save 15% or more on car insurance")
magneto = boss("Magneto", 600, 1, 3, 60, 25, "Magnetic Field")
speedforce = item("Speed Force Potion", 70, 0, 5, 13, 0)
snakehead = item("Kevin Durant", 25, 10, 2, 5, 0)
cataclyst = item("The Cataclyst", 100, 50, 10, 0, 0)
ratstail = item("Rat's Tail", 75, 0, 0, 25, 0)
helpotion = item("Health Potion", 35, 0, 0, 0, 1)
bea = item("Bea", 40, 10, 14, 0, 0)
arthur = item("Arthur", 60, 15, 20, 1, 0)
batarang = item("Batarang", 10, 3, 7, 0, 0)
berserker = item("Berserker Scroll", 125, 50, 0, 0, 0)
club = item("Club", 8, 3, 0, 0, 0)
dragonbreath = item("Dragon's Breath", 225, 100, 40, 0, 0)
oompaloompa = item("Oompa Loompa", 400, 150, 55, 0, 1)
batman = character("Batman", 480, 15, 40, 70, 16, 2, 0)
wade = character("Deadpool", 535, 12, 37, 86, 20, 1, 0)
bilbo = character("Bilbo", 421, 9, 43, 90, 26, 1, 0)
sbot = character("Stormtrooper", 120, 7, 45, 60, 20, 0, 0)
mbot = character("Sixer", 195, 9, 45, 70, 25, 0, 0)
hbot = character("Dementor", 240, 13, 50, 80, 15, 0, 0)
sbot1 = character("Droid", 138, 8, 43, 61, 8, 0, 0)
sbot2 = character("Sim", 133, 7, 45, 57, 10, 0, 0)
sbot3 = character("Minion", 135, 7, 49, 53, 9, 0, 0)
sbot4 = character("Clone Trooper", 91, 7, 36, 64, 15, 0, 0)
mbot1 = character("Mafioso", 160, 7, 48, 71, 12, 0, 0)
mbot2 = character("69", 154, 9, 49, 80, 19, 0, 0)
mbot3 = character("Gangster", 169, 8, 52, 72, 13, 0, 0)
mbot4 = character("Meowth", 189, 10, 54, 76, 10, 0, 0)
hbot1 = character("Abominable Snowman", 248, 14, 43, 83, 14, 0, 0)
hbot2 = character("Swiper the Fox", 242, 12, 48, 87, 16, 0, 0)
hbot3 = character("Chimera", 250, 11, 56, 82, 14, 0, 0)
hbot4 = character("Manticore", 237, 13, 52, 84, 13, 0, 0)
def cheatcode(self):
    cheat = input("Do you know the hacks to this game? It's worth a try, honestly. It won't hurt you. So, what is it?").title()
    if cheat == "Celtics" or cheat == "Chargers":
        print("Well done, young adventurer. You have gained 50000 gold. Good work!")
        self.gold = self.gold + 50000
    else:
        print("Sorry, that really wasn't the one that I was looking for. Good try, though! Maybe it's the one for your private Minecraft server?")
def sanservinofinale():
    '''this function just implements the riddle that the finale after the final boss does. One history question for all the marbles'''
    print('HE SAYS:')
    print("This creature lives in Scotland by morning, works with steel by mid-day, and writes Gospel of Wealth by night. What is it?. SPELLING COUNTS!")
    answer = input("You have one chance. What is this creature that the dragon speaks of?").title()
    if answer == "Andrew Carnegie":
        print("The Dragon roars in fury as it has finally been defeated after millenia of ruling the dungeon. It turns on its belly and eats itself alive.")
        time.sleep(2)
        print("Congratulations, adventurer! You have secured the bread. Good game!")
        time.sleep(7000000000)
    else:
        print("The Dragon roars in triumph as it claims yet another unsuspecting adventurer. Wrong answer, fool! You get roasted and eaten. How fun :)")
        time.sleep(5050005050050505)

items = [speedforce, helpotion, bea, arthur, batarang, berserker, club, dragonbreath, oompaloompa, ratstail, snakehead, cataclyst]
#listed all the items that are in the shop so i can remove them and add them to the user's items
useritems = []
bosses = [dracula, geicolizard, magneto]
def addstat(self, item):
    '''buffs the stats of the user when they buy an item an deducts their gold count as well'''
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
def losestat(self, item):
    '''makes the user lose stats instead of gaining them'''
    self.attack = self.attack - item.atkbuf
    print(f"You lost {item.atkbuf} attack. You now have {self.attack} attack")
    time.sleep(1.5)
    self.accuracy = self.accuracy - item.accbuf
    print(f"You lost {item.accbuf} accuracy. You now have {self.accuracy} accuracy")
    time.sleep(1.5)
    self.dodge = self.dodge - item.dodgebuf
    print(f"You lost {item.dodgebuf} elusiveness. You now have {self.dodge} elusiveness")
    time.sleep(1.5)
def addstat2(self, item):
    '''this is literally just for the Magneto boss. I was gonna use the other addstat function but I didn't like the pronouns'''
    self.attack = self.attack + item.atkbuf
    print(f"Magneto gained {item.atkbuf} attack. He now has {self.attack} attack")
    time.sleep(1.5)
    self.accuracy = self.accuracy + item.accbuf
    print(f"Magneto gained {item.accbuf} accuracy. He now has {self.accuracy} accuracy")
    time.sleep(1.5)
    self.dodge = self.dodge + item.dodgebuf
    print(f"Magneto gained {item.dodgebuf} elusiveness. He now has {self.dodge} elusiveness")
    time.sleep(1.5)
def shop(self):
    '''time to go shopping!!! r is just a variable to set the while loop up so that users can buy as many items as they want. They buy, then the item gets removed from the shop unless its a healthpotion and they can buy more based on their gold count'''
    r = 0
    print("You now visit the shop!")
    time.sleep(1)
    while r < 5:
        time.sleep(1)
        print(f"You have {self.gold} gold.")
        time.sleep(1.5)
        print("You can buy: ")
        time.sleep(1)
        for x in items:
            print(f"{x.name} which costs {x.cost}")
            time.sleep(.35)
        itembought = input("Choose something to buy, or say no.").lower()
        if itembought == "speed force potion" and self.gold >= speedforce.cost:
            print("You bought the Speed Force Potion! Congrats!")
            addstat(user, speedforce)
            time.sleep(1)
            items.remove(speedforce)
            useritems.append(speedforce)
        elif itembought == "health potion" and self.gold >= helpotion.cost:
            print("You bought a health potion! Nice!")
            addstat(user, helpotion)
            time.sleep(1)
        elif itembought == "bea" and self.gold >= bea.cost:
            print("You bought Bea the sword! Cool!")
            addstat(user, bea)
            time.sleep(1)
            items.remove(bea)
            useritems.append(bea)
        elif itembought == "arthur" and self.gold >= arthur.cost:
            print("You bought Arthur the other sword! Awesome!")
            addstat(user, arthur)
            time.sleep(1)
            items.remove(arthur)
            useritems.append(arthur)
        elif itembought == "batarang" and self.gold >= batarang.cost:
            print("You bought a Batarang! Dope!")
            addstat(user, batarang)
            time.sleep(1)
            items.remove(batarang)
            useritems.append(batarang)
        elif itembought == "berserker scroll" and self.gold >= berserker.cost:
            print("You bought a Berserker Scroll! Cool!")
            addstat(user, berserker)
            time.sleep(1)
            items.remove(berserker)
            useritems.append(berserker)
        elif itembought == "club" and self.gold >= club.cost:
            print("You bought a club! Cool!")
            addstat(user, club)
            time.sleep(1)
            items.remove(club)
            useritems.append(club)
        elif itembought == "dragon's breath" and self.gold >= dragonbreath.cost:
            print("You bought the Dragon's Breath! Cool!")
            addstat(user, dragonbreath)
            time.sleep(1)
            items.remove(dragonbreath)
            useritems.append(dragonbreath)
        elif itembought == "oompa loompa" and self.gold >= oompaloompa.cost:
            print("You bought a pet Oompa Loompa! Whoop!")
            addstat(user, oompaloompa)
            time.sleep(1)
            items.remove(oompaloompa)
            useritems.append(oompaloompa)
        elif itembought == "rat's tail" and self.gold >= ratstail.cost:
            print("Wow, you really trust a rat? Unfortunate for you, I guess.")
            self.gold = self.gold - ratstail.cost

            losestat(user, ratstail)
            time.sleep(1)
            items.remove(ratstail)
        elif itembought == "Kevin Durant" and self.gold >= snakehead.cost:
            print("You bought the snake itself, only to realize it wasn't actually dead. It bites you and slithers away to join the Warriors. Nice!")
            self.gold = self.gold - snakehead.cost

            losestat(user, snakehead)
            time.sleep(1)
            items.remove(snakehead)
        elif itembought == "the cataclyst" and self.gold >= cataclyst.cost:
            print("You do realize that buying a giant explosive is not a good idea, right? It blows up right as you walk out. Luckily, you're damage immune. Unluckily, it has other consequences")
            self.gold = self.gold - cataclyst.cost

            losestat(user, cataclyst)
            time.sleep(1)
            items.remove(cataclyst)
        elif itembought == "No" or itembought == "no":
            print("Okay! Good luck!(Not really I hope you die). On with the show!")
            r = r + 5
        else:
            print("That is invalid, either because you don't have enough gold or because you mistyped. Either way, the shopkeeper gets offended by your attempt to swindle him and throws you out. He will let you back in once you have proved your worth and defeated another monster. How unfortunate :)")
            r = r + 5
            time.sleep(2)
def geicocheck(self):
    '''only because otherwise the user wins if they die from the car crash? idk not supposed to happen this checks the user's health before they fight to ensure user doesn't win immediately'''
    if self.hp <= 0:
        print("You died from a car crash! How unfortunate. Try harder next time I suppose.")
        time.sleep(59999)
    else:
        print("Oh, you survived the crash? Darn.")
def leech(self, other):
    '''leech, Dracula's special ability, which allows him to drain health and gain it. Activated every turn after both characters attack'''
    print("Dracula leeches 25 health from you! Now you're clearly gonna die! Hahahahahahahahahahahaha")
    self.hp = self.hp - 25
    other.hp = other.hp + 25
def carinsurance(self):
    '''car insurance thing, Geico Lizard's special ability. Basically they lose health and damage for gold which is useless'''
    print("Welcome to Geico! Hahahahhahhahhhaha! You can save 15% on car insurance, but you gotta crash your car first lmao ¯\_(ツ)_/¯. You gain 150 gold but uh you lose 150 health and all your defense immediately! Also have fun trying to hit a lizard :)")
    time.sleep(2)
    print("Oh, I forgot to mention. Gold is useless now. Oops.")
    self.gold = self.gold + 150
    self.hp = self.hp - 150
    self.defense = 0
def magneticfield(self, other):
    '''magneto's special ability, which lists the user's items before having Magneto steal all of them. Lists the user's stats and Magneto's stats after the items transfer'''
    print("You have: ")
    for x in useritems:

        print(f"{x.name}")
        time.sleep(1.2)
    print("When suddenly you hear:")
    time.sleep(1.5)
    print ("HAHHHAHHAHAHHHAHHAHAHAAHAHHAHAHHAAHAHAHAHAHAHAHAHAAHHAHAHAHAHAHAHAHHAHHAHAHHAHAHAHHAHAHAHA you're not allowed to use those! That's cheating, peasant!")
    time.sleep(2.5)

    for x in useritems:
        print(f"You lose your {x.name}")
        time.sleep(1.2)
        losestat(self, x)
        time.sleep(1)
    print("You know, I could really use these! Thanks for these magical items!  Welcome to the future, scrub! My name is Magneto, and today, YOU DIE!")
    time.sleep(1.5)
    for x in useritems:
        print(f"Magneto gets your {x.name}")
        time.sleep(1)
        addstat2(other, x)
        time.sleep(1)

def healthpotion(self):
    g = 0
    '''lets the user use a health potion'''
    while g < 5 and self.healthpotions > 0:
        magenta = input("Would you like to take a health potion?").lower()
        if magenta == "y" or magenta == "yes":
           print("You used a health potion! Gain 200 health immediately! Now you won't die as fast!")
           self.hp = self.hp + 200
           self.healthpotions = self.healthpotions - 1
        elif magenta == "n" or magenta == "no":
           print("Okay then. I hope you die next round!")
           g = g + 5
        else:
            print("Can you just say yes or no please?")

print("Welcome to the Challenger, Nooblet! Are you ready to take on some of the greatest nemises in all of existence? No? Well that sucks, because you're gonna do it anyways¯\_(ツ)_/¯. At least you have some valuable allies. Enjoy!")
time.sleep(6)
print("The rules of this game are simple. You choose a character and adventure through the dungeon. There are a total of 5 rooms, each with a varying level of difficulty and a different enemy to face.")
time.sleep(6)
print("Should you die within the rooms, there's no going back! If you somehow make it through the rooms, you will face a final boss. They all have special abilities and are very strong, so get ready to have some funnn!")
time.sleep(6)
print("You will earn gold and can enter the shop after every fight. You can buy things like weapons, potions, and other similar items that will help you win(or maybe not). Guess you'll have to find out!")
time.sleep(6)
print("Oh lmao I forgot one last thing these enemies are reincarnations of their movie selves. We all know that zombies don't die fast. As such, they will attack you even after you kill them. You just have to dodge it, I guess.")
time.sleep(6)
print("Buena muerte, mi contrario!")
#just some introductory lines the usual
'''o is another while loop activator thing so that the user has to pick a character'''
o = 0
while o < 5:

    user = input("Choose a character: Deadpool, Bilbo, or Batman: ").title()
    if user == "Deadpool":
        user = wade
        o = o + 5
    elif user == "Bilbo":
        user = bilbo
        o = o + 5
    elif user == "Batman":
        user = batman
        o = o + 5
    else:
        print("That is an invalid character. Try again!")
cheatcode(user)

def fighting(self, other):
    '''basically implements all the fight functions down later into one big function that makes them fight until one of them dies'''
    while self.hp > 0 and other.hp > 0:

        fight(self, other)
        time.sleep(1)
        print("")
        time.sleep(1)
        showstat(self, other)
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        fight2(other, self)
        time.sleep(1)
        print("")
        time.sleep(1)
        showstat(self, other)
        time.sleep(1)
        print("")
        time.sleep(1)
        if self.hp < 0:
            print("Oh no, you died! Sucks to suck!")
            time.sleep(59999)
        if other.hp < 0:
            print("Looks like you won! Cool.")
            print(f"You have {self.healthpotions} healthpotions.")
            break

def encounter(other):
    '''Idk why I made this it just introduces the fight I suppose'''
    print(f"You encountered a {other.name}! FIGHT!")

green = [hbot, mbot, sbot, sbot1, sbot2, sbot3, sbot4, mbot1, mbot2, mbot3, mbot4, hbot1, hbot2, hbot3, hbot4]
bot1 = random.choice(green)
#Choosing random bots for random rooms. I do that a lot
def showstat(self, other):
    '''Shows the stats of the user and the enemy each turn so that the player doesn't get confused or whatever'''
    print(f"You have:{self.hp} hp, {self.defense} defense, {self.attack} attack, {self.accuracy} accuracy, and {self.dodge} evasiveness.")
    print(f"Your enemy has:{other.hp} hp, {other.defense} defense, {other.attack} attack, {other.accuracy} accuracy, and {other.dodge} evasiveness.")

def fight(self, other):
    '''The fight function 1.0!!! Basically if the user is on target is a percentage that is the user's accuracy. Even if he is on target, the enemy has a percentage to dodge that attack which is their dodge/elusiveness number. Otherwise its just a fight.'''
    red = random.randint(1, 100)
    blue = random.randint(1, 100)
    yellow = self.attack - other.defense
    if yellow < 0:
        yellow == 0
    elif red < self.accuracy and blue > other.dodge:
        print(f"You attack the {other.name}! The attack is super effective! It deals {yellow} damage! What a hit! Dang it! Ugh can we nerf you?")
        other.hp = other.hp - yellow
    else:
        print(f"You tried to attack the {other.name}, but it dodged the attack! Great job, {other.name}! Now kill {self.name}!")
def fight2(other, self):
    '''Same thing as the first fight only the other guy is attacking you'''
    red = random.randint(1, 100)
    blue = random.randint(1, 100)
    orange = other.attack - self.defense
    if red < other.accuracy and blue > self.dodge:
        print(f"The {other.name} attacks you! The attack is super effective! It deals {orange} damage! Incredible! You're almost dead! Yay.")
        self.hp = self.hp - orange

    else:
        print(f"The {other.name} attacked you, but you somehow dodged the attack... Dang it, {other.name}, I was counting on you!")
def bossfight1(self, other):
    '''legit the same as the fights only the pronouns are slightly different'''
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    realatk = self.attack - other.defense
    if rand1 < self.accuracy and rand2 > other.dodge:
        print(f"You attack {other.name}! The attack is super effective! It deals {realatk} damage! What a hit! Dang it! Ugh can we nerf you?")
        other.hp = other.hp - realatk
    else:
        print(f"You tried to attack {other.name}, but it dodged the attack! Great job, {other.name}! Now kill {self.name}!")
def bossfight2(other, self):
    '''same idea as bossfight 1'''
    red = random.randint(1, 100)
    blue = random.randint(1, 100)
    orange = other.attack - self.defense
    if red < other.accuracy and blue > self.dodge:
        print(f"{other.name} attacks you! The attack is super effective! It deals {orange} damage! Incredible! You're almost dead! Yay.")
        self.hp = self.hp - orange

    else:
        print(f"{other.name} attacked you, but you somehow dodged the attack... Dang it, {other.name}, I was counting on you!")
def bossfighting(self, other):
    '''its the fighting thing only i just added the bossfight things with the pronouns in it so it looks cleaner'''
    while self.hp > 0 and other.hp > 0:

        bossfight1(self, other)
        time.sleep(1)
        showstat(self, other)
        time.sleep(1)
        bossfight2(other, self)
        time.sleep(1)
        showstat(self, other)
        time.sleep(1)
        if self.hp <= 0:
            print("Oh no, you died! Sucks to suck!")
            time.sleep(59999)
        if other.hp <= 0:
            print("Looks like you won! Cool.")
            break
def bossfightingdracula(self, other):
    '''its bossfighting but i had to include leech for dracula specifically so that's why its here'''
    while self.hp > 0 and other.hp > 0:

        bossfight1(self, other)
        time.sleep(2)
        showstat(self, other)
        time.sleep(2)
        bossfight2(other, self)
        time.sleep(2)
        showstat(self, other)
        time.sleep(2)
        leech(self, other)
        time.sleep(2)
        showstat(self, other)
        if self.hp <= 0:
            print("Oh no, you died! Sucks to suck!")
            time.sleep(59999)
        if other.hp <= 0:
            print("Looks like you won! Cool.")
            break
def bossfight():
    '''b continues the while loop. Just a bunch of text stuff and then you fight a boss based upon which room you choose. Special abilities included'''
    b = 0
    print("YOU HAVE REACHED THE BOSS ROOM! Nice. Lucky, as always, I see. ANYWAYS. CHOOSE YOUR FATE! DEATH BY FIRE, WATER, OR ICE?")
    print("You have to choose, by the way. There's no other option to win the game")
    while b < 5:
        bossroom = input("So, which will it be? Fire, water, or ice? ").lower()
        if bossroom == "fire":
            print("You slowly walk into the door laced with flames. The whole world goes black for a second.")
            time.sleep(2.5)
            print("You awaken. Suddenly, you find yourself driving down a road in a Lamborghini. Wow, what a great time, right?")
            time.sleep(2.5)
            print("WRONG. Wonder why, huh? Well, all's fine and dandy until you hear a voice in the chair next to you. You look, and somehow see nothing.")
            time.sleep(2.5)
            print("The noise gets louder. Curious, you turn to the chair with your full attention when you see a little lizard next to you. He says:")
            time.sleep(2.5)
            carinsurance(user)
            print("It's you versus the Geico Lizard. INSTANT L. (Hahahahhahahaha get it? L for lizard? Ok it was pretty bad). Anyways FIGHT!")
            showstat(user, geicolizard)
            time.sleep(1)
            geicocheck(user)
            time.sleep(1.5)
            bossfighting(user,geicolizard)
            print('You finally manage to grab the lizard by the neck and hold a dagger to its throat. As you are about to cut its head off, it says: "Ok ok ok ok fine. Here, I can offer you savings on home and auto insurance too." Satisfied, you put the lizard down and shake its hand, and you leave as partners and allies.')
            time.sleep(2.5)
            b = b + 5
        elif bossroom == "water":
            print("You slowly walk into the door engulfed with water. You didn't bring your goggles, so sit back and enjoy the show that you can't see.")
            time.sleep(2.5)
            print("The water slowly dissipates. Confused, and soaked, you open your eyes. You find yourself in a dark castle.")
            time.sleep(2.5)
            print("Still a little dizzy from your journey down the waterfall, you slowly get to your feet and stumble upon a giant coffin.")
            time.sleep(2.5)
            print('Upon the coffin, there is a sign that says:"DO NOT TOUCH". With the intelligence of a caterpillar, you touch it.')
            time.sleep(2.5)
            print("Suddenly, the whole castle begins to shake. Startled, you step back and watch as a figure emerges out of the coffin, with bats flanking its left and right side.")
            time.sleep(2.5)
            print("Amazing job lad, you've just awoken the greatest vampire of all time. Unfortunately, you don't have garlic to save you. Have fun getting your blood sucked! FIGHT!")
            showstat(user, dracula)
            time.sleep(1.5)
            bossfightingdracula(user,dracula)
            print("Dracula makes one final attempt at your neck, only to hopelessly miss, and collapses in a heap on the floor. You pick up the wooden stake at the stand next to his coffin, and pierce his heart. He explodes in a cloud of dust.")
            b = b + 5
        elif bossroom == "ice":
            print("You walk into the door that is snowy and Christmas-like, hoping that you'll become a part of the cast of Frozen or something of that nature.")
            time.sleep(2.5)
            print("Instead, as you walk in, the temperature drops suddenly, from 0 Celsius to 0 Kelvin. Your arms slowly begin to lose movement.")
            time.sleep(2.5)
            print("Before you know it, you are trapped within a giant ice cube. You become unconscious.")
            time.sleep(2.5)
            print('You wake up in a barren land. Wondering where you are, you slowly open your eyes and look around.')
            time.sleep(2.5)
            print("You observe laser beams and psychic powers. You quickly realize that you are in the future. You begin to walk around when suddenly you hear a loud screeching noice.")
            time.sleep(2.5)
            print('You walk towards the noise, only to observe a man in a helmet bending metal. You feel sympathy towards the metal, so you throw your spear at the man, only to find that it has no effect.')
            time.sleep(2.5)
            print('The man slowly turns towards you and you realize that this is a fight waiting to happen. Confident in your abilities, you quickly open your inventory to see:')
            time.sleep(1.5)
            magneticfield(user, magneto)
            print("I hope you didn't buy a lot of items! Actually, I hope you did. Huehuehue. FIGHT!")
            showstat(user, magneto)
            time.sleep(1.5)
            bossfighting(user, magneto)
            print("Magneto makes one last attempt to control your weapons, but they have no use at this point. You pull out your gun with a plastic bullet and finish him for good.")
            time.sleep(2.5)
            b = b + 5
        else:
            print("That's an invalid room, silly! You have to beat a boss to win, you know.")







def chooseroom(self, other):
    '''z is another while loop continuer. This basically allows the user to choose a room and fight a monster'''
    z = 0
    while z < 5:
        room = input("Choose a room, 1, 2, 3: ")
        if room == "1" or room == "2" or room == "3":
            encounter(other)
            showstat(self, other)
            time.sleep(1.5)
            fighting(self, other)
            z = z + 5
        else:
            print("Choose again. Sorry, I didn't get that.")

#Choosing random bottssss
green.remove(bot1)
bot2 = random.choice(green)
green.remove(bot2)
bot3 = random.choice(green)
green.remove(bot3)
bot4 = random.choice(green)
green.remove(bot4)
bot5 = random.choice(green)
green.remove(bot5)
bot6 = random.choice(green)
green.remove(bot6)
bot7 = random.choice(green)
green.remove(bot7)
chooseroom(user, bot1)
print("You got 40 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 40
healthpotion(user)
shop(user)
chooseroom(user, bot2)
print("You got 50 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 50
healthpotion(user)
shop(user)
chooseroom(user, bot3)
print("You got 60 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 60
healthpotion(user)
shop(user)
chooseroom(user, bot4)
print("You got 70 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 70
healthpotion(user)
shop(user)
chooseroom(user, bot5)
print("You got 80 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 80
healthpotion(user)
shop(user)
chooseroom(user, bot6)
print("You got 100 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 100
healthpotion(user)
shop(user)
chooseroom(user, bot7)
print("You got 120 gold for winning that encounter! Congrats! You'll die eventually!")
user.gold = user.gold + 120
healthpotion(user)
shop(user)
#After every fight, the user visits the shop and can use a health potion
print("THIS IS YOUR LAST CHANCE, CHAMPION. IF YOU HAVE ANY HEALTH POTIONS LEFT, USE THEM NOW, OR FACE ETERNAL PERIL!!!")
healthpotion(user)
bossfight()
#After 7 rooms, the user fights the boss. If they win the code continues
time.sleep(10)
#For dramatic effect
print("Wait a second? YOU THOUGHT YOU WERE DONE??!")
time.sleep(.5)
print("THERE IS ONE LAST TRIAL AWAITING YOU. THE GOLDEN DOOR!!")
time.sleep(.8)
#q makes more while loop stuff
q = 0
while q < 5:
    '''Legit just makes them go ito the room and answer a question. It's mostly for connective text'''
    answer = input("WILL YOU ENTER THE GOLDEN GATE?").lower()
    if answer == "yes" or answer == "y":
        print("YOU WALK INTO YOUR FINAL TRIAL. THERE AWAITS A GIANT DRAGON, OF MONSTROUS SIZE AND LENGTH AND GIRTH")
        print("AS YOU APPROACH, HE OPENS HIS MIGHTY MOUTH AND......")
        time.sleep(6)
        sanservinofinale()
        q = q + 5
    else:
        print("Just do it already. I'll even compliment you if you somehow manage to win. You do realize that there's no emergency exit, right?")
