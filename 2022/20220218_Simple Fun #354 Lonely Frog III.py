# Simple Fun #354: Lonely Frog III
# https://www.codewars.com/kata/59c9e82ea25c8c05860001aa/train/python

# 나의 풀이
def jump_to(x, y):
    cnt = 0
    while x != y:
        if y//2 == y/2 and y//2 >= x:
            y //= 2
        else:
            y -= 1
        cnt += 1
    return cnt

# 다른 사람의 풀이: 이러한 방법도 있구나 신기하다.
def jump_to1(x, y):
    n = 0
    while y >= 2*x:
        n += y%2 + 1
        y //= 2
    return n + y - x

print(jump_to(1, 8), 3)
print(jump_to(1, 17), 5)
print(jump_to(1, 15), 6)
print(jump_to(3, 12), 2)
print(jump_to(3, 16), 3)
print(jump_to(3, 17), 4)
print(jump_to(10, 19), 9)