# 추월을 한 선수의 이름을 부름 "2등 -> 1등" 이면 "2등의 이름" 부름
# players: 선수들의 등수에 따른 이름 배열
# callings: 해설진이 이름을 부른 배열
# answer: 경주가 끝났을 때 순서 배열
# callings 배열 돌면서, players에 해당 이름을 찾아서 한 칸 앞으로 옮김 -> 배열을 다 돌면 players return

def solution(players, callings):
  answer = []
  
  index = {i: player for i, player in enumerate(players)} # 등수: 선수
  player = {player: i for i, player in enumerate(players)} # 선수: 등수
    
  for i in callings: # kai
    loc = player[i] # 4등
    loc2 = loc-1 # 3등
    player2 = index[loc2] # poe
    
    index[loc] = player2
    index[loc2] = i
    
    player[i] = loc2
    player[player2] = loc

  return list(index.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))