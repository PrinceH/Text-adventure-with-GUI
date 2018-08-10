class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{}\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Food(Item):
    """The base class for all food"""
    def __init__(self, name, description, value, amount):
        self.amount = amount
        super().__init__(name, description, value,)

    def __str__(self):
        return "{}\n{}\nValue: {}\nAmount: {}".format(self.name, self.description, self.value, self.amount)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description,value)

    def __str__(self):
        return "{}\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                        description="A sword forged by mighty blacksmiths.",
                        value=15,
                        damage=15)


class Reed_Trident(Weapon):
    def __init__(self):
        super().__init__(name="Reed trident",
                        description="A powerful reed trident. Though it looks week, you know it packs a punch.",
                        value=20,
                        damage=20)
                        

class Apple(Food):
    def __init__(self,amt):
        self.amt = amt
        super().__init__(name= "Apple",
                        description= "A tasty reinvigorating fruit",
                        value=15,
                        amount= self.amt)

class Bread(Food):
    def __init__(self,amt):
        self.amt = amt
        super().__init__(name="Bread",
                       description="A warm loaf a bread cooked by the King's bakers.",
                       value=10,
                       amount = self.amt)

class Water(Food):
    def __init__(self,amt):
        self.amt = amt
        super().__init__(name="Water",
                       description="Water from the local stream",
                       value=5,
                       amount = self.amt)