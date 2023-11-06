# s: 문자열
# skip: 스킵할 알파벳 문자열
# index: 건너 뛸 수
# s를 돌면서 문자 1개에 index만큼까지의 문자를 봄
# 문자에 skip의 문자가 있는지를 확인
# 있는 수만큼 counting 해서 index에 값을 추가

def solution(s, skip, index):
    answer = ''
    # for c in s:
    #     i = ord(c)
    #     j = index
    #     while j > 0:
    #         i += 1
    #         if i > ord('z'):
    #             i = ord('a')
    #         if chr(i) in skip:
    #             j += 1
    #         j -= 1
    #     answer += chr(i)
    
    for c in s:
        al = ord(c)
        i = index
        while i > 0:
            al += 1
            if al > ord('z'):
              al = ord('a')
            if chr(al) in skip:
              i += 1
            i -= 1
        answer += chr(al)
      
    return answer

print(solution("aukks", "wbqd", 5))
