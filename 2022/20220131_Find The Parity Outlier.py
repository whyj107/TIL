# Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

# 나의 풀이
def find_outlier(integers):
    result = {0: [], 1: []}
    for i in integers:
        result[i % 2].append(i)
    return result[0][0] if len(result[0])==1 else result[1][0]

# 다른 사람의 풀이
def find_outlier1(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

"""
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""