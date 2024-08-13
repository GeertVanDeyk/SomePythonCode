if __name__ == '__main__':
    n = int(input())
    Scores = input().split()
    ListOfScores = [int(x) for x in Scores]
    SortedListOfScores = sorted(set(ListOfScores))  # sort unique values
    HighestScore = max(SortedListOfScores)
    RunnerUpScore = max(SortedListOfScores[-2:-1])
    # max funtion makes the returned set an integer
    print(RunnerUpScore)
#  or
#  RunnerUpScore = max(sorted(set(ListOfScores))[-2:-1]))
    