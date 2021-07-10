import random
class Story():
    def __init__(self, friend, foe):
        self.friend = friend
        self.foe = foe
        self.scenario = (random.randint(3,4) * random.randint(1,2)) % 2
        if self.scenario == 0:
            self.character = friend
        else:
            self.character = foe

newStory = Story("bob","janice")
print(newStory.foe)
print(newStory.friend)
print(newStory.scenario)
print(newStory.character)
