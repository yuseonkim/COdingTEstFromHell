# 수빈이 현재 위치 점 N / 동생 위치 점 K
# 수빈이가 X에서 걸으면 X-1, X+1로 이동 / 순간이동하면 0초(시간 안 걸림) 현재 위치에서 2배 위치로 이동
# 수빈이와 동생의 위치가 주어졌을 때, 수빈 -> 동생 찾는 가장 빠른 시간

# 2번
# 5 = 2*2 + 1 / 101
# 10 = 2*2*2 + 2 / 1010
# 9 = 2*2*2 + 1 / 1001
# 18 = 2*2*2*2 + 2 / 10010
# 17 = 2*2*2*2 + 1 / 10001

# 2번
# 4 = 2*2 / 10
# 5 = 2*2 + 1 / 101
# 10 = 2*2*2 + 2 / 1010
# 20 = 2*2*2*2 + 2*2 / 10100
# 21 = 2*2*2*2 + 2*2 + 1 / 10101 

# 1번
# 3 = 2 + 1 / 11
# 6 = 2*2 + 2 / 110
# 12 = 2*2*2 + 2*2 / 1100
# 11 = 2*2*2 + 2 + 1 / 1011

import sys
from collections import deque

def bfs():
  graph = [-1] * 100001
  graph[n] = 0
  queue = deque([n])
  
  while queue:
    target = queue.popleft()
    # 동생 위치 도착
    if target == k:
      return graph[target]
    # 이동 경우 파악
    for i in (target+1, target-1, target*2):
      # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
      if 0 <= i <= 100000 and graph[i] == -1:
        if i == target * 2:
          graph[i] = graph[target] # 현재까지의 최단 시간을 유지
          queue.appendleft(i) # 순간이동이기에 먼저 탐색(순간이동은 시간이 소요되지 않기 때문에 큐의 왼쪽에 추가)
        else:
          graph[i] = graph[target] + 1 # 현재까지의 시간에 +1
          queue.append(i) # 탐색하기 때문에 큐의 오른쪽에 추가(일반적인 추가)
          
    
n, k = map(int, sys.stdin.readline().split())
print(bfs())