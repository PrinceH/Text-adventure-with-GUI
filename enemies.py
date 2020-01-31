
class Enemy:
    #A base class for all enemies
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        if self.hp > 0:
            return True
        elif self.hp == 0:
            return False
    #will print the formatted name, description, hp, and damage to the outbox when used in game_gui
    def __str__(self):
        return "Name: {}\nDescription: {}\nHP: {} \nDamage: {}".format(self.name, self.description, self.hp, self.damage)

class Gnome(Enemy):
    def __init__(self):
        super().__init__(name="Gnome", description ="A small dwarfish enemy who normally lives in the ground. ",hp=45,damage=10)

class Stronger_Gnome(Enemy):
    def __init__(self):
        super().__init__(name="Large Gnome", description="A big burly gnome. This enemy is larger than normal dwarves.", hp=60, damage=20)


class Nymph(Enemy):
    def __init__(self):
        super().__init__(name="Nymph",description="Normally peaceful nature spirits who protect the forest.", hp=40,damage=25)

class Treant(Enemy):
    def __init__(self):
        super().__init__(name="Treant",description="A tree looking creature. Though tall, it looks weak.",hp=100,damage=15)
        