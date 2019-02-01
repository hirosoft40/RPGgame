# RPG Game by Hiroko Ross
# Nov 2018 / python3

import random

# list of items that the player can use
items = [
        ["evade", 2, ' can\'t get hit'],
        ["amore", 3, ' does not get damaged'],
        ["tonic", 3, ' receive 10 health points'],
        ["fireball", 3, ' attack last 2 times'],
        ["wind", 2, ' blow wind and lower enemy\'s point'],
        ["swap", 2, ' swap power with enemy'],
        ["changed my mind. Go back to main menu.", " ", " "]]

# list of actions
actions = ['fight enemies', 'do nothing','flee', 'go to the store','view character list', 'go to gem mountain']

class Character():
    def __init__(self, health, power, bounty):
        self.name = "Generic"
        self.health = health
        self.power = power
        self.coin = 20
        self.bounty = bounty
        self.myItems = []

    def attack(self, enemy):
        if enemy.alive() == 'dead':
            print (f"{enemy.name} is {enemy.alive()}. Please choose other enemy.")
        else:            
            if self.name.lower() == 'hero': 
                hero.doubleAttack(enemy)    
                if enemy.name.lower() == 'shadow': # Shadow
                    shadow.damage(self)  
                elif enemy.name.lower() == 'ninja':
                    ninja.attackBounceBack(self)
                elif enemy.name.lower() == ' medic ': 
                    medic.recuperated(enemy)
            elif self.name.lower() == 'goblin':
                goblin.damageHimself(enemy)
            elif self.name.lower() == 'bishop':
                bishop.giveAwayPower(enemy)
            else:
                enemy.health -= self.power  

            print("++++++++++++++++++++++++++++++")
            print("                                 ")
            print("ATTACK ｀O´)／☆★☆★（（（＊＿＊）））")
            print("                                 ")
            print("++++++++++++++++++++++++++++++")
            print(f"{self.name} does {self.power} damage to the {enemy.name}.")
            print(f"{enemy.name}'s health is now {enemy.health}.")
            self.print_alive_status(enemy)

    def print_alive_status(self, enemy):
        if hero.alive() == 'dead':
            print ("++++++++++++++++++++++++++++++")
            print(f"The {hero.name} is dead")
            print ("GAME OVER.")
            return False
        elif enemy.alive() == "dead":  
            self.coin += enemy.bounty 
            print("++++++++++++++++++++++++++++++")
            print("                                 ")
            print(f"The {enemy.name} is dead.")
            print(f"{self.name} received {enemy.bounty} bounty from {enemy.name}.")
            print(f"{self.name} now has {self.coin} coins.")
            
            if enemy.name.lower() == 'zombie': # if zombie, comeback
                zombie.comeBack()

        
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
        if len(self.myItems) == 0:
            print (f" : don't have any items.")
        else:
            for i in self.myItems:
                print (f" : has {i} item.")


class Hero(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Hero'
        self.amore = 0          # protect himself
        self.evade = 0
        self.tonic = 0
        self.fireball = 0
        self.wind = 0
        self.swap = 0
        self.usingItem = False
        self.detail = "20% of time, his power doubles"
        
    def doubleAttack(self, enemy):
        if random.random() < 0.2:
            print ("DOUBLE ATTACK ++<<<<...++<<<<")
            enemy.health -= self.power * 2 
             
        else:
            enemy.health -= self.power        
             


    def buyItems(self, item):
        amount = items[item][1]
        if item == 6:
            print ("Bye.")
            return False
        elif self.coin < amount:
            print("You don't have enough money to purchase it.")
            return False
        else:
            if item == 0: #evade
                if self.evade == 10:
                    print ("You can't buy more evade.")
                    return False
                else:
                    self.evade += 2
            elif item == 1: #amore
                self.amore += 2
            elif item == 2:
                self.tonic += 1
            elif item == 3:
                self.fireball += 1
            elif item == 4:
                self.wind += 1
            elif item == 5:
                self.swap += 1
            hero.myItems.append(items[item][0])
            print(f"Your purchased {items[item][0]} successfully.")
            hero.coin -= amount
            print(f"You spent {amount} coins and you have {hero.coin} coins left.")
            print(" ")

    def useItems(self, item, enemy):
        if item not in self.myItems:
            print(f"You do not own {item}")
            return False
        else:
            print("++++++++++++++++++++++++++++++")
            print("                                 ")
            print("ATTACK ｀O´)／☆★☆★（（（＊＿＊）））")
            print("                                 ")
            print("++++++++++++++++++++++++++++++")

            if item == 'evade':   # evade
                if random.random() < (0.3 * self.evade):
                    print (f"{self.name} evaded the attack!")
                else:
                    print (f"{enemy.name} was so strong.")
                    print(f"{self.name} cound not evade the attack!")
                    self.health -= enemy.power
            elif item == 'amore':  # amore
                print(f"{self.name} used amore.")
                self.amore -= 2
            elif item == 'tonic': 
                self.health += 10
                print(f'{self.name} recovered and now has {self.health} health points')
                self.tonic -= 1
            elif item == 'fireball':
                if random.random() < (0.3):
                    print ("٩(๑`^´๑)۶༄༅༄༅༄༅༄༅)`Д´)")
                    print (f"Firball Hit!")
                    enemy.health -= (self.health * 3)
                else:
                    print (f"ヽ(ﾟДﾟ;)ﾉ!!Oh, No! {enemy.name} avoided the fireball.")       
                self.fireball -= 1
            elif item == 'wind':
                self.wind -= 1
                print("(# `)3')▃▃▃▅▆▇▉▉▉")
                print(f"{self.name} blew wind and halved enemy's power.")
                self.health -= (enemy.power // 2)
            elif item == 'swap':
                self.swap -= 1
                print(f"{self.name} swaped power with {enemy.name}.")
                self.power = enemy.power
                print(f"{self.name} has {self.power} power.")
                enemy.power = self.power
                print(f"{enemy.name} has {enemy.power} power.")
            print(f"{self.name} 's health is now {self.health}.")
            print(f"{enemy.name}'s health is now {enemy.health}.")
            self.myItems.remove(item)
            self.print_alive_status(enemy)


class Goblin(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Goblin'
        self.detail = '20% of time, he hits himself. Lousy Goblin.'

    def damageHimself(self, enemy):
        if random.random() < 0.2:
            print (f"{self.name} attacked himself!")
            self.health -= self.power
        else:
            enemy.health -= self.power

class Zombie(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Zombie'
        self.detail = 'Can live up to 5 battles after 1st death'
        self.death_count = 0
    
    def comeBack(self):
        if self.death_count < 5 and self.health <= 0:
            print ("++++++++++++++++++++++++++++++")
            print (f"  ") 
            print (f"ﾍ（０Д０ﾍ） I am Zombie. I never die.. ") 
            print (f"  ") 
            self.health += 5
            self.death_count += 1
        else:
            self.health = 0
            hero.coin += self.bounty 
            print("++++++++++++++++++++++++++++++")
            print("                                 ")
            print(f"After 5 tries, the zombie is finally dead.")


class Shadow(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Shadow'
        self.attacked_count = 0
        self.detail = 'Take damage only once in 10 times'

    def damage(self, enemy):
        self.attacked_count += 1
        if self.attacked_count < 10:
            self.health -= enemy.power
        else:
            self.attacked_count = 0
            self.health -= 0

class Medic(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Medic'
        self.detail = "20% of time, he gets his health back by 2."

    def recuperated(self, enemy):
        if random.random() < 0.2:
            print (f"{self.name} recuperated 2 health points!")
            self.health += 2
        self.health -= enemy.power

class Bishop(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name ='Bishop'
        self.detail = '10% of time, he mistakenly gives health point.'

    def giveAwayPower(self, enemy):
        if random.random() < 0.3:
            print (f"Drunk {self.name} mistakenly gave youu back 2 health point!")
            enemy.health += 2
        enemy.health -= self.power

class Ninja(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Ninja'
        self.detail = '20% of time, he can bounce back the hit'

    def attackBounceBack(self, enemy):
        if random.random() < 0.2:
            print (f"{self.name} bounced back the attack!")
            enemy.health -= enemy.power
        else:
            self.health -= enemy.power

hero = Hero(10, 2, 10)
zombie = Zombie(5, 3, 3)
shadow = Shadow(1, 2, 7)
medic = Medic(3,3,2)
bishop = Bishop(8, 4, 6)
goblin = Goblin(6, 2, 4)
ninja = Ninja(7,3,5)

# ====== GEM MOUNTAIN to play guess a number game =========
def number_game():
    num = random.randint(1,10) # secret number
    print(" Can you guess the number?")
    print("> ", end=' ')

    while True:
        try:
            user_num = int(input())
        except ValueError:
            print ("Invalid input. Please type in number between 1 and 10.") 
            print("> ", end=' ')
        except:
            if user_num > 10 or user_num < 0:
                print ("Type in number between 1 and 10. ")
                print("> ", end=' ')
        else:
            if user_num == num:
                print ("*･ﾟﾟ･*:.｡..｡.:*ﾟ:*:✼✿(ღ✪ｖ✪)｡ﾟ:*:✼.｡✿.｡")
                print ("Yes, you won! You received 5 coins.")
                print (" ")
                return 5
            else:
                print("Ψ(｀∀´)Ψ")
                print ("Nope, %d is not right. %d is the number. You lost." % (user_num, num))
                print (" ")
                return 0

# ====== Function to handle error for user input ==========
def getInput(res, len_num):
    print(f"What would you like to {res}?: ")
    print("> ", end=' ')

    while True:
        if res == 'use':
            try:
                raw_input = input().lower()
                print (" ")
            except TypeError:
                print ("Invalid input. Please Type in item name.") 
                print("> ", end=' ')
            else:
                if raw_input not in ['evade', 'amore','tonic','fireball','wind','swap']:
                    print ("Please choose item name from above")
                else:
                    return raw_input
        else:
            try:
                raw_input = int(input())
                print (" ")
            except ValueError:
                print ("Invalid input. Please choose numbers from above list.") 
            else:
                if raw_input not in range(1,len_num+1):
                    print ("Please choose items numbers from above list.")
                    print("> ", end=' ')
                else:
                    return raw_input

def main():
    whoToFight = [zombie, shadow, medic, goblin, bishop, ninja]

    while hero.health >= 1 and len(whoToFight) > 0:
        num_fight = random.randint(0,len(whoToFight)-1)
        enemy = whoToFight[num_fight]
        hero.print_status()
        print("==========================================")
        for i in range(len(actions)):
            print (f"{i+1}. {actions[i]}")
        raw_input = getInput("do", len(actions))

        if raw_input == 1:
            print ("Would you like to use item? (y/n)")
            print("> ", end=' ')
            raw_input = input().lower()
            if raw_input == 'y':
                if len(hero.myItems) == 0:
                    print (f"{hero.name} doesn't have any items.")
                    print ("You are brave. Go attack!")
                    print (" ")
                    hero.attack(enemy)
                else:
                    for i in hero.myItems:
                        print (f"{hero.name} has {i} item.")
                    itemToUse = getInput("use", len(items))
                    hero.useItems(itemToUse, whoToFight[num_fight])
            else:
                hero.attack(enemy)    

            if enemy.health > 0:
                enemy.attack(hero)
            else:
                whoToFight.remove(enemy)

        elif raw_input == 2:
            if enemy.health > 0:
                enemy.attack(hero)

        elif raw_input == 3:
            print("Goodbye.")
            break

        elif raw_input == 4:
            print("==========================================")
            print(f" WELCOME TO THE STORE : You have {hero.coin} coins.")
            print(" ------------------------------------------")
            print(" No.| name  | coins |  detail")
            print(" ------------------------------------------")
            for i in range(len(items)):
                print(f" {i+1}  |{items[i][0]} | {items[i][1]} |{items[i][2]} ")
            print("-------------------------------------------")
            item = getInput("buy", len(items))-1             
            hero.buyItems(item)

        elif raw_input == 5:
            print("==========================================")
            print("             CHARACTER LIST ")
            print(" ------------------------------------------")
            print(" name | health | power | detail")
            print(" ------------------------------------------")
            for i in whoToFight:
                print(f"{i.name} |   {i.health}   |   {i.power}   | {i.detail}")
            print(" ")

        elif raw_input == 6:  # if you win number game, you get 10 health
            print("==========================================")
            print(" WELCOME TO THE GEM MOUNTAIN")
            print(" ------------------------------------------")
            print(" In this gem mountain, you will receive 5 coins if you are lucky. ")
            print(" ")
            print(" The game is very simple. Just guess a number in my mind.")
            print(" I am thinking of a number between 1 and 10.")
            print(" ")
            num = number_game()
            hero.coin += num

        else:
            print("Invalid input {}".format(raw_input))

    if len(whoToFight) == 0:
        print("Congraturations! You defeated all enemies.")

main()
