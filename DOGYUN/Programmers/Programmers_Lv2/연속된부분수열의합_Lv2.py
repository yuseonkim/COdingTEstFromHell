# sequence : 오름차순으로 정렬된 수열
# sequence에서 조건을 만족하는 부분 수열 찾기
# 부분수열의 합 k / 부분수열은 1개씩만 선택 아님(연속해서)
# 합이 k인 부분 수열이 여러 개인 경우, 짧은 수열 선택
# 길이가 짧은 수열이 여러 개인 경우, 앞쪽(시작 인덱스가 작은) 수열 선택
# 시작 인덱스 = 0 / 내가 생각하는 방식에서 -1

def solution(sequence, k):
  answer = []
  l = len(sequence)
  end = 0
  part = sequence[0]
  
  for start in range(l):
    while end+1 < l and part < k:
      end += 1
      part += sequence[end]
      print(start, end, part)
    if part == k:
      if not answer:
        answer = [start, end]
      else:
        answer_start, answer_end = answer
        if end - start < answer_end - answer_start:
          answer = [start, end]
          
    part -= sequence[start]
  return answer

print(solution([1, 1, 1, 2, 3, 4, 5], 5))