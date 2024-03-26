n, k = map(int, input().split())
a_list = []

for i in range(n):
  a = int(input())
  if (a <= k):
    a_list.append(a)

a_list.sort(reverse=True) # 1000, 500, 100, 50, 10, 5, 1

count = 0
for i in a_list:
  count += (k // i)
  k %= i
  if k <= 0:
    break

print(count)
