# 16+18=214
# https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

# 나의 풀이
def add(num1, num2):
    answer = []
    while num1 > 0 or num2 > 0:
        n1 = num1 % 10
        n2 = num2 % 10
        answer.append(str(n1+n2))
        num1 //= 10
        num2 //= 10
    return int(''.join(answer[::-1])) if answer != [] else 0

# 다른 사람의 풀이
def add1(a,b):
    s = ""
    while a+b:
        a,p = divmod(a,10)
        b,q = divmod(b,10)
        s = str(p+q)+s
    return int(s or'0')

print(add(2, 11), 13)
print(add(0, 1), 1)
print(add(0, 0), 0)

print(add(16, 18), 214)
print(add(26, 39), 515)
print(add(122, 81), 1103)
