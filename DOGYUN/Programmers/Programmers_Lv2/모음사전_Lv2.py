# word : 모음만 사용한 단어
# 사전의 단어 종류는 "A" ~ "UUUUU"
# 단어가 몇 번째 단어인지 return 

from itertools import product

def solution(word):
    answer = 0
    answer_list = []
    alphabet = ["A", "E", "I", "O", "U"]
    
    for i in range(1, 6):
      for j in product(alphabet, repeat= i):
        answer_list.append(''.join(j))
    
    answer_list.sort()
    answer = answer_list.index(word)+1
    
    return answer
  
print(solution("AAAAE"))

# dfs로 복잡하게 생각하지말고 다른 방법 있는지 더 고민하기