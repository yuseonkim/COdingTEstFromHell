# X는 바다 / 숫자는 무인도의 식량 1일분
# 상하좌우 연결된 건 하나로 침 -> 식량도 합침
# maps : 지도를 나타내는 문자열 배열
# 각 섬에서 머무를 수 있는 최대 일수 / 없으면 -1 return

from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(maps, i, j, n, m, visit):
    visit[i][j] = 1
    q = deque()
    q.append([i, j])
    days = 0
    while q:
        i, j = q.popleft()
        days += int(maps[i][j])
        for d in range(4):
            x, y = i + dx[d], j + dy[d]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 0 and maps[x][y] != 'X':
                q.append([x, y])
                visit[x][y] = 1
    return days

def solution(maps):
  answer = []
  for i in range(len(maps)):
      maps[i] = list(maps[i])
  n = len(maps)
  m = len(maps[0])
  visit = [[0] * m for _ in range(n)]
  
  for i in range(n):
      for j in range(m):
          if maps[i][j] != 'X' and visit[i][j] == 0:
              answer.append(dfs(maps, i, j, n, m, visit))
  if answer:
      return sorted(answer)
  else:
      return [-1]
    