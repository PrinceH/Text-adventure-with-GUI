import random
import time
import winsound
from tkinter import *
from tkinter import simpledialog

import enemies
import items
import player

#fight

#start varibales
# global stamina
# stamina = -5
# global hp 
# hp = -10
# global glory
# glory = 5
# global num
# num=2
# global decrease_stamina
# decrease_stamina = 0
# global stats
# stats = player.Player()
global character
character = player.Player()
global enemy
enemy = enemies.Gnome
global horse
horse = True


#Action for submit button
def click():
    global intext
    intext = txt.get()
    output.delete(0.0,END)
    #out(END," " + "\n" + intext)
    try:
        check_action()
    except:
        error = "Submit button error"
        out(error)
        
#check to see if function is in action list
global num
num = 4
def check_action():
    global num
    if num==4:
        intro_choice()
        num+=1
    elif num==5:
        meet_with_advisor()
        num+=1
    elif num==6:
        on_your_way()
        num+=1
    elif num==7:
        help_the_horse()  
        num+=1 
    elif num==8:
        into_the_forest()
        num+=1
    elif num==9:
        gnome_fight()
        num+=2
    elif num==10:
        stronger_gnome_fight()
        num+=1
    elif num==11:
       attack_or_flee()
       if num == 100:
           attack()
       elif num == 200:
           dodge()
       elif num == 300:
           flee()
    elif num == 12:
        keep_moving()
    else:
       out("Check action error")
    
        
    
#easy way to print to output
def out(string):
    output.insert(END,string)

# Input for user save code
# def start_box():
#     out("What's Your Save Code?")
#     num+=1


# #check day
# def day_check():
#     global intext
#     txt.get()
#     if intext == "4031" or intext==4031:
#         out("day 2")
#     elif intext == "5640" or intext==5640:
#         out("day 3")
#     else:
#         #game.music()
#         intro()


#start of story
def intro():
    global intext
    out("The king looks at you worriedly. Despite his power, something is troubling him. He quickly walks toward you.")
    out("'You are one of my most trusted knights. You have served the kingdom well.")
    out(" My daugther is sick with an unknown illness. It will be up to you to save her from this disease.' \nDo you accept(Yes or No)?")
    out("Enter your choice and press submit to continue.")    
    
#Will the player continue with the mission?
def intro_choice():
    if intext.startswith("y") or intext.startswith("Y"):
        out("Great. I will have my servants pack your bag.")
        out(" Meet with my general. He can give you more details.\
\n\nYou walk out of the king's chamber into the royal meeting hall.\nPress Submit to continue")
    elif intext.startswith("n") or intext.startswith("N"):
       out("Fine. I understand.")
       space()
       out(character.glory_statement)

#informs the player about the journey
def meet_with_advisor():
    out("A solemned face middle aged man greets you. \
'The nearby witches have told us that we're most likely to cure the king's daughter with a rare herb protected by a creature in the forest.\
Your task is to travel to the forest and procure this herb. It is guarded by a large wooden creatures: a Treant. \
     \n\nPress submit to continue")

#will the player feed the horse and forfeit supplies or slow travel speed and lose stamina?
def on_your_way():
    out("*You leave the castle immediately. You mount your steed and hope to make it by there soon. The dreaded forest isn't too far from\
the castle. You could make it there in couple hours on horseback. As you ride you notice your horse is slowing down. She seems tired.*\
\nDo you feed her some of your supplies or slow your travel speed?\n\nEnter 'feed' or 'speed' and press submit to continue")

#player looses supplies if 'f' or 'su'. Player looses stamina if 'sl'.
def help_the_horse():
    if intext.startswith("f") or intext.startswith("F") or intext.startswith("su"):
        #subtracts apples and water in inventory
        character.update_inventory(2,1,2)
        # global inventory
        # global inventory_instance
        # inventory[0] = items.Apple(5)
        # inventory[2] = items.Water(3)
        out("You gave your horse 2 applies and some water. It seems re-energized and lively. You can continue your journey.")
        horse = True
    elif intext.startswith("Sl") or intext.startswith("sl"):
        #decreases stamina by 5
        character.add_stamina(-5)
        horse = False
        out("You slow down. After a few minutes, your horse slows to a trot and falls. You urge her to continue, but she is exhausted.\
 You decided to walk on foot.\nStamina:45")              

def into_the_forest():
    global horse
    if horse == True:
        out("You dismount your steed and steel your nerves ready for what's to come. ")
    elif horse == False: 
        out("You walk into the forest slighly tired from your walk. You steel your nerves in preparation for what's to come.")
    out("As you walk into the forest, you hear a shrill noise. You see a blur to your right. You unsheath your sword preparing for battle.")
    enemy_check()

def enemy_check():
    #num = 9
    global enemy
    global num
    normal_enemies = [enemies.Gnome(),enemies.Stronger_Gnome(),None,None]
    enemy_num = random.randint(0,1)
    enemy = normal_enemies[enemy_num]
    space()
    if enemy.name == "Gnome":
        out("A Gnome is in your path!")
        #num+=1
    elif enemy.name == "Large Gnome":
        out("A Gnome is in your path!")
        num+=1
    else:       
        out("A bird flew past you. You had nothing to worry about.\nYou sheath your sword and carry on.")
        num+=4

def keep_moving():
    out("You keep moving")


def gnome_fight():
    out(enemy)
    space()
    out("Do you want to attack or flee?")

def stronger_gnome_fight():
    out(enemy)
    space()
    out("Do you want to attack or flee?stronk")

def attack_or_flee():
    global num
    if intext.startswith("a"):
        out("You chose to attack.")
        num = 100
    elif intext.startswith("f"):
        out("You chose to flee.")
        num = 300
    elif intext.startswith("d"):
        out("You chose to dodge.")
        num = 200

def flee():
    global num
    flee = [0,0,1,1,1]
    escape_possibility = random.randint(0,len(flee)-1)
    escape = flee[escape_possibility]
    if escape == 1:
        out("You successfully escaped.\nWhile not the most glorious move, you lived to complete your mission.")
        num+=1
    elif escape == 0:
        out("You were unable to escape.")
        attack_or_flee()

def attack():
    attack_phrases = [" You attack with your sword and ", " You lunge forward, quickly stabbing your opponent and \
"," You pierce your opponents skin and "]
    say = random.randint(0,3)
    speak = attack_phrases[say]
    out(speak)
    if items.Reed_Trident() in character.inventory:
        Sword = items.Reed_Trident()
    else:
        Sword = items.Sword()
    enemy.hp-=Sword.damage
    out("deal {} damage to the {}. It has {} hp remaining.".format(Sword.damage,enemy.name,enemy.hp))
    if enemy.is_alive() == True:
        out("\nThe {} is still alive. It rushes forward to attack.\nDo you flee, attack, or try to dodge?".format(enemy.name))
        txt.delete(1.0,END)
        attack_or_flee()
    else:
        global num
        out("You have killed the {}.".format(enemy.name))  
        num+=1
        
def dodge():
    dodge = [0,0,1,1,1]
    dodge_possibility = random.randint(0,len(dodge)-1)
    dodge = dodge[dodge_possibility]
    if dodge == 1:
        out("As the beast lunged at you, you dived to the left. You successfuly dodged.\nYou can move in for a quick counter-attack or use the extra time to flee")
        attack_or_flee()
    elif dodge == 0:
        out("As the beast lunged at you, you dived to the left.\nHowever, it anticipated this, it hit you harder than before.")
        character.add_hp(-enemy.damage)
        attack_or_flee()

#Adds extra blank space in the outbox
def space():
    for x in range(0,1):
            out("\n")

#ends battle music
def end_music():
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

#starts battle music
def music():
    winsound.PlaySound('C:\\Users\\Princeton\\Desktop\\Computer Science\\Python\\My Adventure\\resources\\battle.wav', winsound.SND_ASYNC)

#command that resets character inventory, stats, and restarts game
def restart():
    output.delete(0.0,END)
    global num
    num=2
    character.reset_stats()
    #remember to altar items.inventory, not base inventory 
    out("Press Submit to Begin")

#prints items in inventory
def print_inventory():
    for item in character.inventory:
        space()
        out(item)
        space()

#prints player stats like hp, glory, glory statement,etc
def player_stats():
    space()
    out(character)
    space()
   

#Does not work
def access_inventory():
    access = 2
    request = simpledialog.askstring("Input", "What inventory item would you like to use?", parent=window)
    if request is not None and (request.startswith("W") or request.startswith("w")):
        for i in range(access):
            character.add_hp(5)
        #decrease water varibale by 1
    elif request is not None and request.startswith("B") or request.startswith("b"):
        pass
        #decrease bread varibale by 1
    elif request is not None and request == "Apple":
        character.add_hp(5)
        #decrease apple varibale by 1
    else:
        "Item not found. Try again."



#main
window = Tk()
window.title("Game")
window.configure(background="black")



#image below title
photo = PhotoImage(file=
"C:\\Users\\Princeton\\Desktop\\Computer Science\\Python\\My Adventure\\resources\\sword.png")
Label (window, image=photo, bg="black") .pack() #.grid(row=0, column=0, sticky=W)

#another label
Label (window, text ="Enter choices below", bg="black", fg="white", font="none 12 bold").pack()

#text entry box
txt = Entry(window, width=100,bg="white") #width orignally 40
txt.pack()
#txt.grid(row=5,column=0,sticky=W)
intext = txt.get()

#scrollbar
scrollbar = Scrollbar(window) #changed from window
#scrollbar.grid(row=2,column=3, )
scrollbar.pack(side=LEFT, fill=Y)
#add submit button
Button(window,text="SUBMIT", width=6, command=click) .pack()#.grid(row=5,column=0)

#label for text entry
Label(window, text="Output",bg="black",fg="white",font="none 12 bold") .pack()#.grid(row=1, column=0, sticky=W)

#textbox
global output
output = Text(window,width=100, height=200,wrap=WORD, background="white", yscrollcommand=scrollbar.set) 
output.pack() #orignal w, 75 orignal h = 6
#output.grid(row=2,column=0,columnspan=3,sticky=W)
out("Instructions: After you type an answer. Press the submit button to continue. \
Under the 'General' tab you can find the inventory, player stats, and can restart \
the game. You can turn on/off the music in the 'Sound' tab.\n\nPress Submit To Begin")
scrollbar.config(command=output.yview)



#menu bar
menubar = Menu(window)
general = Menu(menubar,tearoff=0)
menubar.add_cascade(label="General",menu=general)
general.add_command(label="Inventory",command=print_inventory)
general.add_command(label="Use Items", command=access_inventory)
general.add_command(label="Player Stats",command=player_stats)
general.add_separator()
general.add_command(label="Restart",command=restart)
general.add_command(label="End Game",command=window.quit)


sound = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Sound",menu=sound)
sound.add_command(label="Music On",command=music)
sound.add_command(label="Music Off",command=end_music)


window.config(menu=menubar)


#run main loop
window.mainloop()
