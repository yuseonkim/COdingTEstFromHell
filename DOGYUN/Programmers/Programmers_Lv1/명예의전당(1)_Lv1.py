# 출연 가수의 점수가 상위 k번째 이내이면 명예의 전당에 리스트업
# k일 다음부터는 출연 가수의 점수가 k번째 순위의 가수 점수보다 높으면 오르고, 기존 k번째 순위 점수는 제거
# 매일 발표된 명예의 전달의 최하위 점수를 return

# 배열의 최대 길이는 k
# 배열의 길이가 k보다 작으면 그냥 추가 / k보다 커지면 정렬해서 index 1~3까지만
# 배열의 0번째를 answer 리스트에 추가

def solution(k, score):
    answer = []
    rank = []
    
    for s in score:
      rank.append(s)
      if len(rank) <= k:
        rank.sort()
        answer.append(rank[0])
      else:
        rank.sort()
        rank = rank[1:k+1]
        answer.append(rank[0])

    return answer
  
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))