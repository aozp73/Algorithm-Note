n = int(input()) # 전체 상담 개수
t = [] # 각 상담 완료에 걸리는 시간
p = [] # 각 상담 완료 시 받는 금액 
dp = [0] * (n + 1) # 1차원 DP 테이블
max_value = 0

# 시간, 금액 값 입력
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트의 뒤에서 부터 확인 (n - 1 ~ 0, 끝 값 포함 x)
for i in range(n - 1, -1, -1):
    time = t[i] + i
    
    # 상담이 퇴사일 이전에 끝나는 경우
    if time <= n:
        # 현재까지 최고 이익 계산 후 입력
        # 만약 해당 일에 시작하는 것보다 이전 값이 더 크면 이전 값 입력
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        # 해당 일에 시작하지 못한다면 이전 값 입력
        dp[i] = max_value
        
print(max_value)