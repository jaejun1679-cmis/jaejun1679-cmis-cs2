#The game will give the user the illusion of choice. Similar to the game by the name "The Stanley Parable", there will be a narrator which I will code. Primarily #using the raw_input function, it will ask the user to type something. If they obey, the story will continue. If they disobey, the story will change.
#My program allow the user to control a character named "Bob". Bob is trying to go to work and it is the user's responsibility to make sure he showers, eats breakfast, wears proper clothing, and get the correct briefcase.  
import random
import math
import time

def intro():

	print """
Hello! Welcome to my conditionals assignment. Uh I mean my game about things that does things when you input things into this grey thing. 
The objective is to help Bob get ready for work. Bob is a very busy man and must be on time. But before he goes to work, he does a lot things. He needs to wake up, take a shower, eat breakfast, wear a suit, and start his car. What a poor busy man. 

Before you begin, take account this quote: 
"Choose is to make a choice, and a choice is to choose" - JJC
Made no sense but thy shall not judge the ones who try. 
"""
	raw_input("Press enter to begin. \n")

def counttoten():
    time.sleep(1)
    print 1
    time.sleep(1)
    print 2 
    time.sleep(1)
    print 3
    time.sleep(1)
    print 4 
    time.sleep(1)
    print 5 
    time.sleep(1)
    print 6
    time.sleep(1)
    print 7 
    time.sleep(1)
    print 8
    time.sleep(1)
    print 9
    time.sleep(1)
    print 10 

def inttest():
    print """HI! Welcome to the testing center. Hopefully you've had enough sleep because this test is much more complicated than the SAT test. The answers are totally not randomly rigged to fit the 11th requirement on this list: (https://sites.google.com/a/cmis.ac.th/cs2/unit-3/conditional-execution). The "x" represents completion.

Write a description of what your script will do first. This description can be written in gedit and used as the basis of your code later. See this example.
name the file conditionals.py
- 2 conditional execution x
- 2 alternative execution x
- 2 chained conditionals x
- Use raw_input. x
- Use good variable names. x
- Use type conversion when necessary. x
- Define at least 4 functions that do something substantial (not just adding 2 numbers or multiplying). At least 1 must return a boolean value and be used as a part of the flow control. At      least one must return an integer or float. At least 1 must return a string. The 4th can do what ever you want. x
- Define a main() function to organize the flow of your program. Be sure to think about the three phases (input, processing, output) x
- Use at least 3 different relational operators. x 
- Use each of the logical operators at least once. x
- Use random.random() and random.randint() at least once each in your script.
- Use str.format() at least once in your script. x
- Use \"\"\" or \'\'\' strings at least once in your script. x
- Write an interesting and/or entertaining story/game. x 
- Use the same structure we learned about in the simple program assignment. x """

#add the box back

def wakeup():

    answer1 = raw_input("Bob needs to go to work, but should he wake up? (yes or no) ")
    
    if  answer1 == "yes":
        print "\nUgh I hate to admit it, but yes. Bob must wake up so that he can go to work.\n"
        time.sleep(1)

    elif answer1 == "no":
        print "IKR. People should never wake up form their eternal slumber. But come on mate, Bob needs to go to work.\n"
        exit()

    else: 
        print """It clearly says to type "yes" or "no" you retard...\n"""
        time.sleep(1)
        wakeup()

def takeshower():

    answer2 = raw_input("Tadaaa now Bob woke up. But Bob smells very very bad. Should Bob take a shower? (yes or no) ")
    
    if  answer2 == "yes":
        print "\nNICE. Taking a shower is always great. You get to wash thyself whilst singing or rapping your most beloved song. And by the end of your rock concert, you are very clean.\n"
    
    elif answer2 == "no":
        print """\nAlright you dirty person, listen up. He is stinky. I just said that "Bob is very bad smell." *translating into language a retard can understand...*"""
        time.sleep(5)
        print """\nNi Hao!"""
        time.sleep(1)
        print """\nHmmm ironic. Let's say im getting lazy. 01100010 01111001 01100101. (http://binarytranslator.com)\n"""
        exit()

    else: 
        print """\nAre you in the umost okay condition right now? Like I mentioned before, please type "yes" OR "no". Okay we will count to ten and then continue.\n"""
        counttoten()
        takeshower()

def eatbreakfast():

    answer3 = raw_input("Eat breakfast? Now how about that. It really doesn't matter when you eat but eh. So...eat? (yes or no) ")
    
    if  answer3 == "yes":
        print "\nNO. HE MUST NOT EAT AT HOME, for money management purposes. If he goes to his office, there must be be free food. You know that place where there is a small fridge and it is like a lounge. FREE FOOD. TAKE FREE FOOD ANYWHERE YOU GO. \n"
        exit()
    
    elif answer3 == "no":
        print """Yas. For reasons along the line of "Be cheap in order to save money" he must not eat at home but eat the free food provided the office place he works at. Ohhh maybe he works for Google or something. (idk lel) \n"""

    else: 
        print """ Okay now. I'm done with you incapacities to type "yes" or "no". You GPA must be below 2.5. bye. \n"""
        exit()

def wearsuit(trynum=0):

    answer4 = raw_input("All if not most classy men and bussiness workers, they must (men and women; I'm not sexist) wear suits (or maybe that's just some social schema one must conform to). At hand, YOU know Bob works in an office and he is getting ready for work. So now u tell me, SHOULD he wear a suit? Hint: The answer is yes. (yes or no)\n")

    if answer4 == "yes":
        print "NICE. At least you know how business men dress to work. Now Bob is wearing a suit and tie~\n"

    if trynum == 1:
        print "TRY AGAIN YOU RETARD\n"
        trynum = trynum + 1
        wearsuit(trynum)

    elif trynum == 2:
        print "yoyoyoyoyo\n"
        trynum = trynum + 1
        wearsuit(trynum)

    elif trynum == 3:
        print """
Here. Please read about Hitler talking about youth. 

My German Youth, after a year's time, I can now greet you here again!

Since then, enormous events have taken place in Germany. Already twelve months ago, the battle for power has granted us success. In the meantime, our movement-of which you are the young guards today and future bearers-has taken hold of one position after another in our country and bestowed it to the German people. At the same time, your movement has grown from an already large union to the largest youth organization in the world. This is the result of numerous contributors whose leader I assigned to you, party comrade, Mr. Schirach.In this vast arena here today, you are a part of what people stand for in this country. You must now take on and learn in your youth what we want to see take shape in all of Germany. We know that nothing is handed to a people but everything must be fought for and conquered. There is nothing one can be a master of that one has not first learned and instilled into oneself. And so now, we want that you, German boys and German girls, take up all that we have hope for in you and our country-what we want to see fulfilled in Germany. We want to be ONE nation, and you my youth, you shall now become this nation. We do not want to see class and status differences anymore, and so you must not allow yourselves to nurture attitudes that promote them. We want to see ONE Reich, and you must already now train yourselves for this in ONE organization. We want our folk to be loyal, and you must learn this loyalty. We want our people to be obedient, and you must practice obedience. We want our folk to be peace loving, but also brave. You must always be ready for peace and at the same time courageous. We do not want our people to be weaklings but that they can be tough in order to withstand the difficulties of life. And you must already train yourselves for this in your youth. We want our people to love honor again, und you must declare yourselves to the principle of honor already in your youngest years. We want you to be a proud people again, and in your youth you must attain this pride; a proud people from which springs the pride of your youth and carries into the generations to come. All that we demand from the Germany of the future, we demand from you, boys and girls. This you must practice and in this contribute to the future. No matter what we create today and what we do, we will pass on one day. But in you Germany will continue. And when there will be nothing left of us, then you must bear the flag in your hand-a flag which we once raised from nothing. You must therefore stand confident on the soil of your country, and you must be strong so that this flag will never be taken from you. And then, when generation after generation comes after you, you will have the right to demand the same from them. Then you can demand from your future youth that they be like you were. And then Germany looks at you also with pride, and everyone's heart runs over with joy when we see you. And when we see in you the promise that our work is not in vain, but that it bears fruit in our country, then we are all gripped with a proud happiness to see in you the fulfillment of our work. With that we have the assurance that the Millions who died in WWI-the great numbers of our comrades-have not made the sacrifice for Germany in vain, so that in the end, out from all of it, a one-spirited, free, proud, and honor-loving people will emerge. And I know it cannot be any other way because you are flesh from our flesh and blood from our blood, and in your young minds burns the same spirit that dominates us. You cannot be any other way but be bound to us. And when the large processions of our movement march today gloriously through Germany, then we know that you will join these columns, and we know that before us lays Germany, in us marches Germany, and after us comes Germany!" - Adolf Hitler, Sept 8, 1934. 

In short, Hitler is talking about the young mind of Germany. Now the fact that you cannot type "yes" or "no" is like...sigh nvm. From now on I will talk in some form on English you will understand. \n"""
        exit()
    
    elif answer4 == "no":
        print """...................okay im getting tired. lets finish this quick. like i said, he must wear a suit to work. RUN THE CODE AGAIN.\n"""
        trynum = trynum + 1
        wearsuit(trynum)

def correctcase():

    answer5 = raw_input("Bob needs to go to work, therefore he needs his suitcase. Now, should Bob carry his suitcase to work? (yes or no) ")
    
    if  answer1 == "no":
        print "Sadly, that is correct and not correct at the same time. People use Google Docs these days. O' wothyest of programs. People need suitcases yet they have Google Docs to do everything...."
        time.sleep(2)

    elif answer1 == "yes":
        print """Hold up. I don't even know if business poeple even need suitcases anymore. HAHAHAHAH. *smoke bomb* "im outtie" \n"""
        time.sleep(2)

    else: 
        print """k."""
        time.sleep(2)
        correctcase()

def outro():
    print "Well it seems like we have reached the end of this real-life 100% replica of life-simulation game. That's it. I am FREEEEEE. Ah but before you and I partways, I must give you an intellectual evaulation due to the require of the conditionals assignment. Uh i mean uh to see if you should breed in the future. WAIT no uhh i mean to see you can uhhh........nvm run the quiz."
    inttest()

def main():
    inttest()
main()
