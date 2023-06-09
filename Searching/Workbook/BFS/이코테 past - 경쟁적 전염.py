from collections import deque

n, k = map(int, input().split())

# 전체 맵 정보 담는 리스트
graph = []
# 바이러스 정보 담는 리스트
data = []


# 1. 하나의 행씩 보드 정보 입력
for i in range(n):
    graph.append(list(map(int, input().split())))
    # 2. 입력한 행에서 바이러스가 있다면
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류/초기 시간/좌표 x, 좌표 y 저장
            data.append((graph[i][j], 0, i, j))
           
# 낮은 번호부터 증식하여 겹치는 부분을 처리하므로 정렬 후 deque에 담기 
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나가는 북/동/남/서 4방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# BFS 진행 (가까운 노드 모두 탐색)
while q:
    virus, s, x, y = q.popleft()
    
    # 종료 조건 : q가 비거나, 입력 값 target_s초 되었을 때
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 해당 위치가 n x n 벽 내부의 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 어떠한 바이러스도 방문하지 않았다면
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                # 다음 초에 방문하기 위해 큐 뒷 부분에 넣기
                q.append((virus, s + 1, nx, ny))
                
print(graph[target_x - 1][target_y - 1])