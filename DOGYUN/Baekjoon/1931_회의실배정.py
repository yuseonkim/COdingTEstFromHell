n = int(input())

endPoint = 0
answer = 0
li = []

for i in range(0, n):
  a, b = map(int, input().split())
  li.append([a, b])

li.sort(key=lambda x: (x[1], x[0]))

for start, end in li:
  if endPoint <= start:
    answer += 1
    endPoint = end

print(answer)