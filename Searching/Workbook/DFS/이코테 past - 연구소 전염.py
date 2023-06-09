n, m = map(int, input().split())
# 입력 값을 저장할 초기 맵 리스트 
data = [] 
# 벽을 설치한 각 경우의 수마다 바이러스 전파할 맵 리스트
temp = [[0] * m for _ in range(n)] 

for _ in range(n):
    data.append(list(map(int, input().split())))
    
    
# 북/동/남/서 방향 리스트 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 경우의 수별로 안전 영역 값 갱신하여 저장할 변수
res = 0

def virus(x, y):
    # DFS활용으로 해당 바이러스 좌표에서 벽 내부 모든 공간에 전파
 for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
               
# 바이러스를 뿌린 이후, 해당 회차의 맵에서 안전 영역 크기 계산 
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global res
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                # 해당 경우의 수 그리기 위해 벽 3개를 만든 맵 복사
                temp[i][j] = data[i][j]
            
        # 바이러스 위치를 잡고, 각 바이러스에서 전파 진행   
        for i in range (n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        # 안전 영역 최대값 갱신
        res = max(res, get_score())
        return
    
    # 재귀함수로 2차원 리스트의 빈 공간에 벽 3개를 설치하는 모든 경우의수 완전탐색
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1
                
dfs(0)
print(res)