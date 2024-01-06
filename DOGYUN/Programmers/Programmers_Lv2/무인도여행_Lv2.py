# X는 바다 / 숫자는 무인도의 식량 1일분
# 상하좌우 연결된 건 하나로 침 -> 식량도 합침
# maps : 지도를 나타내는 문자열 배열
# 각 섬에서 머무를 수 있는 최대 일수 / 없으면 -1 return

def dfs(maps, i, j, n, m, visited):
  visited[i][j] = True
  area = int(maps[i][j])
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  for dx, dy in directions:
    x, y = i + dx, j + dy
    if 0 <= x < n and 0 <= y < m and not visited[x][y] and maps[x][y] != 'X':
      area += dfs(maps, x, y, n, m, visited)

  return area

def solution(maps):
  answer = []
  n, m = len(maps), len(maps[0])
  visited = [[False] * m for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if maps[i][j] != 'X' and not visited[i][j]:
        answer.append(dfs(maps, i, j, n, m, visited))

  if answer:
    return sorted(answer)
  else:
    return [-1]
    