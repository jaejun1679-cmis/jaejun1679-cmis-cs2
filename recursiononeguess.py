import random

def findnumber(minnum, maxnum, target):

    guessnum = float(raw_input("\nWhat do you think it is?: "))

    if target == guessnum:
        print "\nYou are CORRECT! ARE U A WIZARD?!"
        exit()

    elif guessnum > maxnum or guessnum < minnum:
        print "\nYou have exceeded the limits set by yourself."
        useranswer = raw_input("Would you like to try again? ")
        if useranswer == "yes":
            findnumber(minnum, maxnum, target)
        else:
            exit()
        exit()

    elif target > guessnum:
        print "\nThat's too low! Please try again."
        findnumber(minnum, maxnum, target)

    elif target < guessnum:
        print "\nThat's too high! Please try again."
        findnumber(minnum, maxnum, target)

def output(minnum, maxnum):
	return """
I am thinking from a number from {} to {}.
""".format(minnum, maxnum)	    

def main():
    maxnum = float(raw_input("What is the maximum number?: "))
    minnum = float(raw_input("What is the minimum number?: "))
    print output(minnum, maxnum)
    target = random.randint(minnum, maxnum)    
    findnumber(minnum, maxnum, target)
main()
