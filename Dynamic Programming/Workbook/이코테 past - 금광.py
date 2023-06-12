# 각 테스트 케이스 별로 for문 진행
for tc in range(int(input())):
    # 입력: n x m 금광 맵 정보
    n, m = map(int, input().split())
    # 입력: 금광 정보
    data = list(map(int, input().split()))

    # 2차원 DP 테이블 초기화
    dp = []
    index = 0
    # 하나의 행 마다
    for i in range(n):
        # 열의 크기만큼 잘라서 저장
        dp.append(data[index:index + m])
        index += m
    
    # 다이나믹 알고리즘
    # 이동 방식 : 열 -> 열 (0번째 열 제외)
    for j in range(1, m):
        # 해당 열의 각 행에서 이전 이동 값 중 최대 저장
        for i in range(n):
            
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            
            # 왼쪽 위에서 오는 경우 (맵을 벗어난 곳에서 오는 값: 0)
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
                
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
                
            # 3가지 경우의수에서 최대값 저장
            dp[i][j] = dp[i][j] + max(left, left_up, left_down)
    
    # 마지막 열에서 최대값 출력 
    res = 0
    for i in range(n):
        res = max(res, dp[i][m - 1])
        
    print(res)