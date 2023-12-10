# 던파...?
# k : 현재 피로도
# dungeons : 최소 필요 필요도, 소모 필요도가 담긴 2차원 배열
# 유저가 탐험할 수 있는 최대 던전 수 return

from itertools import permutations

def solution(k, dungeons):
    dungeons_length = len(dungeons)
    answer_list = [i for i in range(dungeons_length)]
    for i in range(dungeons_length, 0, -1):
      for cases in permutations(answer_list, i):
        current = k
        check = True
        for case in cases:
          if current < dungeons[case][0]:
            check = False
            break
          else:
            current -= dungeons[case][1]
        if check:
          return i
  
print(solution(80, [[80,20],[50,40],[30,10]]))