import os
import sys
import Modules
import MenuArt
import time
import DeathAnimation

def clearScreen():
    if os.name.lower() == "posix":
        os.system("clear")
    else:
        os.system("cls")

def hud(topText, middleText, bottomText, divider):
    clearScreen()
    print(divider + '\n' + divider)
    print(topText)
    if middleText != '':
        print(divider + '\n' + divider)
        print(middleText)
    print(divider + '\n' + divider)
    print(bottomText)
    print(divider + '\n' + divider)

def questionMenu(character):
    stringConcat = ''
    for item in character.q_and_a.keys():
            if item not in character.asked:
                stringConcat += str(item) + '. ' + character.get_question(item) + '\n'
    return stringConcat
    
def main():
    divider = '------------------------------------------------------------'

    # start screen animation
    animation = [MenuArt.menuArt1(), MenuArt.menuArt2(), MenuArt.menuArt3(), MenuArt.menuArt4()]
    for frame in animation:
        time.sleep(0.5)
        clearScreen()
        print(frame)
    for frame in animation[-2::-1]:
        time.sleep(0.5)
        clearScreen()
        print(frame)

    #prompt user to start
    print("Want to Start?")
    startOrQuit = str(input('Press "Y" to Begin or Other Keys to Quit: '))
    if startOrQuit.upper() == "Y":

    #   create character object
        clearScreen()
        bastian = Modules.Character('Big Friendly Python', '''For some reason, you are hiking in a jungle and hear
"Hi! I am a model character to test the game\'s story system!
I am also a friendly python thing!
It\'s not safe here, so you\'ll have to come with me."'''
, {'win': "You run away right before the 'friendly' python bites you. You win, I guess...", 'lose':'You were swallowed by the snake....'}
, {'win': 'You just received a new friend! With big snake hugs! The python protects you from the jaguar onslaught', 'lose': 'You run away and trip over a branch... you were eaten by pirhanas'}
, {1:["What is your name?","Big Friendly Python Junior Esquire 3rd"], 2:["What is your quest?","To do friendly stuff and help you in this game."],3:["What is your favorite color?","Blue-No! Wait!"], 4:["Is this a question?","Yes, it is indeed"],5:["Is this also a question?","Yep......"], 6:["I like turtles.","What?"]})

        story = Modules.Story(bastian)
    ##  Create introduction and grab initial question as input
        print(divider)
        input('\n\n' + bastian.get_intro() + '\n\n' + divider + '\nPress Enter to Continue')
        clearScreen()
        questionNum = int(len(bastian.q_and_a) / 2)
        hud("""You might want to ask this character a few questions first. \nYou just met them, after all.""","You only have time to ask " + str(questionNum) + " questions. Ask wisely!",questionMenu(bastian), divider)
        theQuestion = int(input("Choose the number key for the question you want to ask, then press Enter: "))
        questionNum -= 1
        while questionNum > 0:
            hud(bastian.get_answer(theQuestion),"You only have time to ask " + str(questionNum) + " questions. Ask wisely!",questionMenu(bastian), divider)
            theQuestion = int(input("Choose the number key for the question you want to ask, then press Enter: "))
            questionNum -= 1
        hud(bastian.get_answer(theQuestion), str(bastian) + " is urging you to trust them. Do you?", "Y - Yes \nN - No", divider)
    else:
        sys.exit("Have a good one!")

main()
