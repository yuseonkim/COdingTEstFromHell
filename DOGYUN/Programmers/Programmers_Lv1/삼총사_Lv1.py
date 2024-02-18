# 3명의 번호를 더했을 때 0이 되면 삼총사
# 삼총사를 만들 수 있는 방법의 수 return

from itertools import combinations

def solution(number):
  answer = 0
  
  for i in combinations(number, 3):
    if sum(i) == 0:
      answer += 1
        
  return answer

print(solution([-2, 3, 0, 2, -5]))