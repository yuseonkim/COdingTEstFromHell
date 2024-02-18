# x, y, n이 주어질 때 x를 y로 변환하기 위해 필요한 최소 연산 횟수 Return
# 만들 수 없으면 -1 return
# case 만들어서 queue 사용하면 될듯

from collections import deque

def solution(x, y, n):
    answer = 0
    dist = [0 for _ in range(y+1)]
    queue = deque()
    queue.append(x)
    
    if x == y:
      return 0
    
    while queue:
      new_x = queue.popleft()
      for i in range(3):
        if i == 0:
          current_x = new_x * 2
        if i == 1:
          current_x = new_x * 3
        if i == 2:
          current_x = new_x + n
        if current_x > y or dist[current_x]:
          continue
        if current_x == y:
          return dist[new_x] + 1
        queue.append(current_x)
        dist[current_x] = dist[new_x] + 1
    
    return -1
  
print(solution(2, 5, 4))