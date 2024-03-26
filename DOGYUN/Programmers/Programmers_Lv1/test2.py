# 손상된 히스토그램(너비가 1이고 높이가 0 이상의 정수인 막대그래프로 구성)
# 검은 부분이 손상된 부분
# histogram : 히스토그램의 정보가 담긴 2차원 배열
# 0은 비어있는 부분, 1은 막대그래프가 있는 부분, 2는 손상된 부분

def solution(histogram):
  answer = []
  graph = []
  height = len(histogram)-1 # 5
  width = len(histogram[0]) # 5
  for i in range(width): # 0~5 막대그래프 1개 0, 1, 2, 3, 4
    count = 1
    for j in range(height, -1, -1): # 0~6 높이 1개씩 올라가면서 5,4,3,2,1,0
      graph.append(histogram[j][i])
      if histogram[j][i] == 0:
        answer.append(count)
        break
      elif histogram[j][i] == 1:
        if 2 in graph:
          count = 1
        else:
          count += 1
      else:
        count += 1

        
  return answer

print(solution([[0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [1,0,1,0,0], [2,1,2,2,2], [2,1,2,2,2]]))