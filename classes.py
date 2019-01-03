class character:
    '''Make a character class'''
    def __init__(self, name, hp, defense, attack, accuracy, dodge):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.accuracy = accuracy
        self.dodge = dodge
batman = character("Batman", 82, 18, 7, 50, 32)
wade = character("Wade", 135, 37, 4, 77, 1)
bilbo = character("Bilbo", 50, 12, 8, 80, 65)
