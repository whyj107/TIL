# How Much?
# https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/train/python

# 나의 풀이
def howmuch(m, n):
    return [[f'M: {i}', f'B: {i//7}', f'C: {i//9}'] for i in range(min(n, m), max(n, m)+1) if i % 7 == 2 and i % 9 == 1]

# 다른 사람의 풀이
def howmuch1(m, n):
    i = min(m, n)
    j = max(m, n)
    res = []
    while (i <= j):
        if ((i % 9 == 1) and (i %7 == 2)):
            res.append(["M: " + str(i), "B: " + str(i // 7), "C: " + str(i // 9)])
        i += 1
    return res

print(howmuch(1, 100) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
print(howmuch(1000, 1100) == [["M: 1045", "B: 149", "C: 116"]])
print(howmuch(10000, 9950) == [["M: 9991", "B: 1427", "C: 1110"]])
print(howmuch(0, 200) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
print(howmuch(2950, 2950) == [])
print(howmuch(20000, 20100) == [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])