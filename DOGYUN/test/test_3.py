# n개의 주사위를 가지고 승부 -> N차까지 있음
# 각 주사위는 1~n의 번호를 가지고 있으며, 주사위에 쓰인 수의 구성은 모두 다름
# A가 먼저 n/2개의 주사위를 가져가고, B가 나머지 n/2개 가져감
# 가져간 주사위로 나온 수를 합해 점수를 계산 -> 점수가 더 큰 쪽이 승리하고, 같으면 무승부
# A가 승리하기 위해 골라야하는 주사위 번호를 오름차순으로 배열에 담아 return
# dice[i]는 i+1번째 주사위에 쓰인 6개의 수를 담고 있음 -> dice[0] : 첫번째 시행 / len(dice[i]) = 6

from itertools import combinations

def solution(dice):
  answer = []
  max_count = 0
  result_index = None
  
  combinations_list = list(combinations(dice, len(dice)//2))
  
  for combination in combinations_list:
    a = list(combination) # A가 뽑은 것
    b = [dic for dic in dice if dic not in a] # B가 뽑은 것
    # A가 가지는 수 & B가 가지는 수
    a_one_dimension = [element for row in a for element in row]
    a_one_dimension.sort(reverse=True)
    a_index = [dice.index(selected_dice) + 1 for selected_dice in a]
    
    b_one_dimension = [element for row in b for element in row]
    b_one_dimension.sort(reverse=True)
    b_index = [dice.index(selected_dice) + 1 for selected_dice in b]
    
    count = sum(1 for a_val in a_one_dimension for b_val in b_one_dimension if a_val > b_val)
    
    if count >= len(a_one_dimension) // 2 + 1:
      if count > max_count:
        max_count = count
        result_index = (a_index, b_index)
      
    answer = result_index[0]

  return answer

solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])