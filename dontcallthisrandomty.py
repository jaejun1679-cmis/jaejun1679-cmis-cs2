def wearsuit(trynum):

    answer4 = raw_input("As all classy meny and bussiness workers, they must (men and women; I'm not sexist) wear suits (or maybe that's just some social schema one must conform to). At hand, YOU know Bob works in an office and he is getting ready for work. So now u tell me, SHOULD he wear a suit? Hint: The answer is yes. (yes or no)\n")

    if answer4 == "yes":
        print "NICE. At least you know how business men dress to work. Now Bob is wearing a suit and tie~\n"
    
    elif answer4 == "no":
        print """...................okay im getting tired. lets finish this quick. like i said, he must wear a suit to work.\n"""
        trynum = trynum + 1

    if trynum == 3:
        print "yoyoyoyoyo"
        
def main():
	wearsuit(0)
main()

#place "wearsuit(trynum)" somewhere else so that the program can make sure trynum == 3 and print yoyoyo instead of calling the wearsuit function again
