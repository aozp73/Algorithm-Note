n = int(input())
data = list(map(int, input().split()))

# 순서 뒤집기 ('최장 증가 부분 수열' 문제로 변환)
data.reverse()

# dp 테이블 모든 원소 1로 초기화
dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
    # 체크하는 원소 보다 작은 이전 값들 모두 순회
    for j in range(0, i):
        if data[j] < data[i]:
            # 각 원소들을 최장 경우의 수로 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 되는 최소 수 출력
print(n - max(dp))