# 조이스틱으로 알파벳 이름 완성 / 처음은 'A'로만 되어있음
# 규칙
# 위, 아래 : 다음 / 이전 알파벳으로 이동(A ~ Z -> A)
# 왼쪽, 오른쪽 : 커서(cursor) 이동
# name : 만들고자 하는 이름
# 조이스틱 조작 횟수의 최솟값 return
# 연속된 A는 커서 이동만 하면 되기 때문에 그 부분을 고려하기!!

def solution(name):
    answer = 0
    length = len(name)

    def alphabet_to_number(c):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(c) - ord('A')]

    for ch in name:
        answer += alphabet_to_number(ch)

    move = length - 1
    for i in range(length):
        next = i + 1
        while (next < length) and (name[next] == 'A'):
            next += 1
        distance = min(i, length - next)
        move = min(move, i + length - next + distance)

    answer += move
    return answer
  
print(solution('JAN'))