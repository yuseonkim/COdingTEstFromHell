# 각 기사에게 부여된 번호 : 1~number
# 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
# 공격력의 제한수치(limit)보다 큰 공격력의 무기 희망 -> 제한수치 초과 시 정해놓은 power의 공격력 무기 구매
# 공격력 합계

def solution(number, limit, power):
  attack_list = []
  for i in range(1, number+1): 
    primary_count = 0
    for j in range(1, int(i**(1/2))+1):
      if i%j == 0:
        primary_count += 1
        if j**2 != i:
          primary_count += 1
      if primary_count > limit:
        primary_count = power
        break
    
    attack_list.append(primary_count)

  return sum(attack_list)

print(solution(10, 3, 2)) 