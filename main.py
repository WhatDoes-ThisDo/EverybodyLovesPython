import os
import sys
import Modules
import MenuArt

print(MenuArt.menuArt())
print("Want to Start?")
startOrQuit = str(input('Press "Y" to Begin or Other Keys to Quit: '))
if startOrQuit.upper() == "Y":
    bastian = Modules.Character('Big Friendly Python', '''For some reason, you are hiking in a jungle and hear
"Hi! I am a model character to test the game\'s story system! I am also a friendly python thing!
It\'s not safe here, so you\'ll have to come with me."'''
, {'win': "You run away right before the 'friendly' python bites you. You win, I guess...", 'lose':'You were swallowed by the snake....'}
, {'win': 'You just received a new friend! With big snake hugs! The python protects you from the jaguar onslaught', 'lose': 'You run away and trip over a branch... you were eaten by pirhanas'}
, {1:["What is your name?","Big Friendly Python Junior Esquire 3rd"], 2:["What is your quest?","To do friendly stuff and help you in this game."],3:["What is your favorite color?","Blue-No! Wait!"], 4:["Is this a question?","Yes, it is indeed"],5:["Is this also a question?","Yep......"], 6:["I like turtles.","What?"]})
    print(bastian.get_question(1))
    story = Modules.Story(bastian)
    print(bastian.friend)
    print(bastian.get_intro())
else:
    sys.exit("Have a good one!")
#print(bastian.get_question(1))
#print(bastian)
#print(bastian.friend)
##
##def main():
##
##    #Display main menu
##
##    #Prompt user to press space to continue
##
##    #Ask for the user's name
##
##    #Load Character and story from binaries
##
##main()
