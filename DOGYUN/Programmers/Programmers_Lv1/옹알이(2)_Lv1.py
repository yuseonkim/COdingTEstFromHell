# 조카가 발음할 수 있는 단어의 개수를 return
# aya, ye, woo, ma
# 같은 단어를 연속으로 발음하는 것은 불가능

def solution(babbling):
  answer = 0
  words = ['aya', 'ye', 'woo', 'ma']
  
  for bab in babbling:
    for j in words:
      if j*2 not in bab:
        bab = bab.replace(j, ' ')
    if len(bab.strip()) == 0:
      answer += 1
      
  return answer

print(solution(["aya", "yee", "u", "maa"]))