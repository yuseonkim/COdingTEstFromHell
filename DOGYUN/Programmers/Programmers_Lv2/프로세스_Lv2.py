# 대기 큐에서 하나를 꺼냄 -> 우선순위가 더 높은 프로세스가 있으면 꺼낸 프로세스를 다시 넣음
# 더 높은 프로세스가 없으면 꺼낸 큐 실행 -> 실행한 프로세스는 다시 넣지 않고 종료
# priorities : 우선 순위 정보가 담긴 배열
# location : 몇 번째로 실행되는지 알고 싶은 프로세스 위치 / index로 생각 (0으로 시작)

from collections import deque

def solution(priorities, location):  
    q = deque(priorities)
    answer = 0
    while q:
      max_value = max(q)
      start = q.popleft()
      location -= 1
      if start != max_value:
        q.append(start)
        if location < 0:
          location = len(q) - 1
      else:
          answer += 1
          if location < 0:
            break

    return answer
  
print(solution([2, 1, 3, 2], 2))