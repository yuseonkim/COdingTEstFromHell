n = int(input())
lopes = []
for _ in range(n):
  lopes.append(int(input()))

lopes.sort(reverse=True)
results = []

for j in range(n):
  results.append(lopes[j]*(j+1))

print(max(results))