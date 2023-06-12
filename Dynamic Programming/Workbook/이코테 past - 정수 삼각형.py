n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))
    
# 2번째 행부터 내려가면서 DP 테이블 갱신
for i in range(1, n):
    for j in range (i + 1):
        # 왼쪽 위에서 내려오는 경우 (왼쪽 대각선)
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        
        # 바로 위에서 내려오는 경우 (오른쪽 대각선)
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
            
        # 두 경우 중 최대를 저장
        dp[i][j] = dp[i][j] + max(up_left, up)
        
print(max(dp[n - 1]))