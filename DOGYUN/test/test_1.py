# 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하는 문제
# 두 사람이 선물을 주고 받은 기록이 있음 -> 이번 달까지 선물 준 횟수가 많은 사람이 다음 달에 선물 하나 받음
# 두 사람이 선물을 주고받은 기록이 하나도 없거나 같다면, 선물 지수가 더 큰 사람이 작은 사람에게 선물을 하나 받음
# 선물 주고 받은 기록이 없거나 같은 경우 + 선물 지수가 같으면, 다음 달에 선물을 주고받지 않음
# 선물 지수 = (이번 달까지 자신이 친구들에게 준 선물의 수) - (받은 선물의 수)
# friends : 친구들의 이름을 담은 1차원 배열
# gifts : 친구들이 주고받은 선물 기록을 담은 1차원 배열 [선물을 준 친구, 선물을 받은 친구]
# 다음 달에 가장 많은 선물을 받는 친구가 받은 선물의 수 return

def solution(friends, gifts):
    answer = 0
    answer_list = []
    friends_gift_score = []
    
    # 친구끼리 주고받은 선물 배열 만들기
    friends_matrix = [[0] * len(friends) for _ in range(len(friends))]
    for gift in gifts:
      a, b = gift.split()
      a_index = friends.index(a)
      b_index = friends.index(b)
      friends_matrix[a_index][b_index] += 1
    
    # 선물 지수 만들기
    for i in range(len(friends_matrix)):
      for _ in range(len(friends_matrix[i])):
        get = sum(friends_matrix[i])
        send = sum(k[i] for k in friends_matrix)
      friends_gift_score.append(get - send)
    
    # 비교 로직
    for i in range(len(friends_matrix)):
      gift = 0
      for j in range(len(friends_matrix[i])):
        if i == j:
          continue
        else:
          if friends_matrix[i][j] > friends_matrix[j][i]:
            gift += 1
          elif friends_matrix[i][j] == friends_matrix[j][i] or friends_matrix[i][j] == friends_matrix[j][i] == 0:
            if friends_gift_score[i] > friends_gift_score[j]:
              gift += 1
      answer_list.append(gift)
    
    answer = max(answer_list)
    return answer
  
print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
