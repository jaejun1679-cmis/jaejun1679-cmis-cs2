import time

def find(start, end):
    if start > end:
        countdownfrom(start, end)
    elif end > start: 
        countupfrom(start, end)

def countdownfrom(start, end):
    if start == end:
        print "We made it to " + str(end) + "!"
    else:
        time.sleep(1)
        print start - end
        countdownfrom((start + 1), end)

def countupfrom(start, end):
    if start == end:
        print "We made it to " + str(start) + "!"
    else:
        time.sleep(1)
        print end - start
        countdownfrom((start - 1), end)

def main():
    start = float(raw_input("Insert the starting number: "))
    end = float(raw_input("Insert the ending number: "))
    find(start, end)

main()
