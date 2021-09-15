# 정규표현식 실전 연습
import re

# 휴대전화번호
phone_number = re.compile('^01[01]-\d{3,4}-\d{4}$')
print(phone_number.match("010-123-3456"))
print(phone_number.match("011-1233-3456"))

# 이메일
email = re.compile('^\w+@\w+\.\w+$')
print(email.match("whyj107@gmail.com"))
print(email.match("whyj107@@gmail.com"))
print(email.match("whyj107"))

# 비밀번호 : 최소 길이 8이상, 대소문자 포함, 적어도 하나의 숫자 표함
pw = re.compile('^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,}$')
print(pw.match("abcedfg1"))
print(pw.match("abcedf"))
print(pw.match("abcedf1"))
print(pw.match("abcedf1%"))

# () 내의 조건은 반드시 필요 조건이다.
