class Program:
    def __init__(numlist):
        numlist.numbers = []

    def insert(numlist, number):
        numlist.numbers.append(number)

    def search(numlist, x):
        if x in numlist.numbers:
            return numlist.numbers.index(x) + 1
        else:
            return -1
