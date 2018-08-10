from tkinter import *
import player,items,enemies
import time,winsound
num=2
#Action for submit button
def click():
    global intext
    intext = txt.get()
    output.delete(0.0,END)
    #out(END," " + "\n" + intext)
    try:
        check_action()
        global num
        num+=1
    except:
        error = "There has been an error"
        out(error)
        
#check to see if function is in action list
def check_action():
    if num==2:
        start_box()
    elif num==3:
        day_check()
    elif num==4:
        intro_choice()
    elif num==5:
        meet_with_advisor()
    elif num==6:
        on_your_way()
    elif num==7:
        help_the_horse()   
    else:
       out("Good job. You broke the game. Are you proud of yourself? \nDo you feel better?")
    
        
    
#easy way to print to output
def out(string):
    output.insert(END,string)


def start_box():
    out("What's Your Save Code?")


#check day
def day_check():
    global intext
    txt.get()
    if intext == "4031" or intext==4031:
        out("day 2")
    elif intext == "5640" or intext==5640:
        out("day 3")
    else:
        #game.music()
        intro()


#start of story
def intro():
    global intext
    out("The king looks at you worriedly. Despite his power, something is troubling him. He quickly walks toward you.")
    out("'You are one of my most trusted knights. You have served the kingdom well.")
    out(" My daugther is sick with an unknown illness. It will be up to you to save her from this disease. \nDo you accept?'")
    
    
#Will the player continue with the mission?
def intro_choice():
    if intext.startswith("y") or intext.startswith("Y"):
        out("Great. I will have my servants pack your bag.")
        out(" Meet with my general. He can give you more details.\
\n*You walk out of the king's chamber into the royal meeting hall.*")
    elif intext.startswith("n") or intext.startswith("N"):
       out("Fine. I understand.")
       coward = player.Player()
       space()
       out(coward.glory_statement)

#informs the player about the journey
def meet_with_advisor():
    out("A solemned face middle aged man greets you. \
'The nearby witches have told us that we're most likely to cure the king's daughter with a rare herb protected by a creature in the forest.\
Your task is to travel to the forest and procure this herb. It is guarded by a large wooden creatures: a Treant.")

#will the player feed the horse and forfeit supplies or slow travel speed and lose stamina?
def on_your_way():
    out("*You leave the castle immediately. You mount your steed and hope to make it by there by shortly. The dreaded forest isn't too far from\
the castle. You could make it there in couple hours on horseback. As you ride you notice your horse is slowing down. She seems tired.*\
\nDo you feed her some of your supplies or slow your travel speed?")

#player looses supplies if 'f' or 'su'. Player looses stamina if 'sl'.
def help_the_horse():
    if intext.startswith("f") or intext.startswith("F") or intext.startswith("su"):
        #inventory.inventory = [items.Apple(3), items.Bread(2),items.Water(2),items.Sword()]
        #Figure out a way to remove items from inventory and update the inventory that is printed in the output box
        out("You gave your horse 2 applies and some water. It seems re-energized and lively. You can continue your journey.")
    elif intext.startswith("sl"):
        global stat
        global stats_new
        stat = True
        stats_new = player.Player()
        stats_new.add_stamina(-5)   #Figure out how to decrease stamina and update player stats that is printed to output box
        out("You slow down. After a few minutes, your horse slows to a trot and falls. You urge her to continue, but she is exhausted.\
You decided to walk on foot.")


        

def space():
    for x in range(0,2):
            out("\n")

#ends battle music
def end_music():
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

#starts battle music
def music():
    winsound.PlaySound("C:/Users/Princeton/Downloads/battle.wav", winsound.SND_ASYNC)

#command that resets character inventory, stats, and restarts game
def restart():
    output.delete(0.0,END)
    global num
    num=2
    items = player.Player()
    #remember to altar items.inventory, not base inventory 
    out("Press Submit to Begin")

#prints items in inventory
items = player.Player()
inventory = items.inventory
def print_i():
    for item in inventory:
        space()
        out(item)
        space()

#prints player stats like hp, glory, glory statement,etc
def player_stats():
    if stat == False:
        stats = player.Player()
        space()
        out(stats)
        space()
    elif stat == True:
        space()
        out(stats_new)
        space()

#main
window = Tk()
window.title("Game")
window.configure(background="black")



#image below title
photo = PhotoImage(file="C:/Users/Princeton/Downloads/Python/My Adventure/sword.png")
Label (window, image=photo, bg="black") .grid(row=0, column=0, sticky=W)


#label for text entry
Label(window, text="\nOutput",bg="black",fg="white",font="none 12 bold") .grid(row=1, column=0, sticky=W)

#scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2,column=3)


#text entry box
txt = Entry(window, width=40,bg="white")
txt.grid(row=5,column=0,sticky=W)
intext = txt.get()

#add submit button
Button(window,text="SUBMIT", width=6, command=click) .grid(row=5,column=0)

#another label
Label (window, text ="Enter choices below", bg="black", fg="white", font="none 12 bold")  .grid(row=4, column=0, sticky=W)

#textbox
output = Text(window,width=75, height=6,wrap=WORD, background="white")
output.grid(row=2,column=0,columnspan=3,sticky=W)
out("Instructions: After you type an answer. Press the submit button to continue. \
Under the 'General' tab you can find theinventory, player stats, and can restart \
the game. You can turn on/off the music in the 'Sound' tab.\n\nPress Submit To Begin")
scrollbar.config(command=output.yview)


#menu bar
menubar = Menu(window)
general = Menu(menubar,tearoff=0)
menubar.add_cascade(label="General",menu=general)
general.add_command(label="Inventory",command=print_i)
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