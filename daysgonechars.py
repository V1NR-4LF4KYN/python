class LivingBeing:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    

class Human(LivingBeing):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height
    
    def attack(self):
        print("attacking...")


d = Human("Bill", 26, 182)

print(d.get_name())
