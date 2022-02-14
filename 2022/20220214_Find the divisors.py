# Find the divisors!
# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python

# 나의 풀이
def divisors(integer):
    result = set()
    for i in range(2, int(integer**0.5)+1):
        if integer//i == integer/i:
            result.add(i)
            result.add(integer//i)
    return f'{integer} is prime' if len(result) == 0 else sorted(list(result))

# 다른 사람의 풀이
def divisors1(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

print(divisors(15), [3, 5])
print(divisors(253), [11, 23])
print(divisors(24), [2, 3, 4, 6, 8, 12])
print(divisors(25), [5])
print(divisors(90), [2, 3, 5, 6, 9, 10, 15, 18, 30, 45])
print(divisors(13), "13 is prime")
print(divisors(3), "3 is prime")
print(divisors(29), "29 is prime")
