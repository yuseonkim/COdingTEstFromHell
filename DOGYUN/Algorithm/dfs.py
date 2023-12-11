# n = 정점의 개수 / m = 간선의 개수 / v = 탐색을 시작할 정점의 번호
# 인접행렬, stack 자료구조로 구현
n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split()) # 간선이 연결하는 두 정점의 번호
  matrix[f][t] = matrix[t][f] = 1 # 서로 연결되어 있음을 표현
  
def dfs(matrix, i, visited):
  stack = [i]
  while matrix:
    value = stack.pop()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
    for c in range(len(matrix[value])-1, -1, -1): # 스택에서 pop 될 때는 탐색 순서의 반대로 나오기 때문에 역순으로 봐줌
      if matrix[value][c] == 1 and not visited[c]:
        stack.append(c)

dfs(matrix, v, visited)

# 인접리스트, stack으로 구현
n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  # 간선으로 연결되어 있는 노드를 표시
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
  if graph[t] == []:
    graph[t] = [f]
  else:
    graph[t].append(f)
    
def dfs_list(graph, i, visited):
  stack = [i]
  visited[i] = True
  while stack:
    value = stack.pop()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
    
    for j in graph[value]:
      if not visited[j]:
        stack.append(j)
        
for i in graph: # 스택에서 pop 될 때는 탐색 순서의 반대로 나오기 때문에 역순으로 봐줌
  i.reverse()
  
dfs_list(graph, v, visited)