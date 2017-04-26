#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""


# class Character:
#     def __init__ (self, name, health, power):
#         self.name = name
#         self.health = health
#         self.power = power

class Hero:
   def __init__ (self, health, power):
       self.health = health
       self.power = power

   def attack(hero, goblin):
#       goblin.health = 6
       goblin.health -= hero.power
       print("You do {} damage to the goblin.".format(hero.power))
       if goblin.health <= 0:
           print("The goblin is dead.")

class Goblin:
   def __init__ (self, health, power):
       self.health = health
       self.power = power

   def attack(goblin, hero):
       # Goblin attacks hero
       hero.health -= goblin.power
       print("The goblin does {} damage to you.".format(goblin.power))
       if hero.health <= 0:
           print("You are dead.")


hero = Hero(10, 5)
goblin = Goblin(6, 2)

# hero_health = hero.health
# hero_power = hero.power
# goblin_health = goblin.health
# goblin_power = goblin.power


def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            hero.attack(goblin)
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

        if goblin.health > 0:
            goblin.attack(hero)
            # # Goblin attacks hero
            # hero.health -= goblin.power
            # print("The goblin does {} damage to you.".format(goblin.power))
            # if hero.health <= 0:
            #     print("You are dead.")

if __name__ == "__main__":
  main()
