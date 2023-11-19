# 하루에 1개만 구입 가능
# 판매는 얼마든지 할 수 있음
# 첫 줄에 테스트 케이스 수 T / 두번째 줄 몇 일인지 N / 세번째부터 매매가 리스트 / 각 날의 매매가는 10000원 이하
# 테스트 케이스는 #1 (최대이익), #2 (최대이익) 이런 식으로 출력
# 매매가가 최대인 날 찾기 / 반대로 돌면서 최대값 찾음 -> 최대값인 날 한번에 계산하는 것으로 생각

t = int(input())

for i in range(1, t+1): 
  n = int(input())
  cost_list = list(map(int, input().split(' ')))
  max_cost = cost_list[-1]
  profit = 0
  
  for day in range(n-2, -1, -1):
    if cost_list[day] >= max_cost:
      max_cost = cost_list[day]
    else:
      profit += max_cost - cost_list[day]
  
  print('#{} {}'.format(i, profit))
