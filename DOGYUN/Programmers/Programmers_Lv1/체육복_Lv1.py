# 학생들의 번호는 체격 순으로 매겨져 있음
# 바로 앞번호 혹은 뒷번호에게만 여분의 체육복 빌려줄 수 있음
# 최대한 많은 학생이 체육복을 받을 수 있도록
# n : 전체 학생 수 / lost : 체육복을 도난당한 학생들 / reserve : 여벌의 체육복을 가져온 학생 번호
# 체육수업을 들을 수 있는 학생의 수의 최댓값 return

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    reserve_lost_set = lost_set & reserve_set
    
    lost_set -= reserve_lost_set
    reserve_set -= reserve_lost_set
    
    for i in reserve_set:
      if i-1 in lost_set:
        print(lost_set)
        lost_set -= {i-1}
      elif i+1 in lost_set:
        print(lost_set)
        lost_set -= {i+1}
        
    print(lost_set)
    
    return n - len(lost_set)
  
print(solution(5, [2, 4], [1, 3, 5]))