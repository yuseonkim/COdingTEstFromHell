# 중심이 원점이고, 반지름이 각각 r1, r2인 원 사이 공간의 정수 좌표(r1 < r2)
# 좌표는 r1, r2의 테두리도 포함
# 영역 내에 있는 x, y 좌표 r1 원 <= k <= r2 원
# r1**2 <= x**2 + y**2 <= r2**2
# x좌표의 최대 최소 범위 정해서 그 안에 있는 정수 모두 카운트
# 1사분면만 해서 *4
import math

def solution(r1, r2):
    answer = 0
    for y in range(1, r2+1):
      if (r1**2-y**2) > 0:
        min_x = math.ceil((r1**2-y**2)**0.5)
      else:
        min_x = 0
      max_x = math.floor((r2**2-y**2)**0.5)
    
      if max_x == min_x and min_x != 0:
        answer += 1
      elif max_x != min_x:
        answer += (max_x - min_x+1)
      else:
        answer += 1

    return answer*4
  
print(solution(2, 3))