from secrets import choice
import time #Make me be able to pause the text 

#Possible answers player can give 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, or C\n")

#item pool (use if Item > 0: else:)
Sword = 0 
Key = 0
lnote = 0
Family_spoon = 0

#Game over

def option_gameover():
    print("\nYou have died!")
    time.sleep(1.5)
    print("\n\nGAME OVER!")
    time.sleep(10)
    
#story intro 

def intro():
    print("\nThe last memory you have is fighting hand to hand with an Orc. He bested you in combat and you blacked out."     
    "\nThinking this is the end, you've accepted your fate but as luck will have it, this was not your time to fall.."     
    "\nYou wake up in a room that you do not recognize, you look around to see what you can learn.."     
    "\nYou see a chest in the corner of the room. It looks to be the only thing of value, there is also a door leading outside..")
    
    time.sleep(1)

    print ("\nA. Go see whats in the chest" 
    "\nB. Go open the door and walk outside ignoring the chest")

    #this allows you to pick a choice
   
    choice = input(">>> ")
    if choice in answer_A:
        option_chest()
    elif choice in answer_B:
        option_door()
def option_chest(): #this opens the chest then forces you to select option B to get into the world
    print("You walk over the the old chest and open it to find a sword, do you take it? yes/no") 
    choice = input(">>> ")
    if choice in yes:
        Sword = 1 #this adds item to the char
    print("You take the sword and put it on your side")
    if choice in no:
        print("You close th chest and leave the sword behind") 
    time.sleep(1)      
    print("You now walk through the door") 
    time.sleep(1)
    option_door()
def option_door():
    print("\nYou open the door and walk you to a unfamiliar village,")
    time.sleep(.8)
    print("\nTo the East is a vast mountain range") #make this high level thing path will lead to death
    time.sleep(.8)
    print("\nTo the West there is a tavern") #tavern maid that will let you talk to her and get a quest to get liberry key
    time.sleep(.8)
    print("\nTo the North there is a path leading into the forest") #the path to the next stage *Needs Sword*
    time.sleep(.8)
    print("\nTo the South there is a library") #door is locked Needs Key item

    time.sleep(1)

    print("\nWhere would you like to go")

    #this is the 1st major choice in the game to see what the player does

    print("\n A. Head East"
    "\n B. Head West"
    "\n C. Head North"
    "\n D. Head South")
    choice = input(">>> ")
    if choice in answer_A:
        option_east()
    elif choice in answer_B:
        option_west()
    elif choice in answer_C:
        option_north()
    elif choice in answer_D:
        option_south() 

def option_east(): #EAST normal game over and alt ending 
    print("You head off the the moutain range you walk for many miles only to be met by a dragon... What do you do?")
    time.sleep(1)
    print("\nA. Run"
    "\nB. Accept your fate")
    choice = input(">>> ")
    if choice in answer_A:
        option_dragonending()
    elif choice in answer_B:
        option_gameover()
def option_dragonending():
    print("You try to run but it's no use the dragon swoops down a eats you...")
    time.sleep(1.5)
    print("\n GAME OVER!") 
    time.sleep(10)

def option_west(): #WEST
    print("You head to the West towrds a tavern, Do you wish to enter? Yes/No")
    choice = input(">>> ")
    if choice in yes:
        option_tavern()
    elif choice in no:
        option_turnback()

def option_turnback():
    print("\nYou really walked all the way over here for nothing...")
    time.sleep(.8)
    print("\nyou turn back ") 
    time.sleep(.8)
    print("\nTo the East is a vast mountain range") 
    time.sleep(.8)
    print("\nTo the West there is a tavern") 
    time.sleep(.8)
    print("\nTo the North there is a path leading into the forest") 
    time.sleep(.8)
    print("\nTo the South there is a library") 

    time.sleep(1)

    print("\nWhere would you like to go") 

    print("\n A. Head East"
    "\n B. Head West"
    "\n C. Head North"
     "\n D. Head South")
    choice = input(">>> ")
    if choice in answer_A:
        option_east()
    elif choice in answer_B:
         option_west()
    elif choice in answer_C:
        option_north()
    elif choice in answer_D:
        option_south()

def option_turnback2():
    print("\nYou walk back to the center of the village")
    time.sleep(.8)
    print("\nTo the East is a vast mountain range") 
    time.sleep(.8)
    print("\nWalk to Thomas' house") 
    time.sleep(.8)
    print("\nTo the North there is a path leading into the forest") 
    time.sleep(.8)
    print("\nTo the South there is a library")

    time.sleep(1)

    print("\nWhere would you like to go") 

    print("\n A. Head East"
    "\n B. Head to Thomas"
    "\n C. Head North"
    "\n D. Head South")
    choice = input(">>> ")
    if choice in answer_A:
        option_east()
    elif choice in answer_B:
        option_thomas()
    elif choice in answer_C:
        option_north()
    elif choice in answer_D:
        option_south()

def option_tavern(): #Tavern Maid interactions 
    print("You walk in and it's a old medieval style tavern, you walk uop to the bar and see a tavern maid. What do you do?")
    time.sleep(1)
    print("\nA. Talk to her"
    "\nB. Leave the tavern")
    choice = input(">>> ")
    if choice in answer_A:
        option_maidtalk()
    elif choice in answer_B:
        if lnote > 0:
            option_turnback2()
        else:
            option_turnback()  
def option_maidtalk(): #Tavern Maid dialog 
    print("Hello, Names Matilda. How can I help?")
    time.sleep(1)
    print("\nA. What is this place?"
    "\nB. Quest?"
    "\nC. Walk away and leave.")
    choice = input(">>> ")
    if choice in answer_A:
        option_villagelore()
    elif choice in answer_B:
        option_keyquest()
    elif choice in answer_C:
        if lnote > 0:
            option_turnback2()
        else:
            option_turnback()  
def option_villagelore(): #Lore of the village
    print("Well this here is my tavern its been in the family for 3 generations, this village has been around for over 200 year!"
    "\nThe Villages name is Duncaster located 50 miles north of the capital of Garngalor"
    "\nWe dont really get much vistors in here its nice to see a new face! Is there anything else i can help you with?")
    time.sleep(1)
    print("\nA. What is this place?"
    "\nB. Quest?"
    "\nC. Walk away and leave.")
    choice = input(">>> ")
    if choice in answer_A:
        option_villagelore()
    elif choice in answer_B:
        if Family_spoon > 0:
            option_keyquest()
        else:
            option_givekey()
    elif choice in answer_C:
        if lnote > 0:
            option_turnback2()
        else:
            option_turnback()  
def option_keyquest(): #Quest options
    print("\nPlayer 'Got any work I can do to make some gold'")
    print("\nUnfortunately i dont have any gold to offer you, however I have a note that needs to be delivered to Thomas.")
    print("\nhe lives in the hobble closest to the river. Could you do this for me? I have something i can give you for your work.")
    time.sleep(1)
    print("Do you accept? Yes/No")
    choice = input(">>> ")
    if choice in yes:
        option_note()
    else:
        option_declinenote()
def option_note():
    lnote = 1
    print("\nItem added Note!")
    time.sleep(.8)
    print("\nMatilda 'Thank you! come back once you have given Thomas the note!'")
    time.sleep(.8)
    print("\nWhat do you do now?")
    time.sleep(1)
    print("\nA. What is this place?"
    "\nB. Quest?"
    "\nC. Walk away and leave.")
    choice = input(">>> ")
    if choice in answer_A:
        option_villagelore()
    elif choice in answer_B:
        option_keyquest()
    elif choice in answer_C:
        if lnote > 0:
            option_turnback2()
        else:
            option_turnback()    
def option_declinenote():
    print("\n...")
    time.sleep(1)
    print("\nWell If you change your mind you can come back and ask...")
    time.sleep(.8)
    print("WHat do you do now?")
    time.sleep(.8)
    print("\nA. Talk to her"
    "\nB. Leave the tavern")
    choice = input(">>> ")
    if choice in answer_A:
        option_maidtalk()
    elif choice in answer_B:
        if lnote > 0:
            option_turnback2()
        else:
            option_turnback()  

#Quest for thomas for the key to the library

def option_thomas():
    print("\nYou walk for a few minutes and you see a tatered shack."
    "\nIt has brown outer walls with a roof made of hay and mud, there is one window on the side of the home."
    "\nYou walk up closer unaware of who you're about to meet"
    "\nYou walk up the the door and knock...")
    time.sleep(1)
    print("\nA man no older then 26 open the door hes tall and in shape, he also has a scar that runs from his ear to his cheek")
    time.sleep(.8)
    print("What do you say?")
    time.sleep(1)
    print("A.Ummm, Nice house you got here.."
    "\nB. Sooo, Who exactly are you?"
    "\nC. I have this note that Matilda asked me to give you."
    "\nD. What are you doing living out here all alone so far from the rest of the village?")
    choice = input(">>> ")
    if choice in answer_A:
        option_house()
    elif choice in answer_B:
        option_thomaslore()
    elif choice in answer_C:
        option_note2() #exchage the lnote for family spoon -- this will then give the key when back at the tavern
    elif choice in answer_D:
        option_thomaslore2()
    
    

intro()        
