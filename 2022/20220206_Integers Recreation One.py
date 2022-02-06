# Integers: Recreation One
# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

# 나의 풀이
def list_squared(m, n):
    result = []
    for i in range(m, n+1):
        tmp = []
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                tmp.append(j**2)
                if j**2 != i:
                    tmp.append((i//j)**2)
        if sum(tmp)**0.5 == int(sum(tmp)**0.5):
            result.append([i, sum(tmp)])
    return result

# 다른 사람의 풀이
CACHE = {}
def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number]
    return CACHE[number]

def list_squared1(m, n):
    ret = []
    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])
    return ret

print(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
print(list_squared(42, 250), [[42, 2500], [246, 84100]])
print(list_squared(250, 500), [[287, 84100]])