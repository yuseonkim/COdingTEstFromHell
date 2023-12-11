# 다양한 명함을 모두 수납할 수 있는 지갑의 크기 정하기
# 가로, 세로를 바꿀 수 있음
# sizes : 모든 명함의 가로, 세로 길이가 나오는 2차원 배열
# 지갑의 크기 return

def solution(sizes):
    answer = 0
    w_list = []
    h_list = []
    
    for size in sizes:
      w_list.append(max(size))
      h_list.append(min(size))
        
    answer = max(w_list) * max(h_list)
    return answer
  
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))