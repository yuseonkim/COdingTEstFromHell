# 일차선 다리 지나는 트럭 -> 모든 트럭이 건너는 최소 시간 구하기
# bridge_length : 다리에 올라갈 수 있는 최대 트럭 수(칸 수로 생각, 100이면 100칸)
# weight : 다리가 견딜 수 있는 무게

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    while truck_weights:
      answer += 1
      current -= bridge.popleft()
      if (current + truck_weights[0]) <= weight:
        truck_start = truck_weights.popleft()
        current += truck_start
        bridge.append(truck_start)
      else:
        bridge.append(0)
    
    answer += bridge_length
    
    return answer
  
print(solution(2, 10, [7, 4, 5, 6]))