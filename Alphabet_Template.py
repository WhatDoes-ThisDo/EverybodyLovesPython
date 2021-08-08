class English3DAlphabet:
    def __init__(self):
        #create 10x10 art of characters
        self.upperCaseLetters = {' ':['          ',
                                      '          ',
                                      '          ',
                                      '          ',
                                      '          ',
                                      '          ',
                                      '          ',
                                      '          ',
                                      '          ',
                                      '          '],

                                 'A':['    *##   ',
                                      '   *####  ',
                                      ' *##  *## ',
                                      '*##    *##',
                                      '*#########',
                                      '*#########',
                                      '*##    *##',
                                      '*##    *##',
                                      '*##    *##',
                                      '*##    *##'],
                                 
                                'B':['*#######  ',
                                     '*######## ',
                                     '*##    *##',
                                     '*##    *##',
                                     '*######## ',
                                     '*######## ',
                                     '*##    *##',
                                     '*##    *##',
                                     '*######## ',
                                     '*#######  '],
                                 
                                 'C':[' *####### ',
                                      '*#########',
                                      '*###   *##',
                                      '*##       ',
                                      '*##       ',
                                      '*##       ',
                                      '*##       ',
                                      '*###   *##',
                                      '*#########',
                                      ' *####### '],
                                 
                                  'D':['*#######  ',
                                       '*######## ',
                                       '*##    *##',
                                       '*##    *##',
                                       '*##    *##',
                                       '*##    *##',
                                       '*##    *##',
                                       '*##    *##',
                                       '*######## ',
                                       '*#######  '],}

    def printUpperLetter(self, letter):
        for row in self.upperCaseLetters[letter.upper()]:
            if row != None:
                print(row)
    def printLine(self, phrase):
        charList = []
        for character in phrase:
            if character == ' ':
                charList.append(character)
            else:
                charList.append(character.upper())
        for line in range(10):
            linestring = ''
            for char in charList:
                if self.upperCaseLetters[char][line] != None:
                    linestring += self.upperCaseLetters[char][line] + ' '
            print(linestring)
        # create list of the first line of each character in list
        # loope to print each character in the first line
        
        # go on 
            
                
            
            

    
            
testAlphabet = English3DAlphabet()
testAlphabet.printUpperLetter('A')
#testAlphabet.printUpperLetter('b')
#testAlphabet.printUpperLetter('c')
#testAlphabet.printUpperLetter('d')

testAlphabet.printLine('Bab Dca')

