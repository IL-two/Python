from random import randint

class Warrior:

    def __init__(self, name = "Unnamed warior"):
        self.__health = 100
        self.__name = name
        self.__life = True

    @property
    def health (self):
        return self.__health

    @property
    def name (self):
        return self.__name

    @property
    def life (self):
        return self.__life

    @life.setter
    def life (self, value):
        self.__life = value

    def warriorLife (self):
        if (self.__health <= 0):
            self.life = False

    def damage(self):
        self.__health -= 20
        print("{0} получил урон".format(self.name))
        print("У воина {0} осталось {1}hl".format(self.name, self.health))
        self.warriorLife()

    def attack (self, other):
        print("{0} атакует {1}".format(self.name, other.name))

    def attack_success(self):
        if (randint(0, 1) == 1):
            return True
        else:
            return False

    def printWarrior(self):
        lif = "Жив" if self.__life else "Метрв"
        print("{0} {1} имеет {2} здоровья.".format(self.name, lif, self.health))

class BattleField:

    def __init__(self, war1, war2):
        self.__warrior_1 = Warrior(war1)
        self.__warrior_2 = Warrior(war2)

    def winner(self):
        if (self.__warrior_1.life):
            print("Победил {0}! У него осталось {1}hl".format(self.__warrior_1.name, self.__warrior_1.health))
        else:
            print("Победил {0}! У него осталось {1}hl".format(self.__warrior_2.name, self.__warrior_2.health))

    def fight (self):

        self.__warrior_1.printWarrior()
        self.__warrior_2.printWarrior()
        while (self.__warrior_1.life and self.__warrior_2.life):

            if (self.__warrior_1.attack_success()):
                self.__warrior_1.attack(self.__warrior_2)
                self.__warrior_2.damage()
            else:
                self.__warrior_2.attack(self.__warrior_1)
                self.__warrior_1.damage()

        self.__warrior_1.printWarrior()
        self.__warrior_2.printWarrior()
        self.winner()





b = BattleField("Боец", "Не Боец")
b.fight()

