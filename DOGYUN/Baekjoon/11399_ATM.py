n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()

sum, count = 0
for i in p_list:
  count += i
  sum += count

print(sum)