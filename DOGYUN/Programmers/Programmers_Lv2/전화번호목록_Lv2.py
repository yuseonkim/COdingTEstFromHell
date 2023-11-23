# phone_book : 전화번호가 담긴 배열
# 접두어는 한 번호가 다른 번호의 앞부분에 포함되어 있는 경우임
# 어떤 번호가 다른 번호의 접두어인 경우 false, 아닌 경우 true를 return

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
      current = phone_book[i]
      next = phone_book[i+1]
      current_length = len(current)
      if current[0] != next[0]:
        continue
      if current == next[:current_length]:
        return False
        
    return answer
  
print(solution(["0", "119"]))