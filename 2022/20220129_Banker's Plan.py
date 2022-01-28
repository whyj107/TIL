# Banker's Plan
# https://www.codewars.com/kata/56445c4755d0e45b8c00010a/train/python

# 나의 풀이
import math
def fortune(f0, p, c0, n, i):
    f, c = f0, c0
    for _ in range(n-1):
        f = math.trunc(f + f*0.01*p - c)
        c = math.trunc(c + c*0.01*i)
    return f >= 0

# 다른 사람의 풀이
def fortune1(f, p, c, n, i):
    for _ in range(n-1):
        f = int(f * (100 + p) / 100 - c)
        c = int(c * (100 + i) / 100)
        if f < 0:
            return False
    return True

print(fortune(100000, 1, 2000, 15, 1), True)
print(fortune(100000, 1, 9185, 12, 1), False)
print(fortune(100000000, 1, 100000, 50, 1), True)
print(fortune(100000000, 1.5, 10000000, 50, 1), False)
print(fortune(100000000, 5, 1000000, 50, 1), True)
print(fortune(10000.0, 0, 10000.0, 2, 0), True)

"""
100000, 91815, 83457, 74923, 66211, 57318, 48241, 38977, 29523, 19877, 10035, -5

f0 = 100000, p = 1 percent, c0 = 2000, n = 15, i = 1 percent

f1 = 100000 + 0.01*100000 - 2000 = 99000;  
c1 = c0 + c0*0.01 = 2020 (with inflation of previous year)

f2 =  99000 + 0.01*99000 - 2020  = 97970;  
c2 = c1 + c1*0.01 = 2040.20 
(with inflation of previous year, truncated to 2040)

4 -> f3 =  97970 + 0.01*97970 - 2040  = 96909.7 (truncated to 96909); 
c3 = c2 + c2*0.01 = 2060.4 (with inflation of previous year, truncated to 2060)
"""