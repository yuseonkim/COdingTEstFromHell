# prices : 초 단위로 기록된 주식가격이 담긴 배열
# 가격이 떨어지지 않은 기간이 몇 초인지 return

def solution(prices):
  answer = [0] * len(prices)
  for i in range(len(prices)):
    for j in range(i, len(prices)-1):
      if prices[i] <= prices[j]:
        answer[i] += 1
      else:
        break

  return answer


print(solution([1, 2, 3, 2, 3]))