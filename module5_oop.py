class Program:
    def __init__(numlist):
        numlist.numbers = []

    def insert(numlist, number):
        numlist.numbers.append(number)

    def search(numlist, X):
        if X in numlist.numbers:
            return numlist.numbers.index(X) + 1
        else:
            return -1

def main():
    storage = Program()
    N = int(input("Please enter a positive integer: "))
    for _ in range(N):
        number = int(input())
        storage.insert(number)

    X = int(input("Please enter an integer: "))
    index = storage.search(X)
    print(index)

main()
