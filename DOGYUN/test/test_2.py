# 그래프는 크기 N에 따라 모양이 달라지며, 1개 이상의 정점과, 정점들을 연결하는 단방향 간선으로 이루어짐
# 도넛 모양 그래프
# 크기가 n일 때, n개의 정점과 n개의 간선이 있음 -> 방문하지 않은 곳으로 이동 => 최종적으로 원래 자기 위치(출발 정점)으로 돌아옴
# 막대 모양 그래프
# 크기가 n일 때, n개의 정점과 (n-1)개의 간선이 있음 -> 방문하지 않은 곳으로 이동 => 최종적으로 마지막 노드에 도착
# 8자 모양 그래프
# 크기가 n일 때, (2n+1)개의 정점과 (2n+2)개의 간선이 있음 -> 방문하지 않은 곳으로 이동 
# size가 1인 경우를 제외하고는 => 어디로 들어갔느냐에 따라 갈 수 있는 영역이 다름(위쪽, 가운데, 아래쪽)
# 위쪽 => 위쪽만 / 가운데 => 원하는 쪽으로 / 아래쪽 => 아래쪽만
# 그래프와는 무관한 정점에서 시작해서 그래프에 간선을 연결 / 각 정점에 서로 다른 번호를 매김
# edges : 그래프의 간선 정보를 담은 2차원 배열
# edges는 [a, b]의 형태(a -> b로 향하는 간선이 있음)
# [(생성한 정점의 번호), (도넛 모양 그래프의 수), (막대 모양 그래프의 수), (8자 모양 그래프의 수)] return
# 1. 초기상태 : 서로 연결된 경우, matrix의 값은 1 / 서로 연결되어 있지 않은 경우, matrix의 값은 0
# a) matrix[i][i]인 지점의 값이 1이면, a += 1 
# b) 1인 지점이 matrix[i][j]이면, 해당 경로를 타고 들어가서 다시 원래 지점으로 돌아올 수 있는지 확인
#    b-1) 돌아올 수 없다면 b += 1 
#    b-2) 돌아올 수 있다면 matrix[i] 부분에 1이 몇 개 있는지 확인
#        b-2-1) 1이 있는 부분이 1개면 a += 1 
#        b-2-2) 1이 있는 부분이 2개면 c += 1 

def dfs(matrix, start, answer):
  stack = [start]
  visited = [False] * len(matrix)
  
  while stack:
    v = stack.pop()
    
    if not visited[v]:
      visited[v] = True
      for i in range(len(matrix[v])):
        if matrix[v][i] == 1 and not visited[i]:
          stack.append(i)
          if i in stack:
            answer[3] += 1
            break
          if i == v:
            answer[1] += 1
            
        
def solution(edges):
    answer = [0, 0, 0, 0] # [(생성한 정점의 번호), (도넛 모양 그래프의 수), (막대 모양 그래프의 수), (8자 모양 그래프의 수)]
    max_num_per = [0 for _ in range(len(edges))]
    
    for i, (a, b) in enumerate(edges):
      max_num_per[i] = max(a, b)
      
    max_num = max(max_num_per) # N X N을 위한 N 구하기
    # 초기 init
    matrix = [[0]*(max_num) for _ in range(max_num)]
    for _ in range(max_num):
      for edge in edges:
        a, b = edge[0]-1, edge[1]-1
        matrix[a][b] = 1
    
    for i in range(max_num):
      dfs(matrix, i, answer)
      
    print(answer)
    return answer
  
solution([[2, 3], [4, 3], [1, 1], [2, 1]])
# solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])