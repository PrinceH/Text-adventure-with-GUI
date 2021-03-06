import items


class Player():
    #inventory = [items.Apple(7), items.Bread(4),items.Water(5),items.Sword()]
    def __init__(self):
        self.inventory = [items.Apple(5), items.Bread(2),items.Water(3),items.Sword()]
        self.hp = 100
        self.stamina = 50
        self.glory = 0
        self.glory_statement = "=======================\nYou failed. History will forget you"
        """
    #Keep this for game without gui   
    def print_inventory(self):
        for item in self.inventory:
            print (item,'\n')

         """
    #Does not work. 
    def update_inventory(self,Apple_amt,Bread_amt,Water_amt):
        self.inventory = [items.Apple(Apple_amt),items.Bread(Bread_amt),items.Water(Water_amt),items.Sword()]
        
    #prints formatted player stats to the gui output box when creating an instance variable    
    def __str__(self):
        return "HP: {} \nStamina: {} \nGlory: {}".format(self.hp,self.stamina,self.glory)

    def add_hp(self,amt):
        #self.amt = amt
        self.hp += amt

    def add_stamina(self,amt):
        #self.amt = amt
        self.stamina += amt

    def add_glory(self,amt):
        #self.amt = amt
        self.glory += amt

    def check_glory(self):
        if self.glory>10:
            self.glory_statement = ("=======================\nYou are a mighty warrior. You will be remembered for saving the King's daughter.")
        elif self.glory>=5:
            self.glory_statement = ("=======================\nYou came far, though you didn't succeed. Your efforts will encourage future warriors..")

    def reset_stats(self):
        self.inventory = [items.Apple(5), items.Bread(2),items.Water(3),items.Sword()]
        self.hp = 100
        self.stamina = 50
        self.glory = 0
        self.glory_statement = "=======================\nYou failed. History will forget you"
