from module5_mod import Program

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
