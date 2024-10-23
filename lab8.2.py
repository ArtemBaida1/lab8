import numpy as np

def fill_matrix(N):
    matrix = np.arange(N**2, 0, -1).reshape(N, N)
    return matrix

N = int(input("Введіть число N: "))
matrix = fill_matrix(N)
print("Матриця:")
print(matrix)