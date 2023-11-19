# 카드 뭉치에서 한 장씩 꺼내서 사용
# cards1, cards2 : 문자열로 이루어진 배열(최대 길이 10) / 서로 다른 단어가 존재
# 원하는 단어 배열 : goal
# 만들 수 있으면 Yes / 만들 수 없으면 No return
# 첫 번째 인덱스에서 찾을 수 있는지 확인이 필요 -> 없으면 바로 No return 

def solution(cards1, cards2, goal):
    answer = ''
    cards1_index, cards2_index = 0, 0
    
    for i in range(len(goal)):
      if (goal[i] not in cards1[cards1_index]) and (goal[i] not in cards2[cards2_index]):
        answer = 'No'
        break
      elif (goal[i] in cards1[cards1_index]):
        cards1_index += 1
        answer = 'Yes'
        if (cards1_index >= len(cards1)):
          cards1_index = 0
        
      elif (goal[i] in cards2[cards2_index]):
        cards2_index += 1
        answer = 'Yes'
        if (cards2_index >= len(cards2)):
          cards2_index = 0
        
        
    return answer
    
print(solution(["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"]))