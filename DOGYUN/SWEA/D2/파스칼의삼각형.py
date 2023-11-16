# 첫 줄에는 테스트 케이스 수 T / 두 번째 줄부터 크기 N으로 파스칼 삼각형 만듦
# 1
# 1 1
# 1 2 1
# 1 3 3 1
import sys

T = int(sys.stdin.readline())

for test in range(T):
  N = int(sys.stdin.readline())
  pascal = [[0] * N for _ in range(N)]
  pascal[0][0] = 1
  for i in range(1, N):
    for j in range(N):
      if j == 0:
        pascal[i][j] = 1
      else:
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
  print('#{}'.format(test))
  
  for k in range(N):
    for l in range(N):
      if pascal[k][l]:
        print(pascal[k][l], end=' ')
    print()