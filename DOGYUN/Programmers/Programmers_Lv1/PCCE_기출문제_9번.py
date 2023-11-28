# 2차원 격자 보드판에서 상하좌우 중 같은 색깔로 칠해진 칸의 개수 구하기
# board : 2차원 문자열 리스트
# h, w : 칸의 위치

def solution(board, h, w):
    answer = 0
    length = len(board)
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    for direction in directions:
        next_h = h + direction[0]
        next_w = w + direction[1]
        
        if next_w>=0 and next_w<length and next_h>=0 and next_h<length:
            if board[h][w] == board[next_h][next_w]:
                answer += 1
    
    return answer

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))