# 알파벳을 0~9의 숫자로 바꿔서 합하는 문제
# 같은 알파벳은 같은 숫자, 같은 숫자를 여러 알파벳에 주는 것 안됨
# 입력
# 첫째 줄 단어의 개수 N / 2~N째 줄 단어가 하나씩 입력(알파벳 대문자로만)
# 단어의 최대 길이 10 / N의 최대 길이 8
# 출력 : 단어의 합의 최댓값
# 자릿수가 가장 높은 쪽, 같은 자릿수의 경우 다음 수가 어느 자리에 있느냐에 따라

N = int(input())
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
sum = 0
word_list = []

for _ in range(N):
  words = input()
  word_list.append(words)

for word in word_list:
  for i in range(len(word)):
    num = 10 ** (len(word)-i-1) # 몇번째 자릿수
    alphabet_dict[word[i]] += num

for value in alphabet_dict.values():
  if value > 0:
    alphabet_list.append(value)

alphabet_list.sort(reverse=True)
for i in range(len(alphabet_list)):
  sum += alphabet_list[i] * (9-i)

print(sum)