import random

class Character():
    def __init__(self, health, power, bounty):
        self.name = "Generic"
        self.health = health
        self.power = power
        self.coin = 20
        self.bounty = bounty
        self.attacked_count = 0
        self.isDead = False

    def attack(self, enemy):
        #アッタクできるヘルスポイントがあるかチェック
        #while enemy.isDead != True:
        if enemy.isDead == True:        ## can't attack dead enemy
            print ("{enemy.name} is dead. Please choose other enemy.")
        else:
            self.noOfAttacked(enemy)    ## Attack Count increase == 
            
            if self.name.lower() == 'hero': 
                self.power = hero.doubleAttack()    
            if enemy.name.lower() == 'shadow':
                damage = shadow.damage(self.power)  
            else:
                damage = self.power

            enemy.health -= damage  # attack

            print("++++++++++++++++++++++++++++++")
            print("                                 ")
            print("BOMB ｀O´)／☆★☆★（（（＊＿＊）））")
            print("                                 ")
            print(f"{self.name} does {damage} damage to the {enemy.name}.")
            print(f"{enemy.name}'s health is now {enemy.health}.")
            print("                                 ")

            if enemy.health <= 0:  # enemy died 
                self.coin += enemy.bounty # get bounty from defeating
                enemy.isDead = True
                if enemy.name.lower() == 'zombie': # if zombie, comeback
                    zombie.comeBack()
                    enemy.isDead = False
                print("++++++++++++++++++++++++++++++")
                print("                                 ")
                print("YAAAY ♫•*¨*•.¸¸♪✧(๑´▿｀๑)♫•*¨*•.¸¸♪✧")
                print("                                 ")
                print(f"The {enemy.name} is dead.")
                print(f"{self.name} received {enemy.bounty} bounty from {enemy.name}")
                print(f"{self.name} has {self.coin} coins.")
                
            if self.health <= 0: # self died
                print ("++++++++++++++++++++++++++++++")
                print(f"The {self.name} is dead.")
                self.isDead = True
        
        # 自分が死んだら、ゲーム終了

    def noOfAttacked(self, enemy):
        if enemy.attacked_count >= 10:
            enemy.attacked_count = 0
        else:
            enemy.attacked_count += 1

    def alive(self):
        if self.health > 0:
            return "alive"
        else:
            return "dead"

    def print_status(self):
        print ("++++++++++++++++++++++++++++++")
        print (f"{self.name}\'s detail'")
        print (f" : has {self.health} health points.")
        print (f" : has {self.power} power points.")
        print (f" : has {self.coin} coins.")
        print (f" : bounty point is {self.bounty}.") 
        print (f" : was attacked {self.attacked_count} times.") 

class Hero(Character):
    # the arguments for this __init__ is for creating Hero instance object
    def __init__(self, health, power, bounty):
        # passing the same arguments to super class,
        # so when re-using Character constructor, 
        # Character constructor can work with Hero's arguments
        super().__init__(health, power, bounty)
        self.name = 'Hero'
    

    def doubleAttack(self):
        if random.random() < 0.2:
            return self.power * 2    
        else:
            return self.power

class Goblin(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Goblin'

class Zombie(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Zombie'
    
    def comeBack(self):
        if self.health <= 0:
            print ("++++++++++++++++++++++++++++++")
            print (f"Zombie Never Dies! ")
            self.health += random.randint(5,10)
            print (f"Zombie has {self.health} health! ")
        

class Shadow(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Shadow'

    def damage(self, power):
        if self.attacked_count < 10:
            return 0
        else:
            return power


class Wizard(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Wizard'

class Monster(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Monster'

hero = Hero(10, 2, 10)
goblin = Goblin(6, 2, 4)
zombie = Zombie(5, 3, 3)
wizard = Wizard(8, 4, 6)
monster = Monster(7, 3, 5)
shadow = Shadow(1, 2, 7)

hero.print_status()
goblin.attack(hero)
for i in range(3):
    hero.attack(zombie)
    #goblin.print_status()

# ==========================================
#             CHARACTER MAP
# ------------------------------------------
# name    | health| power | bounty |speciality
# ------------------------------------------
# Hero    |   10  |   2   |   10  | 
# Goblin  |   6   |   2   |   4   | 
# Zombie  |   5   |   3   |   3   | doesn't die even if his health is below zero
# Lousy Wizard  |   8   |   4   |   6   | 20% of 
# cleric  |   sometimes give pther person a point
# Ninja   |   7   |   3   |   5   | 20% of time, the hit bounce back to him
# Shadow  |   1   |   2   |   7   | 1 starting health but will only take damage about once out of every ten times he is attacked.
# Medic   |   3   |   3   |   2   | Can sometimes recuperate 2 health points after being attacked with a probability of 20%
# ==========================================

# # In this simple RPG game, the hero fights the goblin. He has the options to:

# # 1. fight goblin
# # 2. do nothing - in which case the goblin will attack him anyway
# # 3. flee
# #!/usr/bin/env python

# # In this simple RPG game, the hero fights the goblin. He has the options to:

# # 1. fight goblin
# # 2. do nothing - in which case the goblin will attack him anyway
# # 3. flee

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             hero.attack(goblin)
#             # # Hero attacks goblin
#             # goblin_health -= hero_power
#             # print("You do {} damage to the goblin.".format(hero_power))
#             # if goblin_health <= 0:
#             #     print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             goblin.attack(hero)
#             # Goblin attacks hero
#             # hero_health -= goblin_power
#             # print("The goblin does {} damage to you.".format(goblin_power))
#             # if hero_health <= 0:
#             #     print("You are dead.")

# main()
