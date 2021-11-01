import random
class Story():
    def __init__(self, character):
        self.character = character
        self.scenario = (random.randint(3,4) * 12345 * random.randint(1,2)) % 2
        self.scenario += ((random.randint(3,4) * 12345 * random.randint(1,2)) % 2)
        if self.scenario == 0:
            self.character.friend = True
        else:
            self.character.friend = False
    def fetchFriendStatus(self):
        return self.character.friend

##newStory = Story("bob","janice")
##print(newStory.foe)
##print(newStory.friend)
##print(newStory.scenario)
##print(newStory.character)

#ToDo:
#  

class Character():
    def __init__(self, name, intro, evil, good,
                 q_and_a):
        self.name = name
        self.intro = intro
        self.friend = False
        self.q_and_a = q_and_a #question being q_and_a[num][0] and answer being q_and_a[num][1]
        # limit the number of allowed questions to half the total
        self.evil = evil
        self.good = good
        self.answer_countdown = round(len(self.q_and_a.keys())/2)
        self.asked = []
        
    def __repr__(self):
        return self.name
    def get_intro(self):
        return self.intro
    def get_question(self, numKey):
        return self.q_and_a[numKey][0]
    def trust(self):
        if self.friend == True:
            return self.good['win']
        if self.friend == False:
            return self.evil['lose']
    def distrust(self):
        if self.friend == True:
            return self.good['lose']
        if self.friend == False:
            return self.evil['win']
    def get_answer(self, numKey):
        if numKey not in self.asked and numKey in self.q_and_a.keys():
            self.asked.append(numKey)
            return str(self.q_and_a[numKey][1])
        else:
            return "I'm sorry. I don't think they understood that."
            


 #syntax about good
 # good = {'win': "", lose:""}   

#test the class using an instance
##bastian = Character('Big Friendly Python'
##,False
##, {'win': "You run away right before the 'friendly' python bytes you. You win, I guess...", 'lose':'You were swallowed by the snake....'}
##, {'win': 'You just received a new friend! With big snake hugs! The python protects you from the jaguar onslaught', 'lose': 'You run away and trip over a branch... you were eaten by pirhanas'}
##, {1:["What is your name?","Big Friendly Python Junior Esquire 3rd"], 2:["What is your quest?","To do friendly stuff and help you in this game."],3:["What is your favorite color?","Blue-No! Wait!"], 4:["Is this a question?","Yes, it is indeed"],5:["Is this also a question?","Yep......"], 6:["I like turtles.","What?"]})
##
##newStory = Story(bastian)
##print(newStory.fetchFriendStatus())
##print(newStory.character)
##print(newStory.character.trust())
##print(bastian)
##bastian.friend = True
##print(bastian.answer_countdown)
##print(bastian.get_question(1))
##print(bastian.get_answer(1))
##print(bastian.distrust())
##print(bastian.trust())
