# N마리의 포켓몬 중 N/2마리 가져가도 됨
# 종류에 따라 번호를 부여
# 최대한 많은 종류의 포켓몬을 포함해서 선택 (최대 N/2 마리인 것)
# nums: N마리 포켓몬의 종류 번호
# 최대한 많은 종류를 가져가는 방법의 포켓몬 종류 번호의 개수를 return

def solution(nums):
    answer = 0
    max_select = int(len(nums) / 2) # a
    nums_set = list(set(nums)) # b
    
    if max_select > len(nums_set):
      answer = len(nums_set)
    else:
      answer = max_select
      
    return answer
  
print(solution([3,3,3,2,2,2]))