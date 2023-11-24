# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있음
# 개발 속도가 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있음
# 배포 될 때는 앞에 있는 기능이 배포될 때 함께 배포됨
# progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 배열
# speeds : 각 작업의 개발 속도가 적힌 배열
# 각 배포마다 몇 개의 기능이 배포되는지 return

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(progresses)):
      progress_day = math.ceil((100-progresses[i])/speeds[i])
      queue.append(progress_day)
      
    while queue:
      end_day = queue.popleft()
      count = 1
      
      while queue:
        compare_day = queue.popleft()
        if compare_day <= end_day:
          count += 1
        else:
          queue.appendleft(compare_day)
          break
        
      answer.append(count)
      
    return answer
  
print(solution([93, 30, 55], [1, 30, 5]))