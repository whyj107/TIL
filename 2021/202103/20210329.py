# 재귀 단계
# 팩토리얼
# 이렇게 풀면 런타임 오류가 발생한다.
"""
def f(n):
    if n == 1: return 1
    return n * f(n-1)
num = int(input())
print(f(num))

# 함수도 존재한다.
import math
print(math.factorial(int(input())))
"""
#######################################################
# 피보나치 수
"""
def fibo(n):
    a, b = 0, 1
    for k in range(n):
        a, b = b, a+b
    return a

print(fibo(num))
"""
#######################################################
# 하노이 탑 이동 순서
"""
def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)
        hanoi(disk - 1, mid, start, end)

total = int(input())
answer = 0

for disk in range(total):
    answer *= 2
    answer += 1

print(answer)
hanoi(total, 1, 2, 3)
"""
#######################################################
# 브루트 포스
"""
N, M = map(int, input().split(' '))
n = list(map(int, input().split(' ')))
answer = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = n[i]+n[j]+n[k]
            if sum_v <= M and sum_v > answer:
                answer = sum_v
print(answer)
# 사실 콤비네이션을 이용해서 가장 큰 값을 구해도 된다.
from itertools import combinations
print(max(v for v in map(sum, combinations(n, 3)) if v <= M))
"""
#######################################################
# 분해합
"""
n = int(input())
answer = 0
for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    answer = i + sum(n_list)

    if answer == n:
        print(i)
        break

    if i == n:
        print(0)
"""
#######################################################
# 덩치
"""
people = [(*map(int, input().split(' ')),) for _ in range(int(input()))]
answer = ""
for w, h in people:
    rank = 1
    for w1, h1 in people:
        if (w < w1) & (h < h1):
            rank += 1
    answer += str(rank) + " "
print(answer)
"""
#######################################################
"""
# 영화감독 숌
N = int(input())
movie = 666
while N:
    if '666' in str(movie): N -= 1
    movie += 1
print(movie - 1)
"""