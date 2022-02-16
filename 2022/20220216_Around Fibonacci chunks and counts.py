# Around Fibonacci: chunks and counts
# https://www.codewars.com/kata/59bf943cafcda28e31000130/train/python

# 나의 풀이
def around_fib0(n):
    fibo = [0 for _ in range(n+1)]
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]

    fibo_n = str(fibo[n])
    lc_idx = len(fibo_n) % 25 if len(fibo_n)%25 != 0 else 25
    last_chunk = fibo_n[-lc_idx:]

    digit_n, max_n = 0, fibo_n.count('0')
    for i in range(1, 10):
        tmp = fibo_n.count(str(i))
        if max_n < tmp:
            digit_n = i
            max_n = tmp
    return f'Last chunk {last_chunk}; Max is { max_n } for digit { digit_n }'

# 피보나치 계산만 바꾼 것
def around_fib(n):
    fibo1, fibo2 = 0, 1
    for i in range(n-1):
        fibo1, fibo2 = fibo2, fibo1+fibo2

    fibo_n = str(fibo2)
    lc_idx = len(fibo_n) % 25 if len(fibo_n)%25 != 0 else 25
    last_chunk = fibo_n[-lc_idx:]

    digit_n, max_n = 0, fibo_n.count('0')
    for i in range(1, 10):
        tmp = fibo_n.count(str(i))
        if max_n < tmp:
            digit_n = i
            max_n = tmp
    return f'Last chunk {last_chunk}; Max is { max_n } for digit { digit_n }'


# 다른 사람의 풀이
def around_fib1(n):
    a, b = 0, 1
    for i in range(n-1): a, b = b, a + b
    fib = str(b)
    lst = len(fib) % 25
    if lst == 0:
        lst = 25
    maxcnt = 0; digit = -1
    for i in '0123456789':
        c = fib.count(i)
        if c > maxcnt:
            maxcnt = c
            digit = i
    return "Last chunk {}; Max is {} for digit {}".format(fib[-lst:], maxcnt, digit)

print(around_fib(666), "Last chunk 56699078708088; Max is 18 for digit 8")
print(around_fib(934), "Last chunk 78863403327510987087; Max is 30 for digit 7")
print(around_fib(957), 'Last chunk 5402420264154456349058562; Max is 29 for digit 2')