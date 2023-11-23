# 1~4번 지표에는 각각 2개의 유형이 들어있음(알파벳) 총 16가지
# 각 지표당 1개씩 총 4개의 유형을 선택 ex) RFMN
# n개의 질문이 있고, 각 질문에 7개의 답변 중 하나를 선택해서 점수를 매김
# 더 높은 점수를 얻은 유형이 지표에 들어가서 4개를 조합해서 성격 유형이 결정
# survey : 지표가 담긴 배열
# choices : 각 질문마다 선택한 선택지

def solution(survey, choices):
    answer = ''
    answer_dic = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0 }
    
    for s, c in zip(survey, choices): # AN 5
      if c > 4:
        answer_dic[s[1]] += c-4
      elif c < 4:
        answer_dic[s[0]] += 4-c
    
    answer_list = list(answer_dic.items())
    
    for i in range(0, 8, 2):
      if answer_list[i][1] < answer_list[i+1][1]:
        answer += answer_list[i+1][0]
      else:
        answer += answer_list[i][0]
    
    return answer
    
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))