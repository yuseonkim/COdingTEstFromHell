# targets : x축 평행하게 s~e로 미사일 발사하는 영역 배열
# (s, e) 범위 내에서 겹치는 부분을 y축 평행하게 1번 발사하면 요격 가능
# 필요한 미사일의 최솟값 return

def solution(targets):
  answer = 0
  targets.sort(key=lambda x:[x[1], x[0]])
  
  s, e = 0, 0
  for target in targets:
    if target[0] >= e:
      answer += 1
      e = target[1]
    
  return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))