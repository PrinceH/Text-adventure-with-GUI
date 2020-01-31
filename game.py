from tkinter import*
import time
import enemies, player, items
import winsound



"""reed = items.Reed_Trident()
print(reed)


print("You are a coward.") 
coward = player.Player()
#print(coward.check_glory())
coward.add_glory(5)
print(coward.check_glory())

gnome = enemies.Gnome()
print(gnome.hp)

"""


def music():
    winsound.PlaySound("C:/Users/Princeton/Downloads/battle.wav", winsound.SND_ASYNC)
def main():
    save_code()
  
def end():
    exit()
    return None


def intro():
    global name
    name = str(input("What is your name?"))
    print("The king looks at you worriedly. Despite his power, something is troubling him. He quickly walks toward you.")
    time.sleep(1)
    print("'{}, you are one of my most trusted knights. You have served the kingdom well.".format(name))
    time.sleep(1)
    print("{} you will have a hard journey ahead of you. My daugther is sick with an unknown illness.".format(name))
    time.sleep(1)
    print("It will be up to you to save her from this disease. \nDo you accept?' ")
    time.sleep(1)
    brave_warrior()
    time.sleep(1)
    print("You should rest tonight. Go home with your family.")
    day_two()


def brave_warrior():
    ans = input("Yes or No")
    time.sleep(1)
    if ans.startswith("y" or ans.startswith("Y")):
        print("Continue on brave warrior.")
        time.sleep(2)
        print("I will have my servants pack your bag.")
        open_inventory()
    elif ans.startswith("n" or ans.startswith("N")):
        print("You are a coward.") 
        coward = player.Player()
        print(coward.check_glory())
    else:
        brave_warrior()


def open_inventory():
    check_bag = input("Press 'i' to see your inventory.")
    print("...")
    time.sleep(2)
    if check_bag.startswith("i"):
        inventory = player.Player()
        print(inventory.print_inventory()) 

def save_code():
    code = input("What is your save code? \nIf none type 'none'.")
    if code ==  4031 or code == "4031":
        day_two()
    elif code == "5031":
        pass
        #third choice
    elif code == "5640":
        pass
        #fourth choice
    elif code == "none":
        music()
        #print(winsound.SND_NOWAIT)
        time.sleep(1)
        intro()

def day_two():
    for i in range(2):
        print(".",'\n')
    print("End of Day 1.\nSave Code:4031.")
    inventory = player.Player()
    print(inventory.print_inventory())  

intro()

