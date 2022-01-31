# Data Reverse
# https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python

# 나의 풀이
def data_reverse(data):
    result = []
    for i in range(len(data), -1, -8):
        result += data[i:i+8]
    return result

# 다른 사람의 풀이
def data_reverse1(data):
    res = []

    for i in range(len(data) - 8, -1, -8):
        res.extend(data[i:i + 8])

    return res

data1 = [1, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 1, 1, 1, 1,
         1, 0, 1, 0, 1, 0, 1, 0]
data2 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
print(data_reverse(data1) == data2)

data3 = [0, 0, 1, 1, 0, 1, 1, 0,
         0, 0, 1, 0, 1, 0, 0, 1]
data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
print(data_reverse(data3) == data4)