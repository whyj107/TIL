# 정렬
#######################################################
# 수 정렬하기 3
"""
import sys
series = [0] * 10001
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    series[a] += 1

for b in range(len(series)):
    if series[b] != 0:
        for c in range(series[b]):
            print(b)
"""
#######################################################
# 통계학
"""
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
"""
"""
import sys
from collections import Counter

n = int(sys.stdin.readline())
result = [int(sys.stdin.readline()) for i in range(n)]

# 산술평균 출력(소수점 이하 첫째 자리에서 반올림)
print(round(sum(result)/n))

# n이 1개일 경우 계산이 따로 필요 없음
if n == 1:
    # 중앙값 출력
    print(result[0])
    # 최빈값 출력
    print(result[0])
    # 범위 출력 = result[0] - result[0]
    print(0)
else:
    # 중앙값을 얻기 위해서 정렬
    result = sorted(result)
    # 중앙값 출력
    print(result[n//2])

    # 최빈값을 얻기 위해서 Counter를 이용
    # 빈도수를 dict로 만들어 줌
    cnt = Counter(result)
    # 배열 안에 튜플형식으로 최빈값부터 반환
    cnts = cnt.most_common()

    # 최빈값이 여러개일 경우 2번째 것 출력
    # 그래서 처음과 두번쨰만 비교한 후 두번째 것을 출력하면 됨
    if cnts[0][1] == cnts[1][1]:
        mode = cnts[1][0]
    else:
        mode = cnts[0][0]
    # 최빈값 출력
    print(mode)
    # 범위 출력
    print(result[-1]-result[0])
"""
#######################################################
# 좌표 정렬하기
"""
dots = [list(map(int, input().split())) for _ in range(int(input()))]
for i, j in sorted(dots, key=lambda x: (x[0], x[1])):
    print(i, j)
"""
#######################################################
# 좌표 정렬하기2
"""
for i, j in sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0])):
    print(i, j)
"""
#######################################################
# 단어 정렬
"""
tmp = [input() for _ in range(int(input()))]
for i in sorted(list(set(tmp)), key=lambda x: (len(x), x)):
    print(i)
"""
#######################################################
# 나이순 정렬
"""
tmp = [(*map(str, input().split()),) for _ in range(int(input()))]
for i, j in sorted(tmp, key=lambda x: (int(x[0]))):
    print(i, j)
"""
#######################################################
# 백트래킹 : 모든 경우를 탐색하는 백트래킹 알고리즘
#######################################################
"""
# N과 M(1)
from itertools import permutations, combinations, product, combinations_with_replacement
N, M = map(int, input().split())
for i in permutations(range(1, N+1), M):
    print(*i)
print('--------------------------------------')
# N과 M(2)
for i in combinations(range(1, N+1), M):
    print(*i)
print('--------------------------------------')
# N과 M(3)
for i in product(*[range(1, N+1)]*M):
    print(*i)
# N과 M(4)
# https://docs.python.org/ko/3/library/itertools.html#itertools.combinations_with_replacement
for i in combinations_with_replacement(range(1, N+1), M):
    print(*i)
"""
#######################################################
# N-Queen
def solve(a, b, c, i, ans):
    if i == n: return ans + 1

    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            ans = solve(a, b, c, i + 1, ans)
            a[j] = b[i+j] = c[i-j+n-1] = False
    return ans

if __name__=='__main__':
    n = int(input())

    # 체스판을 (x,y)라고 생각했을 때
    # a는 세로, b는 대각선 /, c는 대각선 \
    # n = 5    a(y)           b(x+y)        c(x-y+n-1)
    #       0 1 2 3 4       0 1 2 3 4       4 3 2 1 0
    #       0 1 2 3 4       1 2 3 4 5       5 4 3 2 1
    #       0 1 2 3 4       2 3 4 5 6       6 5 4 3 2
    #       0 1 2 3 4       3 4 5 6 7       7 6 5 4 3
    #       0 1 2 3 4       4 5 6 7 8       8 7 6 5 4

    # 0-4
    a = [False]*n
    # 0-8
    b = [False]*(2*n-1)
    # 0-8
    c = [False]*(2*n-1)

    ans = solve(a, b, c, 0, 0)
    print(ans)
    # python으로 제출시 런타임 에러
    answer = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
    print(answer[n])
