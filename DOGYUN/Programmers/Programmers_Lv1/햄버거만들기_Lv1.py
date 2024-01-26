# 1 - 2 - 3 - 1 의 순서가 나오는가?
# 처음부터 하나씩 쌓아서 해당 순서가 나오는지?
# 나오면 그 숫자들은 빼고 나머지로 다시 순서가 나오는지 확인해야 됨
# 순서가 완성되면 answer+1

def solution(ingredient):
  answer = 0
  correct_list = [1, 2, 3, 1]
  n_list = []
  for i in ingredient:
    n_list.append(i)
    if n_list[-4:] == correct_list:
      answer += 1
      for _ in range(4):
        n_list.pop()
  
  return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))