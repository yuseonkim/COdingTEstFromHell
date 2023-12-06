# brown : Leo가 본 갈색 격자의 수
# yellow : 노란색 격자의 수
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return
# 카펫의 가로 길이는 세로 길이와 같거나 큼

def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, total+1):
      if (total/i) % 1 == 0:
        a = total / i
        if a >= i:
          if a*2 + i*2 == brown + 4:
            return [int(a), i]
  
print(solution(10, 2))

# 10 = 6 + 4
# 6 / 2 = 3 => (2+1) : 곱해서 2가 나옴
# Return [4, 3] : (2+1)에 2씩 더한 것

# 24 = 20 + 4
# 20 / 2 = 10 => (9, 1) / (8, 2) / ... / (5, 5) => (6, 4) : 곱해서 24가 나옴
# Return [8, 6] : (6, 4)에 2씩 더한 것