
def output(minnum, maxnum):
	return """
I'm thinking from a number from {} to {}.
""".format(minnum, maxnum)

def main():
    minnum = raw_input("What is the minimum number?: ")
    maxnum = raw_input("What is the maximum number?: ")
    print output(minnum, maxnum)
main()
