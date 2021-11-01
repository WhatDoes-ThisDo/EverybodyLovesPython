import time
import os

def clearScreen():
    if os.name.lower() == "posix":
        os.system("clear")
    else:
        os.system("cls")

def deathArt1():
    frame = (
        """
               ( )         ( )  
             ( ) \         / ( )
                \ \       / /   
                 \ \     / /    
                  \_\___/_/     
                  /       \     
                 | /     \ |    
                 |  X   X  |     
                 |    ^    |     
                /|_   _   _|\    
               / / | / \ | \ \   
              / /  | |_| |  \ \  
           ( ) /    \___/    \ ( )
             ( )             ( )  
        """
        )
    return frame

def deathArt2():
    frame = (
        """




                   _______
                  /       \ 
                 |         |
                0|  O   O  |0
                 |    ^    |
                 |    _    | 
                  \       /   
                   \_____/     
                     | |           

        """
        )
    return frame

# death animation test
animation = [deathArt2(), deathArt1()]
loop = 0
while loop < 3:
    for frame in animation:
        time.sleep(0.4)
        clearScreen()
        print(frame)    
    loop += 1
