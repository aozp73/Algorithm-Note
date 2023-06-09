from collections import deque

# 도시 개수 / 도로 개수 / 거리 정보 / 출발 도시 번호
n, m, k, x = map(int, input().split())
# 생성 : 2차원 리스트 (연결 및 간선정보 입력용도) 
graph = [[] for _ in range(n + 1)]

# 연결 및 간선정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 생성 : 1차원 리스트 (노드간 최단거리 갱신 테이블)
distance = [-1] * (n + 1)
# 출발 도시 -> 출발 도시 거리 0 세팅
distance[x] = 0

# x를 원소로 가지는 deque 생성하여 변수 q가 참조
q = deque([x])
while q:
    now = q.popleft()
    
    # 현재 루프의 도시에서 이동할 수 있는 모든 인접 도시 확인
    for near_node in graph[now]:
        # 방문하지 않은 도시라면
        if distance[near_node] == -1:
            # 최단 거리 갱신 (이전까지의 거리 + 간선 거리)
            distance[near_node] = distance[now] + 1
            q.append(near_node)
           
# 최단 거리 테이블을 확인하여 거리가 k인 도시 확인 후, 출력 
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 최단 거리가 주어진 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)