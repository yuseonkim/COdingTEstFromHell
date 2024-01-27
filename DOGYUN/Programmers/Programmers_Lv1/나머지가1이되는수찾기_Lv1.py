# n이 주어졌을 때 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 return

def solution(n):
  answer = 0
  i = 1
  while i>0:
    if n%i == 1:
      return i
    i+=1
  return answer

print(solution(12))