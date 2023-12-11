# 수포자 찍는 방식과 정답 비교해서 가장 많이 맞춘 쪽의 번호 return

def solution(answers):
    answer = []
    a_list = [1, 2, 3, 4, 5]
    b_list = [2, 1, 2, 3, 2, 4, 2, 5]
    c_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a, b, c = 0, 0, 0
    
    for i in range(len(answers)):
      a_index = i%len(a_list)
      b_index = i%len(b_list)
      c_index = i%len(c_list)
      
      if a_list[a_index] == answers[i]:
        a += 1
      if b_list[b_index] == answers[i]:
        b += 1
      if c_list[c_index] == answers[i]:
        c += 1
    
    max_num = max(a, b, c)
    
    if max_num == a:
      answer.append(1)
    if max_num == b:
      answer.append(2)
    if max_num == c:
      answer.append(3)
    
    return answer
  
solution([1,3,2,4,2])