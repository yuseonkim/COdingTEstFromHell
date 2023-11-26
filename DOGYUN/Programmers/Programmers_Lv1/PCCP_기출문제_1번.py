# t초동안 1초에 x만큼 체력 회복
# t초 연속으로 붕대를 감는 데 성공하면 추가로 y만큼 체력 회복
# 최대 체력 존재 -> 공격으로 죽으면 -1 return
# 몬스터가 공격하면 풀림 -> 체력 줄어듬 + 붕대 취소
# bandage : [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
# health : 최대 체력
# attacks : [몬스터의 공격 시간, 피해량]
# 모든 공격이 끝난 후 남은 체력 return

def solution(bandage, health, attacks):
    max_health = health
    time = 0
    max_time = attacks[-1][0]
    attack_dict = {}
    for i in attacks:
        attack_dict[i[0]] = i[1]
    continuous_success_time = 0

    while time <= max_time:
        if time in attack_dict:
            health -= attack_dict[time]
            continuous_success_time = 0
            if health <= 0:
                return -1
        else:
            continuous_success_time += 1
            if continuous_success_time < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            else:
                health = health + bandage[1] + bandage[2]
                if health > max_health:
                    health = max_health
                continuous_success_time = 0
        
        time += 1
        
    return health
  
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))