# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer

#############################################################
# 주식가격
def solution1(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer

#############################################################
# 기능개발
import math
def solution2(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    pre = 0
    for i in range(len(progresses)):
        if progresses[pre] < progresses[i]:
            answer.append(i-pre)
            pre = i
    answer.append(len(progresses)-pre)
    return answer

#############################################################
# 프린터
def solution3(priorities, location):
    answer = 0
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location = len(priorities)-1
            else:
                return answer+1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location -= 1
            else:
                priorities.pop(0)
                location -= 1
                answer += 1

def solution4(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
