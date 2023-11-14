# keymap에 저장된 순서로 누른 만큼의 index 문자가 나옴
# 아예 할당되지 않은 경우도 있음 -> -1 return
# 특정 문자열을 작성할 때 키를 최소 몇 번 눌러야 하는지
# keymap : 문자열 순서가 담긴 배열
# targets : 입력하려는 문자열들이 담긴 배열
# targets에 하나를 검사하면 그 결과값을 answer 배열에 넣어줌
# keymap 입력에 대한 최소값을 찾아야 됨 -> key가 없으면 그냥 넘어가 -> 있으면 검사해

def solution(keymap, targets):
    answer = []
    press = 0
    
    for target in targets:
      press = 0
      for c in target:
        flag = False
        time = 101
        
        for key in keymap:
          if c in key:
            time = min(key.index(c)+1, time)
            flag = True
        
        if not flag:
            press = -1
            break
        
        press += time
        
      answer.append(press)
            
    return answer
  
print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))