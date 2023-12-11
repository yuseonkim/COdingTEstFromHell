# 한 명의 선수를 제외하고, 모두가 마라톤 완주
# participant : 마라톤에 참여한 선수 명단
# completion : 완주한 선수의 이름이 담긴 명단
# 완주하지 못한 선수의 이름 return

def solution(participant, completion):
    participant_dict = {}
    sumHash = 0
    for part in participant:
      participant_dict[hash(part)] = part
      sumHash += hash(part)
    
    for comp in completion:
      sumHash -= hash(comp)
    
    return participant_dict[sumHash]
  
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))