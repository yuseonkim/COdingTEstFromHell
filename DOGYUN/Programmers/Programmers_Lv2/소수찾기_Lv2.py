# numbers : 숫자가 적힌 문자열
# numbers의 숫자를 분해해서 만들 수 있는 소수 개수 Return
# 시간 복잡도 해결을 위해 에라토스테네스의 체 이용하기

from itertools import permutations
import math

def isPrimeNumber(num):
    if num <= 1:
        return False 
    
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
          
    return True
    
def solution(numbers):
    number_list = list(numbers)
    numbers_set = set()
    for i in range(1, len(numbers)+1):
        permutationList = permutations(number_list, i)
        for perm in permutationList:
            num = int(''.join(perm))
            numbers_set.add(num)

    count = 0
    for num in numbers_set:
        if isPrimeNumber(num):
            count+=1
            
    return count
  
print(solution("011"))