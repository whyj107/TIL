# 스택
#######################################################
# 제로
"""
import sys
answer = []
for i in range(int(sys.stdin.readline())):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        answer.pop()
    else:
        answer.append(tmp)
print(sum(answer))
"""
#######################################################
# 괄호
"""
import sys
for i in range(int(sys.stdin.readline())):
    answer = []
    for j in sys.stdin.readline().strip():
        try:
            if j == '(': answer.append(j)
            else: answer.pop()
        except:
            answer = [1]
            break
    print("YES" if answer == [] else "NO")
"""
#######################################################
# 균형잡힌 세상
"""
import sys
input_str = sys.stdin.readline().rstrip()
while input_str != '.':
    try:
        if input_str[-1] != '.': raise
        else:
            tmp1 = []
            for i in input_str:
                if i == '(' or i == '[': tmp1.append(i)
                elif i == ')' and tmp1.pop() != '(': raise
                elif i == ']' and tmp1.pop() != '[': raise
            if tmp1 == []: print("yes")
            else: print("no")
    except:
        print("no")
    input_str = sys.stdin.readline().rstrip()
"""
#######################################################
# 스택 수열
"""
from sys import stdin
def solve(tmp):
    cnt, stack, result = 1, [], []
    for i in tmp:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)

print(solve([int(stdin.readline()) for i in range(int(stdin.readline()))]))
"""
#######################################################
# 17298 오큰수
from sys import stdin
def solve(n, l):
    answer = [-1] * n
    idx, stack_tmp = 0, [0]
    while stack_tmp and idx < n:
        while stack_tmp and l[stack_tmp[-1]] < l[idx]:
            answer[stack_tmp.pop()] = l[idx]
        stack_tmp.append(idx)
        idx += 1
    return answer
n = int(stdin.readline())
input_list = list(map(int, stdin.readline().split()))
for i in solve(n, input_list):
    print(i, end=" ")