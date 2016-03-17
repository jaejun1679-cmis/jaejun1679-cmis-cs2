#The game will give the user the illusion of choice. Similar to the game by the name "The Stanley Parable", there will be a narrator which I will code. Primarily using the raw_input function, it will ask the user to type something. If they obey, the story will continue. If they disobey, the story will alter. My program allow the user to control a character named "Bob". Bob is trying to go to work and it is the user's responsibility to make sure he showers, eats breakfast, wears proper clothing, and get the correct briefcase.  
import random
import math

def intro():

	return """
Hello! Welcome to my conditionals assignment. Uh I mean my game about things that does things when you input thing into this grey thing. 
The objective is to help Bob get ready for work. Bob is a very busy man and must be on time. But before he goes to work, he does a lot things. So help this poor man. 
"""

def scene1():

	if raw_input("Bob needs to go to work, but should he wake up? ") == "Yes":
        print "Ugh I hate to admit it, but yes. Bob must wake up so that he can go to work. 
    
    else: 
        print "IKR. People should never wake up form their eternal slumber. But come on mate, Bob needs to go to work." 
        exit()


