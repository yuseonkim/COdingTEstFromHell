# n = 정점의 개수 / m = 간선의 개수 / v = 탐색을 시작할 정점의 번호
# 인접행렬, queue 자료구조로 구현
from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1) ]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  matrix[f][t] = matrix[t][f] = 1

def bfs(matrix, i, visited):
  queue = deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      
      # 다음으로 가야될 연결된 노드를 찾고, queue에 넣음
      for c in range(len(matrix[value])):
        if matrix[value][c] == 1 and not visited:
          queue.append(c)
          
# 인접리스트, queue 자료구조로 구현
from collections import deque

n, m, v = map(int, input().split())
graph = [[] * (n+1)]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
  if graph[t] == []:
    graph[t] = [f]
  else:
    graph[t].append(f)

def bfs_list(graph, i, visited):
  queue = deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for j in graph[value]:
        queue.append(j)