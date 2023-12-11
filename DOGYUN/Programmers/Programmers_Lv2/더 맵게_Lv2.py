# 음식의 스코빌 지수를 K 이상으로 만들기
# 스코빌 지수가 가장 낮은 두 개의 음식을 섞어 새로운 음식으로 만듦 : 새 스코빌 지수 = 가장 덜 맵 + (두번째로 덜 맵 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
# 만들 수 없는 경우 -1 return
# scoville : 음식의 스코빌 지수를 담은 배열 
# K : 스코빌 지수
# 섞어야 하는 최소 횟수 return
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
      heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
      answer += 1
      if len(scoville) == 1 and scoville[0] < K:
        return -1
      
    return answer
  
print(solution([1, 2, 3, 9, 10, 12], 7))