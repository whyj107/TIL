# 완주하지 못한 선수
from collections import Counter
def solution(p, c):
    p_ = Counter(p)
    c_ = Counter(c)
    p_.subtract(c_)
    return p_.most_common(1)[0][0]

def solution1(p, c):
    tmp = 0
    dic = {}
    for p_ in p:
        dic[hash(p_)] = p_
        tmp += int(hash(p_))
    for c_ in c:
        tmp -= hash(c_)
    answer = dic[tmp]
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution1(["m", "j", "n", "l", "l"], ["j", "l", "m", "n"]))

#############################################################
# 전화번호 목록
def solution2(pb):
    pb.sort()
    for p1, p2 in zip(pb, pb[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution3(pb):
    h_m = {}
    for p in pb:
        h_m[p] = 1
    for p in pb:
        tmp = ""
        for n in p:
            tmp += n
            if tmp in h_m and tmp != p:
                return False
    return True

import re
def solution4(pb):
    for b in pb:
        p = re.compilt("^"+b)
        for b2 in pb:
            if b != b2 and p.match(b2):
                return False
    return True

#############################################################
# 위장
def solution5(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([k for n, k in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

def solution6(clothes):
    clothes_type = {}
    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1
    cnt = 1
    for num in clothes_type.values():
        cnt *= num
    return cnt - 1

print(solution6([["yellowhat", "headgear"],
                 ["bluesunglasses", "eyewear"],
                 ["green_turban", "headgear"]]), 5)

#############################################################
# 베스트앨범
def solution7(genres, plays):
    music = {}
    music_total_play = {}
    for i in range(len(genres)):
        if not genres[i] in music.keys():
            music[genres[i]] = [(-plays[i], i)]
            music_total_play[genres[i]] = plays[i]
        else:
            music[genres[i]] += [(-plays[i], i)]
            music_total_play[genres[i]] += plays[i]
    sorted_m_t = sorted(music_total_play.items(), key=lambda i: i[1], reverse=True)
    answer = []
    for k in sorted_m_t:
        sorted_m = sorted(music[k[0]], key=lambda x: (x[0], x[1]))
        answer.append(sorted_m[0][1])
        if len(sorted_m) > 1:
            answer.append(sorted_m[1][1])
    return answer