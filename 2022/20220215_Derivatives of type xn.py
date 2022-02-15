# Derivatives of type x^n
# https://www.codewars.com/kata/55e2de13b668981d3300003d/train/python

# 나의 풀이
def differentiate(poly):
    if 'x' in poly:
        tmp = poly.split('x')
        a = int(tmp[0]) if not tmp[0] in ["", "-"] else (1 if tmp[0] == '' else -1)
        if '^' in tmp[1]:
            b = int(tmp[1].replace('^', ''))
            if b-1 != 1:
                result = f'{a * b}x^{b - 1}'
            else:
                result = f'{a*b}x'
        else:
            result = f'{a}'
    else:
        result = '0'
    return result

# 다른 사람의 풀이
from re import compile
REGEX = compile(r"(-?\d*)(x?)\^?(-?\d*)").fullmatch
def differentiate1(poly):
    a, x, n = REGEX(poly).groups()
    a, n = int(-1 if a=='-' else a or 1), int(n or bool(x))
    if n == 0 or n == 1: return f"{a*n}"
    if n == 2: return f"{a*n}x"
    return f"{a*n}x^{n-1}"

# print(differentiate("3x^2" ), "6x")
# print(differentiate("-7x"), "-7")
print(differentiate("-x"), "-1")