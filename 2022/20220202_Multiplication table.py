# Multiplication table
# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

# 나의 풀이
def multiplication_table(size):
    return [[j for j in range(i, i*(size+1), i)] for i in range(1, size+1)]

# 다른 사람의 풀이
def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

print(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])