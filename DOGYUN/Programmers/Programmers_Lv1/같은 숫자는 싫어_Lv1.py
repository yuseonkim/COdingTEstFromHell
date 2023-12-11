# arr : 1~9사이의 수로 이루어진 배열
# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):
  answer = []
  
  answer.append(arr[0])
  count = 0
  for i in arr[1:]:
    if answer[count] == i:
      continue
    else:
      answer.append(i)
      count += 1
        
  return answer

solution([1,1,3,3,0,1,1])