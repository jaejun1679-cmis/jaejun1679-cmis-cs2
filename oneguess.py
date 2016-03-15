import math
import random

def output(minnum, maxnum):
	return """
I'm thinking from a number from {} to {}.
""".format(minnum, maxnum)

def result(target, guessnum, offby):

    if target > guessnum:
        print """
The target was {}.
Your guess was {}.
That is under {} units.
""".format(target, guessnum, offby)

    elif target == guessnum:
        print """
The target was {}.
Your guess was {}. 
Therefore you are CORRECT! ARE U A WIZARD?!
""".format(target, guessnum, offby)

    else:
        print """
The target was {}.
Your guess was {}. 
That is over {} units.
""".format(target, guessnum, offby)

def main():
    minnum = float(raw_input("What is the minimum number?: "))
    maxnum = float(raw_input("What is the maximum number?: "))
    print output(minnum, maxnum)
    guessnum = float(raw_input("What do you think it is?: "))
    target = random.randint(minnum, maxnum)
    offby = abs(target - guessnum)
    result(target, guessnum, offby)
main()
