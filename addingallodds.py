import math

def test(target, totalsum=0):
    if target > 0:
        while target >= 0:
            if target % 2 != 0:
                totalsum += target
            target -= 1

    elif target <= 0:
        while target <= 0:
            if target % 2 != 0:
                totalsum += target
            target += 1

    return totalsum

def main():
    target = float(raw_input("Insert a number: "))
    test(target)

main()
