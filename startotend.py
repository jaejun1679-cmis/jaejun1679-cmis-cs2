import time

def find(start, end, attempt):
    if start > end:
        countdownfrom(start, end, attempt)
    elif end > start: 
        countupfrom(start, end, attempt)

def countdownfrom(start, end, attempt):

    if start == end:
        print "We made it to " + str(end) + "!"

    else:
        time.sleep(1)
        if attempt == 0:
            print start
        print start - 1
        attempt = attempt + 1
        countdownfrom((start - 1), end, attempt)

def countupfrom(start, end, attempt):

    if start == end:
        print "We made it to " + str(start) + "!"

    else:
        time.sleep(1)
        if attempt == 0:
            print start
        print start + 1
        attempt = attempt + 1
        countupfrom((start + 1), end, attempt)

def main():
    start = float(raw_input("Insert the starting number: "))
    end = float(raw_input("Insert the ending number: "))
    attempt = 0
    find(start, end, attempt)

main()
