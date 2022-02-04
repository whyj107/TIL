# Character Counter
# https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python

# 나의 풀이
def validate_word(word):
    word = word.lower()
    return len(set(word.count(i) for i in set(word))) == 1

# 다른 사람의 풀이
from collections import Counter
def validate_word1(word):
    return len(set(Counter(word.lower()).values())) == 1

print(validate_word("abcabc"), True)
print(validate_word("Abcabc"), True)
print(validate_word("AbcabcC"), False)
print(validate_word("AbcCBa"), True)
print(validate_word("pippi"), False)
print(validate_word("?!?!?!"), True)
print(validate_word("abc123"), True)
print(validate_word("abcabcd"), False)
print(validate_word("abc!abc!"), True)
print(validate_word("abc:abc"), False)