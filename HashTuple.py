if __name__ == '__main__':
    UnnecessaryInput = input()
    tupleOfInputValues = tuple([int(x) for x in input().split()])
    print(hash(tupleOfInputValues))
