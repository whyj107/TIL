# last digits of a number
# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python

# 나의 풀이
def solution(n, d):
    n = str(n)
    return list(map(int, n[len(n)-d if len(n) > d else 0:]))


# 다른 사람의 풀이
def solution1(n, d):
    return [int(c) for c in str(n)[-d:]] if d > 0 else []

print(solution(1, 1), [1])
print(solution(123767, 4), [3, 7, 6, 7])
print(solution(0, 1), [0])
print(solution(34625647867585, 10), [5, 6, 4, 7, 8, 6, 7, 5, 8, 5])

print(solution(1234, 0), [])
print(solution(24134, -4), [])

print(solution(1343, 5), [1, 3, 4, 3])