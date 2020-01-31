import time

glory = 0
health = 100
value = []
inventory = ["Apple","Lantern","Knife"]
equipped = []

def main():
    intro()
    next_move()

def end():
    exit()
    return None



def glory_status():
    if glory <=0:
        print("Your journey achieved nothing. You were forgotten in history. Please try again.")
    elif glory<=5:
        print()
      
"""Intro"""
def intro():
    global player
    player = input("Who dares enter the dragons castle?")
    print(player + ", are you ready for peril?")
    ask_player = input("Yes(1) or No(2)?")
    ask_player = int(ask_player)
    if ask_player<=1:
        time.sleep(2)
        print("Then prepare for your journey")
        next_move()
    else:
        print("Goodbye")
    

        

"""Wait, Hide, or Run"""
def next_move():
    time.sleep(2)
    print("Day 1")
    print("So " + player + " this is your story. It was a dark night in the middle of the forest when you wandered in.")
    time.sleep(2)
    print("You were eager to claim riches; dragons are known for hoarding treasure. You were unsuspecting, naive, full of greed.")
    time.sleep(2)
    print("The forest was humming with nightlife. All of a sudden, you see a bright flash and hear a roar.")
    time.sleep(2)
    print("You should have at least 10 miles before you enter the dragons territory.")
    time.sleep(2)
    print("Is it possible that the dragon flew nearby and heard you?")
    player_r = int(input("What do you do?: wait(1), hide(2) or run(3) "))
    if player_r == 1:
        print("You see a large cave nearby Without packing your supplies, you hurriedly run in the large carvern.")
        print("You stay near the front. You have a lantern,but you don't want to attract unwanted attention.")
        print("You wait a few minutes.The minutes feel like days.As you sit and wait for the danger to pass, you accidently drift to sleep.")
        move_three()

    elif player_r == 2:
                        print("Some journeys aren't meant for cowards. You quickly pack your supplies and begin hiking out of the forest.")
                        scared_player = input("Is this where you want your journey to end? Yes(1) or No(2)")
                        if scared_player ==  "yes":
                                                    print("Okay. Your journey has concluded. You survive, but don't gain any honor or money")
                                                    end()
                        elif scared_player =="no":
                                                    print("You calm yourself down. You control your nerves. You command yourself to continue")
                                                    move_three()

    elif player_r == 3:
        print("You stay as still as possible, glued in place by fear. Seconds seem like hours.")
        print("As you stand your leg begins to cramp. You ignore it as best as you can. You listen intently. \n Nothing \n You lay down and try to rest. ")
        move_three()
    
"""Choices, choices... """
def move_three():
    print("Day 2")
    print("You wake up and stretch your legs. Yesterday frightened you, but you're determined")
    print("")
    

def play_again():
    again = input("Do you want to play again?")
    if again == "yes" or "y:":
        main()
    else:
        end()

#Each choice will be a function so it cn be repeated if the user presses the wrong character
main()
