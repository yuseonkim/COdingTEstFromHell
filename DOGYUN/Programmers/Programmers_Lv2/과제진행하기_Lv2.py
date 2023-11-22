# 과제 계획 세우기
# 시작 시간이 되면 과제 시작
# 기존에 진행 중이던 과제가 있으면 멈추고, 새로운 과제 시작
# 진행 중이던 과제가 끝나면, 잠시 멈춰둔 과제 이어서 시작
# 우선순위 : 새로 시작해야 되는 과제 vs 잠시 멈춰둔 과제 => 새로 시작해야 되는 과제
# 멈춰둔 과제가 여러 개 => 가장 최근에 멈춘 과제
# 과제를 끝낸 순서대로 이름을 배열에 담아 출력
# plans = [name, start, playtime]

# 정렬을 위해 시간 변환
def convertTime(time):
  return int(time[:2])*60 + int(time[3:])

def solution(plans):
    answer = []
    plan_table = {} # 데이터 넣을 곳
    work_list = [] # 작업 중간에 담는 곳
    working = None # 작업 중
    
    for plan in plans:
      plan_table[convertTime(plan[1])] = (plan[0], int(plan[2]))
    
    for time in range(60*24):
      if working:
        working = (working[0], working[1]-1)
        if working[1] == 0:
          answer.append(working[0])
          working = None

      if time in plan_table:
        if working:
          work_list.append(working)
          working = plan_table[time]
        else:
          working = plan_table[time]
      else:
        if not working and work_list:
          working = work_list.pop()     
    return answer
  
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))