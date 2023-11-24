import heapq # heapq는 최소힙만 다룸

# 노드 추가 : heappush
heap = []
heapq.heappush(heap, 1)

# 노드 삭제 : heappop
heapq.heappop(heap) # 가장 작은 원소(루트 노드)를 꺼내어 리턴
# print(heap[0]) : 꺼내지 않고 return만 하고 싶은 경우 인덱스로 접근 / 인덱스 1이 두번째로 작다는 보장은 없음 
# n번째로 작은 원소 -> n-1개의 원소를 빼내야 함

# 기존 리스트 힙으로 변환하기
tmp = [7, 5, 8, 3]
heapq.heapify(tmp)
print(tmp)

# 힙정렬
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, value)
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result

# 최대 힙 만들기 예시
heap_items = [1, 5, 3, 2, 4]
max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, item)
for i in max_heap:
  print(-i) # 값에 - 붙여서 최대 힙으로 바꾸기