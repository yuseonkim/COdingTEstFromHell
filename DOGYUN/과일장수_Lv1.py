# 1~k점까지의 등급으로 사과 분류
# 한 상자에 m개씩 포장
# 가장 낮은 점수 p, 사과 한 상자 가격은 p*m => 최대 이익 구하기
# 점수를 sort reverse -> m개만큼 새 배열에 넣어서 점수 계산 -> 점수 모두 더함
def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    box = []
    for i in range(len(score)):
        box.append(score[i]) # 4, 4, 4
        if ((i+1) % m == 0): # box에 포장할 수 되었을 때
            min_score = min(box) # 4
            answer += min_score * m
            box = []
            
    return answer
  
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	))