# 왼, 오에서 시작해서 중앙에 있는 물을 빨리 먹으면 이기는 게임
# 홀수로 나와도 짝수로 진행하고 나머지는 버림
# 음식 배치가 나오는 문자열 return

def solution(food):
    side = ''
    for i in range(1, len(food)):
      side += str(i)*(food[i]//2)
    answer = side + '0' + side[::-1]
    
    return answer

print(solution([1, 3, 4, 6]))