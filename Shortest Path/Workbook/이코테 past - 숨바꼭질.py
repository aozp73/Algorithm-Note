import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n 헛간 개수(노드), b 통로 개수(간선)
n, m = map(int, input().split())
# 시작노드 1
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# 입력: 간선 정보
for _ in range(m):
    a, b = map(int, input().split())
    # 무방향(양방향) -> 방향 그래프로 변경
    graph[a].append((b, 1))
    graph[b].append((a, 1))
    
def dijkstra(start):
    q = []
    
    # 반복문 시작 전 입력값에 따른 시작 노드 세팅
    # 시작 노드에서의 거리 0 세팅하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # 큐가 비어있지 않다면 계속 진행
    # (초기에 무한 거리로 세팅되어 있으므로, 모든 노드 방문함)
    while q:
        # 현재 탐색하는 노드를 꺼내서
        dist, now = heapq.heappop(q)
        # 만약 큐 우선순위에 밀려나있는 상태고,
        # 새로 들어온 원소에 의해 최단거리가 갱신되었다면
        # 해당 원소는 무시하고 지나감
        if distance[now] < dist:
            continue

        # 입력값에 따라 현재 노드와 연결된 모드 노드 순회
        for i in graph[now]:
            # 현재 노드를 통해 연결된 노드로 가는 비용 저장
            cost = dist + i[1]
            
            # 만약, 최단거리 테이블에 기록된 거리보다 
            # 현재 계산된 거리가 짧다면
            if cost < distance[i[0]]:
                # 해당 노드까지의 최단거리를 갱신하고
                distance[i[0]] = cost
                # 최단거리 이므로 해당 노드에서 이어진 노드들의
                # 최단거리 계산을 위해 큐에 넣음
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
        
print(max_node, max_distance, len(result))