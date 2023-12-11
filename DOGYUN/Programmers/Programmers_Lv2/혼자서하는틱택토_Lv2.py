# board로 들어오는 틱택토 게임판
# 제대로 룰을 지켰으면 1, 아니면 0을 return

def solution(board):
  start_board = ''.join(board)
  valid = start_board.count('O') - start_board.count('X')
  
  if valid not in [0, 1]:
    return 0
  
  col = list(zip(*board))
  o_success = 0
  x_success = 0
  for i in range(3):
    if col[i].count('O') == 3 or board[i].count('O') == 3:
      o_success += 1
    if col[i].count('X') == 3 or board[i].count('X') == 3:
      x_success += 1
  
  for i in range(0, 3, 2):
    if (board[0][i] == board[1][1] == board[2][2-i] == 'O'):
      o_success += 1
    if (board[0][i] == board[1][1] == board[2][2-i] == 'X'):
      x_success += 1
  
  if o_success and x_success:
    return 0
  if o_success == 1 and valid == 0:
    return 0
  if x_success == 1 and valid >= 1:
    return 0
  
  return 1
  
print(solution(["O.X", ".O.", "..X"]))