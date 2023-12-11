def solution(n, tops):
    # dp[i][j]: i번째 행에서 j번째 열에 도달하는 경우의 수를 저장하는 2차원 배열
    dp = [[0] * (n+2) for _ in range(n+2)]

    # 초기값 설정
    dp[0][0] = 1
    
    # 행 반복
    for i in range(1, n+2):
        # 열 반복
        for j in range(i+1):
            # 현재 위치에서 정삼각형을 놓을 수 있는 경우
            if tops[j] == 0:
                dp[i][j] += dp[i-1][j]
            # 현재 위치에서 마름모를 놓을 수 있는 경우 (왼쪽 위 대각선 방향)
            if j > 0 and tops[j-1] == 0:
                dp[i][j] += dp[i-1][j-1]
            # 현재 위치에서 마름모를 놓을 수 있는 경우 (오른쪽 위 대각선 방향)
            if j < n and tops[j] == 0:
                dp[i][j] += dp[i-1][j+1]

    # 마지막 행의 모든 값의 합이 정답
    answer = sum(dp[n])
    return answer % 10007
  
print(solution(4, [1, 1, 0, 1]))