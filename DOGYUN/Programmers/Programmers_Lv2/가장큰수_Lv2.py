# 0 또는 양의 정수가 주어졌을 때, 정수를 이어붙여 만들 수 있는 가장 큰 수 구하기
# numbers : 0 또는 양의 정수가 담긴 배열
# 가장 큰 수를 문자열로 return

def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers_str)))
  
solution([6, 10, 2])