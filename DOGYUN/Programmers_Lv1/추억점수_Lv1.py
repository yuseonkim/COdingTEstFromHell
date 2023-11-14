# 사진별로 추억점수를 매기려고 함
# 그리움 점수를 모두 더한 값이 해당 사진의 추억 점수 (점수가 없는 사람은 0으로 취급)
# name = ["may", "kein", "kain", "radi"]
# yearning = [5, 10, 1, 3]
# photo = [
  # ["may", "kein", "kain", "radi"],
  # ["may", "kein", "brin", "deny"], 
  # ["kon", "kain", "may", "coni"]
#  ]

# photo에서 1개씩 돌면서 이름에 맞는 점수 대입 -> 인덱스 이용
# 한 사진에 들어가는 사람의 이름이 name에 있는지 확인 -> 있으면 점수 넣기

def solution(name, yearning, photo):
  answer = []
  
  for ph in photo:
    score = 0
    for n in ph:
      if n in name:
        score += yearning[name.index(n)]
    answer.append(score)
      
  return answer