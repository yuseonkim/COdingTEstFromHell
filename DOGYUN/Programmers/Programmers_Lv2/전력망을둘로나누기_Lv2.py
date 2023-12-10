# n개의 송전탑이 하나의 트리 형태로 연결
# 하나를 끊어서 2개로 분할 -> 최대한 개수가 비슷하게
# n : 송전탑의 개수
# wires : 전선 정보
# 최대한 비슷하게 나눴을 때 송전탑의 개수의 차이를 return

from collections import deque

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
      graph[a].append(b)
      graph[b].append(a)
    
    def bfs(start):
      visited = [0] * (n+1)
      q = deque([start])
      visited[start] = 1
      count = 1
      while q:
        value = q.popleft()
        for i in graph[value]:
          if not visited[i]:
            q.append(i)
            visited[i] = 1
            count += 1
      
      return count
    
    answer = n
    for a, b in wires:
      graph[a].remove(b)
      graph[b].remove(a)
      
      answer = min(abs(bfs(a) - bfs(b)), answer)
      
      graph[a].append(b)
      graph[b].append(a)
    
    return answer
  
print(solution(4, [[1,2],[2,3],[3,4]]))