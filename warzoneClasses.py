#python3

'''
A Complete Set Of Things Needed For A Shooter
Maybe I Will Implement This Into A Text-Based Adventure Game

Checklist:

    Players:
        #Soldier XY
        #Enemy XY
        Dog X
    Weapons:
        Primary XY
            All The Guns X
        Secondary XY
            All The Guns X
    Throwables:
        #FlashBang XY
    Loadouts:
        #Names XY
        #Primary XY
        #Secondary XY
        Perks X
        Lethal X
        #Tactical XY

'''

# Imports

# Vars
x = None # placeholder for incomplete stuff

# Classes

## The Soldier or Player (AKA Our Side)
class Soldier:
    def __init__(self, name, clothing, loadout):
        self.name = name
        self.clothing = clothing
        self.loadout = loadout


## The Enemy (AKA Their Side)
class Enemy(Soldier):
    def __init__(self, name, clothing, loadout, fraction):
        super().__init__(name, clothing, loadout)
        self.fraction = fraction



    
## The Weapn Class - Parent of All Weapons
class Weapon:
    def __init__(self, name, description, equipped, stats):
        self.name = name
        self.description = description
        self.equipped = equipped
        self.stats = stats
    
    def shoot(self): # shoot
        print("shoot")
    
    def reload(self): # reload
        print("reload")

## The Primary Weapon - Main Weapon of Players
class Primary(Weapon): 
    def __init__(self, name, description, equipped, stats, category):
        super().__init__(name, description, equipped, stats)
        self.category = category
    
    def shoot(self): #shoot
        for _ in range(3):
            print("shoot")


## The Secondary Weapon - Sidearm of Players
class Secondary(Primary):
    def __init__(self, name, description, equipped, stats, category):
        super().__init__(name, description, equipped, stats, category)




## Throwables - Gadgets or Grenades To Be Thrown
class Throwable(Weapon):
    def __init__(self, name, description, equipped, stats, effect):
        super().__init__(name, description, equipped, stats)
        self.effect = effect
    
    def blowUp(self): # blow up
        print("BOOM")






## The Loadout - Inventory Carried by Players
class Loadout:
    def __init__(self, number, name, primary, secondary, perks, lethal, tactical):
        self.number = number
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.perks = perks
        self.lethal = lethal
        self.tactical = tactical
    
    def get_ldout(self): # get name of loadout
        return self.name
        



# Funcs
def space(): # Clean Up the Shell-Output
    for _ in range(1):
        print("")



#Main-Loop


### CREATE Instances of the Classes
        
## Weapons
M4A1 = Primary("M4A1", "A fully automatic, all-purpose assault rifle.", False, 80, "Assault Rilfe")
M9 = Secondary("M9", "A small reliable Pistol", False, 60, "Pistol")
Flashbang = Throwable("Flashbang", "Small blinding device", False, 100, "Blinds Enemies")

## Loadout
ldout1 = Loadout(1, "Custom Loadout 1", M4A1, M9, x, x, Flashbang)


## Soldier
s1 = Soldier("Joe", "Uniform", ldout1)



# Do Stuff (Basically Play The Game)
print(s1.loadout.get_ldout()) # HOLY SHIT!!! THIS ACTUALLY WORKS!!! :D
space()
s1.loadout.primary.shoot() # OMG....


