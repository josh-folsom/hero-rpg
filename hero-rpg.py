#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:
    def __init__ (self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def alive(character):
        if character.health > 0:
           return True
    def print_status_of_Char(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, attackee):
       # Goblin attacks hero
       attackee.health -= self.power
       print("{} does {} damage to {}.".format(self.name, self.power, attackee.name))
       if attackee.health < 1 and attackee.name != "Zombie":
           print("{} is dead.".format(attackee.name))
       else:
           print("{} is UNDEAD, your attacks have no effect".format(attackee.name))

class Hero(Character):
    pass

class Zombie(Character):
    pass

    def alive(zombie):
        zombie.health = 0
        return True

    def print_status_of_Char(self):
        print("{} is not going to get any deader, you better flee!".format(self.name, self.health))

    # def attack(self, attackee):
    #    # Goblin attacks hero
    #    attackee.health -= self.power
    #    print("{} does {} damage to {}.".format(self.name, self.power, attackee.name))
    #    if attackee.health <= 0:
    #        print("{} is dead.".format(attackee.name))
#    def alive(hero):
#        if hero.health > 0:
#            return True
# #           self.health = hero.alive
 #    def attack(hero, goblin):
 # #       goblin.health = 6
 #        goblin.health -= hero.power
 #        print("You do {} damage to the goblin.".format(hero.power))
 #        if goblin.health <= 0:
 #            print("The goblin is dead.")

class Goblin(Character):
    pass

hero = Hero('Hero', 10, 5)
goblin = Goblin('Goblin', 6, 2)
zombie = Zombie('Zombie', 6, 2)


def main():
#    while goblin.alive() and hero.alive():
    while zombie.alive() and hero.alive():
        hero.print_status_of_Char()
#         print("You have {} health and {} power.".format(hero.health, hero.power))
#        goblin.print_status_of_Char()
        zombie.print_status_of_Char()
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            hero.attack(zombie)
#            hero.attack(goblin)
            # Hero attacks goblin
            # goblin_health -= hero_power
            # print("You do {} damage to the goblin.".format(hero_power))
            # if goblin_health <= 0:
            #     print("The goblin is dead.")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if zombie.health < 1:
            zombie.attack(hero)
#        if goblin.health > 0:
#            goblin.attack(hero)

if __name__ == "__main__":
  main()
