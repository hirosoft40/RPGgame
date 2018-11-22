import random

items = [[" evade   ", 2, ' can\'t get hit'],
        [" amore   ", 3, ' does not get damaged'],
        [" tonic   ", 3, ' health + 10'],
        [" fireball", 3, ' attack last 2 times'],
        [" wind    ", 2, ' blow wind and lower enemy\'s point']]


class Character():
    def __init__(self, health, power, bounty):
        self.name = "Generic"
        self.health = health
        self.power = power
        self.coin = 20
        self.bounty = bounty
        self.attacked_count = 0

    def attack(self, enemy):
        if enemy.alive() == 'dead':        ## can't attack dead enemy
            print (f"{enemy.name} is {enemy.alive()}. Please choose other enemy.")
        else:
            self.noOfAttacked(enemy)    ## Attack Count increase == 
            
            if self.name.lower() == 'hero': 
                damage = hero.doubleAttack()    

            if enemy.name.lower() == 'shadow':
                damage = shadow.damage(self.power)  # self.power means attacker's power
            
            elif enemy.name.lower() == 'ninja':
                damage = ninja.attackBounceBack(self.power)
                if damage <= 0:
                    self.health -= self.power
            else:
                damage = self.power
                if enemy.name.lower() == 'medic': 
                    enemy.health += medic.recuperated()
                elif enemy.name.lower == 'bishop':
                    self.health += bishop.giveAwayPower()

                elif self.name.lower() == 'goblin':
                    self.health -= goblin.damageHimself()

            enemy.health -= damage  # attack

            print("++++++++++++++++++++++++++++++")
            print("                                 ")
            print("ATTACK ｀O´)／☆★☆★（（（＊＿＊）））")
            print("                                 ")
            print("++++++++++++++++++++++++++++++")
            print(f"{self.name} does {damage} damage to the {enemy.name}.")
            print(f"{enemy.name}'s health is now {enemy.health}.")

            if enemy.health <= 0:  # enemy died 
                self.coin += enemy.bounty # get bounty from defeating
                #enemy.isDead = True
                if enemy.name.lower() == 'zombie': # if zombie, comeback
                    zombie.comeBack()
                    #enemy.isDead = False
                print("++++++++++++++++++++++++++++++")
                print("                                 ")
                print(" ♫•*¨*•.¸¸♪✧(๑´▿｀๑)♫•*¨*•.¸¸♪✧")
                print("                                 ")
                print(f"The {enemy.name} is {enemy.alive()}.")
                print(f"{self.name} received {enemy.bounty} bounty from {enemy.name}")
                print(f"{self.name} has {self.coin} coins.")
                
            if self.health <= 0: # self died
                print ("++++++++++++++++++++++++++++++")
                print(f"The {self.name} is {self.alive()}.")
                print ("GAME OVER.")
                return False
        
        # 自分が死んだら、ゲーム終了

    def noOfAttacked(self, enemy):
        if enemy.attacked_count >= 10:
            enemy.attacked_count = 0 
        else:
            enemy.attacked_count += 1

    def alive(self):
        if self.health > 0:
            return 'alive' 
        else:
            return 'dead'

    def print_status(self):
        print ("++++++++++++++++++++++++++++++")
        print (f"{self.name}\'s detail'")
        print (f" : has {self.health} health points.")
        print (f" : has {self.power} power points.")
        print (f" : has {self.coin} coins.")
        print (f" : bounty point is {self.bounty}.") 
        print (f" : was attacked {self.attacked_count} times.") 
        print ("++++++++++++++++++++++++++++++")

class Hero(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Hero'
        self.amore = 0          # protect himself
        self.tonic = 10         # health + 10
        self.evade = [0,0]
        self.fireball = 0
        self.wind = 0
        self.myItems = []
        
    def doubleAttack(self):
        if random.random() < 0.2:
            print ("DOUBLE ATTACK ++<<<<...++<<<<")
            return self.power * 2 
        else:
            return self.power

    def buyItems(self, item):
        if item == 'evade':
            self.evade += 2
        elif item == :
            self.amore += 2
        elif item == 2:
            self.tonic += 1
        elif item == 3:
            self.fireball += 1
        elif item == 4:
            self.wind += 1
        self.myItems.append[item]
        self.coin -= items[[item-1][1]]

    def useItems(self, item, enemy):
        if items == 0:
            self.evade += 2
        elif items == 1:
            self.amore += 2
            self.amore -= enemy.power
        elif items == 2:
            self.tonic -= 1
            self.health += 10
        elif items == 3:
            self.fireball-= 1
            ここからやりますよーーーーーーーー頭が限界です。
            ファイヤーボール受けた後の対応を考えましょう
        items == 4:
        wind
        


class Goblin(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Goblin'

    def damageHimself(self):
        if random.random() < 0.2:
            print (f"{self.name} attacked himself!")
            return self.power
        else:
            return 0

class Zombie(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Zombie'
    
    def comeBack(self):
        if self.health <= 0:
            print ("++++++++++++++++++++++++++++++")
            print (f"Zombie Never Dies! ")

        

class Shadow(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Shadow'

    def damage(self, power):
        if self.attacked_count < 10:
            return 0
        else:
            return power


class Medic(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Medic'

    def recuperated(self):
        if random.random() < 0.2:
            print (f"{self.name} recuperated 2 health points!")
            return 2
        else:
            return 0

class Bishop(Character):
    
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name ='Bishop'

    def giveAwayPower(self):
        if random.random() < 0.1:
            print (f"Drunk {self.name} mistakenly gave youu back 2 health point!")
            return 2
        else:
            return 0

class Ninja(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Ninjya'

    def attackBounceBack(self, power):
        if random.random() < 0.2:
            print (f"{self.name} bounced back the attack!")
            return 0
        else:
            return power


hero = Hero(10, 2, 10)
zombie = Zombie(5, 3, 3)
shadow = Shadow(1, 2, 7)
medic = Medic(3,3,2)
bishop = Bishop(8, 4, 6)
goblin = Goblin(6, 2, 4)
ninja = Ninja(7,3,5)

hero.print_status()

    #goblin.print_status()

# ==========================================
#             CHARACTER MAP
# ------------------------------------------
# name    | health| power | bounty | Double Item |speciality
# ------------------------------------------
# Hero    |   10  |   2   |   10  | Amore       | 20% of time, his power doubles
# Zombie  |   5   |   3   |   3   |  n/a        | doesn't die even if his health is below zero
# Shadow  |   1   |   2   |   7   |  n/a        | 1 starting health but will only take damage about once out of every ten times he is attacked.
# Medic   |   3   |   3   |   2   | Super Tonic | 20% of time, He gets his point back by 2 when attacked
# Goblin  |   9   |   5   |   4   | fireball    | He is lousy. 20 % of time, he hits himself
# Bishop  |   8   |   4   |   4   | potion      | 10% of chance. give other person some health
# Ninja   |   7   |   3   |   5   | wind        | 20% of time, the hit bounce back to attacker
# ==========================================
#             ITEM MAP
# ------------------------------------------
#       name    | coin  | character| purpose |speciality
# ------------------------------------------
# evade         |  4   |  Hero   |  can't get hit   | 
# Amore         |  1   |  Hero   | does not damage    | 
# Super Tonic   |  2   |  Hero   | health + 10    | 
# fireball      |  3   |  Goblin  | double     | ٩(๑`^´๑)۶༄༅༄༅༄༅༄༅)`Д´)
# wind          |  2   | Ninja    | blow wind and lower enemy's power| (# `)3')▃▃▃▅▆▇▉
# ==========================================


# # In this simple RPG game, the hero fights the goblin. He has the options to:

# # 1. fight goblin
# # 2. do nothing - in which case the goblin will attack him anyway
# # 3. flee
# #!/usr/bin/env python



import random 
# === guess the number 
def number_game():
    num = random.randint(1,10) # secret number
    print ("I am thinking of a number between 1 and 10.")
    user_num = int(input("What's the number? : "))

    # when number is way off, shows error.
    while True:
        if user_num > 10 or user_num < 0:
            print ("Type in number between 1 and 10. ")
        elif user_num == num:
            print ("Yes, you won! You received 10 coins.")
            return num
        else:
            print ("Nope, %d is not right. You lost." % user_num)
            return 0

    #Loop out when number matches.

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2


    while goblin_health > 0 and hero_health > 0:
        print("==========================================")
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print("==========================================")
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. use items")
        print("5. go to the store")
        print("6. view enemies")
        print("7. try bonus coin")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
            # # Hero attacks goblin
            # goblin_health -= hero_power
            # print("You do {} damage to the goblin.".format(hero_power))
            # if goblin_health <= 0:
            #     print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        elif raw_input == "4":
            print("==========================================")
            print("     WELCOME TO THE STORE   ")
            print(" ------------------------------------------")
            print("   name    | coins  |  purpose")
            print(" ------------------------------------------")
            for i in range(len(items)):
                print(f"{items[i][0]} | {items[i][1]} |{items[i][2]} ")
            
            while True:
                try:
                    item = input("What would you like to buy?: ")
 
                except ValueError:
                    print ("Invalid input. Please choose numbers from above list.") 
                except:
                    if item not in items:
                        print ("Please choose items from above list.")
                else:
                    break

            hero.buyItems(item)

        elif raw_input == "5":
            #あとで書く。敵の詳細を見る。
            pass
        elif raw_input == "6":
            num = number_game()
            if num > 0:
                hero.health += num

        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            goblin.attack(hero)
            # Goblin attacks hero
            # hero_health -= goblin_power
            # print("The goblin does {} damage to you.".format(goblin_power))
            # if hero_health <= 0:
            #     print("You are dead.")

main()
