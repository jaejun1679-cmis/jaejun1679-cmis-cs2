#The game will give the user the illusion of choice. Similar to the game by the name "The Stanley Parable", there will be a narrator which I will code. Primarily using the raw_input function, it will ask the user to type something. If they obey, the story will continue. If they disobey, the story will alter. My program allow the user to control a character named "Bob". Bob is trying to go to work and it is the user's responsibility to make sure he showers, eats breakfast, wears proper clothing, and get the correct briefcase.  
import random
import math

def intro():

	print """
Hello! Welcome to my conditionals assignment. Uh I mean my game about things that does things when you input things into this grey thing. 
The objective is to help Bob get ready for work. Bob is a very busy man and must be on time. But before he goes to work, he does a lot things. He needs to wake up, take a shower, eat breakfast, wear a suit, and start his car. What a poor busy man. 

Before you begin, take account this quote: 
"Choose is to make a choice, and a choice is to choose" - JJC
Made no sense but thy shall not judge the ones who try. 
"""

def scene1():

    answer1 = raw_input("Bob needs to go to work, but should he wake up? (yes or no) ")
    
    if  answer1 == "yes":
        print "Ugh I hate to admit it, but yes. Bob must wake up so that he can go to work.\n"
    
    elif answer1 == "no":
        print "IKR. People should never wake up form their eternal slumber. But come on mate, Bob needs to go to work.\n"
        exit()

    else: 
        print """It clearly says to type "yes" or "no" you retard...\n"""
        exit()

def scene2():

    answer2 = raw_input("Tadaaa now Bob woke up. But Bob is very bad smell. Should Bob take a shower? (yes or no) ")
    
    if  answer2 == "yes":
        print "NICE. Taking a shower is always great. You get to wash thyself whilst singing or rapping your most beloved song. And by the end of your rock concert, you are very clean.\n"
    
    elif answer2 == "no":
        print """Alright you dirty person, listen up. He is stinky. I just said that "Bob is very bad smell." *translating into retard-understandable-language...* (insert mandarin here)  Hm ironnic. But seriously he needs to take a shower you swine-like being.\n""" #come and fix the fill in the blank of mandarin
        exit()

    else: 
        print """Are you in the umost okay condition right now? Like I've mentioned, please type "yes" OR "no". Just two simple words.\n"""
        exit()

def scene3():

    answer3 = raw_input(" Eat breakfast? Now how about that. It really doesn't matter when you eat but eh. So...eat? (yes or no) ")
    
    if  answe3 == "yes":
        print "NO. HE MUST NOT EAT AT HOME, for money management purposes. If he goes to his office, there must be a (insert the food corner in offce place) \n" #do this 
        exit()
    
    elif answer3 == "no":
        print """ \n"""

    else: 
        print """ \n"""
        exit()

def scene4():

    answer4 = raw_input(" (yes or no) ")
    
    if  answe4 == "yes":
        print " \n"
    
    elif answer4 == "no":
        print """ \n"""
        exit()

    else: 
        print """ \n"""
        exit()

def scene5():

    answer5 = raw_input(" (yes or no) ")
    
    if  answe5 == "yes":
        print " \n"
    
    elif answer5 == "no":
        print """ \n"""
        exit()

    else: 
        print """ \n"""
        exit()

def main():
    intro()
    scene1()
    scene2()
    scene3()
    scene4()
    scene5()
main()
