# 원래 이용료 price를 n번째 이용하면 n*price로 지불
# count번 탈 때 가지고 있는 금액에서 얼마가 모자라는지 return

def solution(price, money, count):
  sum = 0
  for i in range(1, count+1):
    sum += i*price

  if sum > money:
    return sum - money
  else:
    return 0

print(solution(3, 20, 4))