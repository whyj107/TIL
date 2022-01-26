# Your order, please
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

# 나의 풀이
def order(sentence):
    answer = {}
    for s in sentence.split():
        idx = ''
        for i in s:
            if i.isnumeric():
                idx += i
        answer[int(idx)] = s
    return ' '.join(v for k, v in sorted(answer.items()))

# 다른 사람의 풀이
def order1(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

def order2(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")