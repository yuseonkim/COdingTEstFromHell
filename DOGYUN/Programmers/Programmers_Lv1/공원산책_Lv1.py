# 지나갈 수 있는 길 'O' / 장애물 'X'
# [방향 거리, 방향 거리] => [E 5] : 동쪽으로 5칸
# 명령 수행 전 이동이 공원을 벗어나는지, 장애물이 있는지 확인 => 문제 생기면 명령 무시
# park: 공원 문자열 배열 / routes: 수행할 명령이 담긴 문자열 배열
# 첫번째 문자로 방향 정함 -> 두번째 문자만큼 가면서 X를 만나거나 공원 범위 넘치면 수행 안하고 넘김
# 수행 성공 시 그 위치를 다시 start 위치로 정함

def solution(park, routes):
    x, y = 0, 0
    w, h = len(park[0]), len(park)
    fourWays = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    
    for i in range(len(park)):
      for j in range(len(park[i])):
        if (park[i][j]=='S'):
          x = i
          y = j
          break
    
    for route in routes:
      dx, dy = x, y
      direction, distance = route.split(' ')
      
      for i in range((int(distance))):
        nx = x + fourWays[direction][0]
        ny = y + fourWays[direction][1]
        
        if 0<=nx<=h-1 and 0<=ny<=w-1 and (park[nx][ny]!='X'):
          x, y = nx, ny
        else:
          x, y = dx, dy    
          break

    return (x, y)
  
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))