# 큐, 덱
#######################################################
# 큐 2
"""
import sys
from collections import deque
q = deque([])
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
"""
#######################################################
# 카드2
"""
import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque(list(range(1, N+1)))
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])
"""
#######################################################
# 요세푸스 문제 0
"""
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque(list(map(str, range(1, N+1))))
lst = []

while q:
    q.rotate(-(K-1))
    lst.append(q.popleft())

print('<' + ', '.join(lst) + '>')
"""
#######################################################
# 프린터 큐
"""
import sys
from collections import deque

def solution(priorities, location):
    answer = 0
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.popleft())
                location = len(priorities) - 1
            else:
                return answer + 1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.popleft())
                location -= 1
            else:
                priorities.popleft()
                location -= 1
                answer += 1

for i in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    p = deque(list(map(int, sys.stdin.readline().split())))
    print(solution(p, M))
"""
#######################################################
# 덱 : 흠... 좀 더 좋은 방법이 없나
"""
import sys
from collections import deque

q = deque([])
for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        q.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        q.append(cmd[1])
    elif cmd[0] == "pop_front":
        if not q: print(-1)
        else: print(q.popleft())
    elif cmd[0] == "pop_back":
        if not q: print(-1)
        else: print(q.pop())
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if not q: print(1)
        else: print(0)
    elif cmd[0] == "front":
        if not q: print(-1)
        else: print(q[0])
    elif cmd[0] == "back":
        if not q: print(-1)
        else: print(q[-1])
"""
#######################################################
# 회전하는 큐 : 큐로 푸는 것보다 이게 더 이해가 편하다. 심지어 del이 pop 보다 더 빨라
"""
from sys import stdin
f = lambda: map(int, stdin.readline().split())
n, m = f()
que = [*range(1, n+1)]
ix, cnt = 0, 0
for _ in f():
    q = que.index(_)
    m1 = abs(q-ix)
    cnt += min(m1, len(que)-m1)
    ix = q
    del que[q]
print(cnt)
"""
#######################################################
# AC : 이 문제도 사실 큐, 덱으로 풀지 않아도 된다. 근데 큐 덱이 더 빠르다.
"""
from sys import stdin, stdout
from collections import deque
def AC(p, q):
    p.replace('RR', '')
    q = deque(q)
    tmp = True
    for c in p:
        if c == 'R':
            tmp = False if tmp else True
        elif c == 'D':
            if q and q[0] != '':
                if tmp:
                    q.popleft()
                else:
                    q.pop()
            else:
                return 'error\n'
    return '['+','.join(q)+']\n' if tmp else '['+','.join(reversed(q))+']\n'

for _ in range(int(stdin.readline())):
    p = stdin.readline()
    n = int(stdin.readline())
    li = stdin.readline().rstrip()[1:-1].split(',')
    stdout.write(AC(p, li))
"""
# 우선순위 큐
# 힙 : 최소가 무조건 맨앞으로 오게됨
#######################################################
# 최대 힙 : 각 숫자 앞에 마이너스 넣고 힙으로 저장하면 제일 큰게 제일 작게되서 맨 앞으로 옴
from sys import stdin
import heapq
N = int(stdin.readline())
lst = []
for _ in range(N):
    n = int(stdin.readline())
    if n != 0:
        heapq.heappush(lst, (-n))
    else:
        try:
            print(-1*heapq.heappop(lst))
        except:
            print(0)
#######################################################
# 최소 힙 : 힙에 넣고 맨앞에꺼 뽑기
from sys import stdin
import heapq
N = int(stdin.readline())
heap = []
for _ in range(N):
    n = int(stdin.readline())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
#######################################################
# 절대값 힙 : 저장할 때 (절대값, 원래숫자) 이렇게 저장하면 절대값 순으로 정렬되니까 맨앞에꺼 뽑기
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
#######################################################
# 가운데를 말해요
from sys import stdin
import heapq
N = int(stdin.readline())
l, r = [], []
for _ in range(N):
    n = int(stdin.readline())
    if len(l) == len(r):
        heapq.heappush(l, (-n, n))
    else:
        heapq.heappush(r, (n, n))

    if r and l[0][1] > r[0][1]:
        l_v = heapq.heappop(l)[1]
        r_v = heapq.heappop(r)[1]
        heapq.heappush(r, (l_v, l_v))
        heapq.heappush(l, (-r_v, r_v))

    print(l[0][1])

