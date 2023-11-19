# 모든 학생(N)이 자신이 몇 등일지 예상 등수를 적음
# A등인데 B등으로 적어서 낸 경우, 불만도 = (|A-B|)
# 예상 등수 리스트가 있을 때, 불만도의 합을 최소로 하는 프로그램 만들기
import sys

n = int(sys.stdin.readline())

score = 0
student = sorted([int(sys.stdin.readline()) for _ in range(n)])
for i in range(n):
  if student[i] != i+1:
    score += abs(student[i] - (i+1))
      
print(score)
# [1, 5, 3, 1, 2] 
# [1, 1, 2, 3, 5]