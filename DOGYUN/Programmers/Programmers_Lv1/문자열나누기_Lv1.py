# 문자열 분해하기
# 첫 글자 : x
# x와 x가 아닌 글자가 나온 횟수를 셈
# 처음으로 두 횟수가 같아지는 순간 멈추고 문자열 분리
# 분해한 문자열 개수를 return

def solution(s):
  answer = 0
  first_word_count = 0
  different_word_count = 0

  for i in s: # banana
    if first_word_count == different_word_count:
        answer += 1
        k = i
    if k == i:
      first_word_count += 1
    else:
      different_word_count += 1
      
  return answer

print(solution('banana'))