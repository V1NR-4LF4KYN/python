#python3

# I am trying to build  this kind of RPG from school. I coded it in JAVA before...

'''
--------------------  RULES  ---------------------------------------------------------
There are Heroes and there are Monsters
They each have HealthPoints (HP) and an Attack-Value (ATT)
The ATT is constructed out of their Strength (STR) and their Attack-Bonus (BONUS)
The BONUS actually belongs to Weapons and not to a Hero/Monster
Weapons can be equipped by Heroes/Monsters

A Hero can fight a Monster. The One with the Higher Attack-Value (ATT) Wins
The Loser loses a HealthPoint (HP)
When one of the player's HealthPoints (HP) drops below 0 the Battle Ends
Heroes have Names.

'''
# HERO CLASS
class Hero:
    # initiation
    def __init__(self, name, STR, ATT, HP):
        self.name = name
        self.STR = STR
        self.ATT = ATT
        self.HP = HP
    
    # getters
    def get_name(self):
        return self.name
    
    def get_STR(self):
        return self.STR
    
    def get_ATT(self):
        return self.ATT
    
    def get_HP(self):
        return self.HP
    
    # setters
    def set_name(self, new_name):
        self.name = new_name
    
    def set_STR(self, new_STR):
        self.STR = new_STR
    
    def set_ATT(self, new_ATT):
        self.ATT = new_ATT
    
    def set_HP(self, new_HP):
        self.HP = new_HP
    
    
    # methods
    def attack(self, Monster):
        if Monster.ATT > self.ATT:
            self.HP -= 1
        else:
            Monster.HP -= 1
    
    
    
# MONSTER CLASS
class Monster:
    # initiation
    def __init__(self, ATT, HP):
        self.ATT = ATT
        self.HP = HP
    
    # getters
    def get_ATT(self):
        return self.ATT
    
    def get_HP(self):
        return self.HP
    
    # setters
    def set_ATT(self, new_ATT):
        self.ATT = new_ATT
    
    def set_HP(self, new_HP):
        self.HP = new_HP
    
    
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# main func
def main():
    # creating players
    h1 = Hero("James", 10, 5, 100)
    m1 = Monster(4, 100)
    
    
    # testing section for attacks
    try:
        print("\nBEFORE:\n")
        
        print("Hero's Health: ", h1.get_HP())
        print("Monster's Health: ", m1.get_HP())
        
        h1.attack(m1)
        
        print("\nAFTER:\n")
        
        print("Hero's Health: ", h1.get_HP())
        print("Monster's Health: ", m1.get_HP())
    except:
        print("Error(s) occurred")

# calling the main-func
main()