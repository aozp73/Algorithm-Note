from collections import deque
# 인접 국가 인구 차 확인할 때 BFS에서 활용

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    # 연합 완성 후, 인구 분배에서 도시 좌표 불러올 때 사용
    united = []
    united.append((x, y))
    
    # BFS 수행에서 조건에 맞는 인접도시 연합 꾸릴 때 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 연합 조건에 부합한다면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    # 다음 탐색을 위해 q에 넣고
                    q.append((nx, ny))
                    # 해당 회차 방문했다는 체크
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // cnt

# main 부분
total_cnt = 0
# 인구 이동 최대 경우의 수까지 반복 (모든 도시가 독립적)
while True:
    # 해당 인구이동 회차에서 처리된 나라 체크용도
    union = [[-1] * n for _ in range(n)]
    # 인구 이동을 최대한 진행하여 모든 도시에서 인구이동이 불가능할 때 종료 
    index = 0
    for i in range(n):
        for j in range(n):
            # 해당 회차에서 처리되지 않았다면,
            if union[i][j] == -1:
                process(i, j, index)
                # 마지막 회차 체크용
                index += 1
                
    if index == n * n:
        break
    total_cnt += 1
    
print(total_cnt)