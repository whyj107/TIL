# Find the unique number
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

# 나의 풀이
# 이렇게 하면 time over 난다.
def find_uniq0(arr):
    return min(arr, key=arr.count)

# 이렇게 하면 되긴 된다.
def find_uniq1(arr):
    result = {}
    for a in arr:
        if a in result.keys():
            result[a] += 1
        else:
            result[a] = 1
    return sorted(result.items(), key=lambda x: x[1])[0][0]

# 하지만 set을 사용하는 다른 사람의 방법이 최고인듯
# 다른 사람의 풀이
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)