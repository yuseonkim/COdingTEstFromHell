# 어떤 수에서 k개의 수를 제거했을 때 가장 큰 숫자 구하기
# number : 문자열 형식의 숫자 / k : 제거 할 개수


def solution(number, k):
    answer = []
    
    for num in number:
      if not answer:
        answer.append(num)
        continue
      if k>0:
        while answer[-1] < num:
          answer.pop()
          k -= 1
          if not answer or k<=0:
            break
      answer.append(num)
    
    answer = answer[:-k] if k > 0 else answer
    
    return ''.join(answer)
  
print(solution("1924", 2))