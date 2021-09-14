# 점프 투 파이썬
# https://wikidocs.net/4308

import re
p = re.compile('[a-z]+')

"""
group() : 매치된 문자열을 돌려준다.
start() : 매치된 문자열의 시작 위치를 돌려준다. → 항상 0일 수밖에 없다. match니까
end() : 매치된 문자열의 끝 위치를 돌려준다.
span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
"""
# match
print("match")
m = p.match("python")
print('group():', m.group())
print('start():', m.start())
print('end():', m.end())
print('span():', m.span())

print('-------------------------------')

# search
print("search")
s = p.search("3 python")
print('group():', s.group())
print('start():', s.start())
print('end():', s.end())
print('span():', s.span())

print('-------------------------------')

# 모듈 단위로 수행하기
m = re.match('[a-z]+', "python")
print(m.group())
s = re.search('[a-z]+', "3 python")
print(s.group())

print('-------------------------------')

"""
컴파일 옵션
 - DOTALL(S)        : .이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
 - IGNORECASE(I)    : 대소문자에 관계없이 매치할 수 있도록 한다.
 - MULTILINE(M)     : 여러줄과 매치할 수 있도록한다. (^, $ 메타문자의 사용과 관계 있음)
 - VERBOSE(X)       : verbose 모드를 사용할 수 있도록 한다.(정규식을 보기 편하게 만들 수
                      있고 주석등을 사용할 수 있음).
"""
# DOTALL
p = re.compile('a.b')
m = p.match('a\nb')
p1 = re.compile('a.b', re.DOTALL)
m1 = p1.match('a\nb')
print(m, m1)

print('-------------------------------')

# IGNORECASE
p = re.compile('[a-z]+', re.I)
print(p.match('python'), p.match('Python'), p.match('PYTHON'))

print('-------------------------------')

# MULTILINE
# ^ : 문자열의 처음 의미
# $ : 문자열의 마지막 의미
p = re.compile("^python\s\w+")
p1 = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data), p1.findall(data))

print('-------------------------------')

# VERBOSE
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# ==
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)