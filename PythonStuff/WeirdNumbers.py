for N in range(100):
    Answer1 = str(N) + " = Not Weird"
    Answer2 = str(N) + " = Weird"
    if N % 2 != 0:
        print(Answer2)
    else:
        if N > 20:
            print(Answer1)
        else:
            if N in range(2, 6):
                print(Answer1)
            else:
                print(Answer2)
