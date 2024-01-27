# 0~9중 일부가 들어있는 정수 배열에서 없는 숫자를 모두 더한 수 return

def solution(numbers):
  number_list = [i for i in range(10)]
  not_founded = []
  
  for num in number_list:
    if num not in numbers:
      not_founded.append(num)
      
  return sum(not_founded)

print(solution([5,8,4,0,6,7,9]))