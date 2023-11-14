# 페인트가 칠해진 길이가 n미터인 벽
# 벽 -> 1미터 크기의 n개로 나눔 -> 1번부터 n번
# 롤러의 길이 m -> 롤러가 벽을 벗어나면 안됨(나머지가 생기면 그건 버리기)
# section -> 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 
# 칠하는 수 return
# m 길이 안에 포함되면 다 칠할 수 있음, 근데 이제 칠하려고 하는데 길이가 전체 n 초과하면 못해줌

def solution(n, m, section):
  count = 1
  start = section[0]
  for i in range(1, len(section)):
    if ((section[i] - start) >= m):
      count += 1
      start = section[i]
  
  return count
  
print(solution(8, 4, [2, 3, 6]))