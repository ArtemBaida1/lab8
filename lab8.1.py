def fill_array(M, N):
    array = [M * i for i in range(1, N + 1)]
    return array

M = int(input("Введіть число M: "))
N = int(input("Введіть кількість елементів N: "))
result = fill_array(M, N)
print("Масив:", result)
