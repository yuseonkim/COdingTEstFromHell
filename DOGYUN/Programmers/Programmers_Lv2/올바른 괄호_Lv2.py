# 올바른 괄호 : '('로 열렸으면 반드시 짝지어서 ')'로 닫혀야 함
# s가 올바른 괄호이면 True, 아니면 False

def solution(s):
    if s[0] == ')':
      return False
    elif s[len(s)-1] == '(':
      return False
    else:
      for i in s:
        if i == '(':
          a += 1
        else:
          a -= 1
        if a == -1:
          return False
      if a > 0:
        return False
      
    return True
  
print(solution('())((()))(()'))