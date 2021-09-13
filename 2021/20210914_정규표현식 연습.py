# 점프 투 파이썬
# https://wikidocs.net/4308

"""
[] : 쿤자 클래스, [] 사이의 문자들과 매치.
    정규 표현식이 [abc]이면 a, b, c중 한개의 문자와 매치되면 매치된다고 여긴다.
    [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미
    [a-c]의 경우 abc와 동일하다.
    [a-zA-Z] : 알파벳 모두
    [0-9] : 숫자

    ^ : 반대의미를 지님.
        [^0-9] : 숫자가 아닌 문자


    \d : 숫자와 매치, [0-9]와 같은 의미
    \D : 숫자가 아닌 것과 매치, [^0-9]와 같은 의미
    \s : whitespace 문자와 매치, [ \t\n\r\f\v]와 같은 의미. 맨 앞의 빈 칸은 공백 문자임
    \S : whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 같은 의미
    \w : 문자 + 숫자. [a-zA-Z0-9_]
    \W : 문자 + 숫자 아닌것. [^a-zA-Z0-9_]

. : 줄바꿈 문자인 \n을 제외한 모든 문자와 매칭.
    a.b의 경우 'a+모든문자+b'를 의미한다. → aab, a0b
    만약 abc가 된다면 매치되지 않는다. 그리고 a[.]b의 경우 a.b이다.

* : * 바로 앞에 있는 문자가 무한대로 반복될 수 있다는 의미
    ca*t → ct, cat, caaat

+ : +는 최소 1번 이상 반복될 떄 사용
    ca+t → cat, caaat

{m} : +와 같은 의미이지만 반복 수가 일치해야된다.
      ca{2}t → caat

{m, n} : m ~ n회 반복
        ca{2, 5}t → caat, caaat, caaaat, caaaaat

? : {0, 1}과 같은 의미
    ab?c → ac, abc
"""

import re
p = re.compile('python')

# match() : 문자열의 처음부터 정규식과 매치되는지 조사
m = p.match("python")
print("match:", m)
print("match.group():", m.group())

# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
s = p.search("3 python")
print('search:', s)

# findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
p = re.compile('[a-z]+')
fa = p.findall("life is go on")
print('findall:', fa)

# finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
fi = p.finditer("life is go on")
print('finditer:', fi)
for r in fi: print(r.group())