import numpy as np

NumbersA = input().split()
NumbersB = input().split()

ListOfNumbersA = [int(x) for x in NumbersA]
ListOfNumbersB = [int(x) for x in NumbersB]

MatrixA = np.array(ListOfNumbersA)
MatrixB = np.array(ListOfNumbersB)

print(np.inner(MatrixA, MatrixB))
print(np.outer(MatrixA, MatrixB))

