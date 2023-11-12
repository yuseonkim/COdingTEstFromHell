# (세로 좌표, 가로 좌표)
# 빈칸은 ".", 파일 있는 칸은 "#"
# 최소한의 이동거리로 한 번의 드래그로 모든 파일 삭제 -> S(시작점)에서 E(끝점)로 이동
# 이동 거리 (E-S)로 정의
# [S(lux, luy), E(rdx, rdy)] return 
def solution(wallpaper):
    start = []
    end = []
    
    for i in range(len(wallpaper)):
        if ('#' not in wallpaper[i]):
            continue
        else:
            for j in range(len(wallpaper[i])):
                if (wallpaper[i][j] == '#'):
                  start.append(i)
                  end.append(j)
                    
    return [min(start), min(end), max(start) + 1, max(end) + 1]
  

print(solution([".#...", "..#..", "...#."]))