# a : 마트에 주는 병 수
# b : 마트에서 받는 병 수
# n : 가지고 있는 병 수

# n을 a로 나눈 몫과 나머지를 더했을 때 a보다 작으면 탈출
# 몫을 answer에 더하기

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        m = (n//a)*b
        rest = n%a
        n = m+rest
        answer += m
    return answer

print(solution(3, 1, 20))