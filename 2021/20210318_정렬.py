# K번째수

def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = map(int, c)
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer

def solution1(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#############################################################
# 가장 큰 수

def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

#############################################################
# H-Index

def solution3(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0