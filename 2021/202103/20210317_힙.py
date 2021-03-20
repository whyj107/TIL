# 더 맵게
import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for n in scoville:
        heapq.heappush(heap, n)
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
        answer += 1
    return answer

#############################################################
# 디스크 컨트롤러
import heapq
def solution1(jobs):
    n = len(jobs)
    heap = []
    time, end = 0, -1
    cnt = 0
    answer = 0

    while cnt < n:
        for i in jobs:
            if end < i[0] <= time:
                answer += (time - i[0])
                heapq.heappush(heap, i[1])
        if len(heap) > 0:
            answer += len(heap)*heap[0]
            end = time
            time += heapq.heappop(heap)
            cnt += 1
        else:
            time += 1
    return answer//n

#############################################################
# 이중우선순위큐
import heapq
from collections import deque
def solution2(operations):
    answer = []
    for i in operations:
        cmd, n = i.split()
        if cmd == 'I':
            heapq.heapify(answer)
            heapq.heappush(answer, (int(n)))
        elif cmd == 'D':
            try:
                answer = deque(answer)
                if n == '1': answer.pop()
                elif n == '-1': answer.popleft()
            except:
                pass
        answer = list(answer)
    return [max(answer), min(answer)] if not answer == [] else [0, 0]
