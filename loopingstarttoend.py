import time

def find(start, end):
    if start > end:
        countdownfrom(start, end)
    elif end > start: 
        countupfrom(start, end)

def countdownfrom(start, end):
    while start > end:
        print x 
        start -+ end

def countupfrom(start, end, attempt):
    while end > end:
        print x
        start += end

def main():
    start = float(raw_input("Insert the starting number: "))
    end = float(raw_input("Insert the ending number: "))
    find(start, end)

main()
