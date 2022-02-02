# Find the stray number
# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

# 나의 풀이
def stray(arr):
    result = {}
    for a in arr:
        if a in result.keys():
            result[a] += 1
        else:
            result[a] = 1
    return sorted(result.items(), key=lambda x: x[1])[0][0]

# 다른 사람의 풀이
def stray1(arr):
    return min(arr, key=arr.count)

print(stray([1, 1, 1, 1, 1, 1, 2]), 2)
print(stray([2, 3, 2, 2, 2]), 3)
print(stray([3, 2, 2, 2, 2]), 3)