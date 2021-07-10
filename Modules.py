import random
class Story():
    def __init__(self, friend, foe):
        self.friend = friend
        self.foe = foe
        self.scenario = (random.randint(3,4) * 12345 * random.randint(1,2)) % 2
        self.scenario += ((random.randint(3,4) * 12345 * random.randint(1,2)) % 2)
        if self.scenario == 0:
            self.character = friend
        else:
            self.character = foe

##newStory = Story("bob","janice")
##print(newStory.foe)
##print(newStory.friend)
##print(newStory.scenario)
##print(newStory.character)

#ToDo:
#  

class Character():
    def __init__(self, name, alignment, aggro_range, resolve_range,
                 questions, answers):
        self.name = name
        self.alignment = alignment
        self.aggro_range = aggro_range
        self.resolve_range = resolve_range
        self.questions = questions
        self.answers = answers
        
    def __repr__(self):
        return self.name

bastian = Character('Bastian','baaayad', 5,5,'wut?','Maybe')

print(bastian)
        
        
        
