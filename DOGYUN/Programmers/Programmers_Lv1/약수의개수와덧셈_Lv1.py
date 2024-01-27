# left부터 right까지의 모든 수들 중에서 약수의 개수가 짝수인 수는 더하고, 홀수인 수는 뺀 수 return

def prime_num(number):
  number_list = []
  for i in range(1, int(number**(1/2))+1):
    if number%i == 0:
      number_list.append(i)
      if i**2 != number:
        number_list.append(number//i)
        
  return len(number_list)

def solution(left, right):
  answer = 0
  for num in range(left, right+1):
    if prime_num(num)%2 == 0:
      answer += num
    else:
      answer -= num
  
  return answer

print(solution(24, 27))