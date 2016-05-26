import math

def test(target, totalsum):
    if target > 0:
        while target >= 0:
            if target % 2 != 0:
                target += totalsum
                return totalsum
            target -= 1

    elif target < 0:
        while target <= 0:
            if target % 2 != 0:
                target += totalsum
                return totalsum
            target += 1

def main():
    target = float(raw_input("Insert a number: "))
    totalsum = 0
    test(target, totalsum)

main()
