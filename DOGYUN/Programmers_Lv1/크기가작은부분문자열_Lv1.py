# t에서 p와 길이가 같은 부분문자열 중
# 부분문자열이 p보다 작거나 같은 것이 나오는 횟수 return

def solution(t, p):
    answer = 0
    p_length = len(p)
    t_slice = []
    count = p_length
    
    for i in range(len(t)):
      t_slice.append(int(t[i:count]))
      count += 1
      if (len(t[i:count]) <= p_length):
        break
    
    list = [i for i in range(len(t_slice)) if t_slice[i] <= int(p)]
    answer = len(list)
    
    return answer
  
print(solution("3141592", "271"))