INF = int(1e9) # 초기 세팅용 : 입력값, 자기자신 외 무한

# n 노드 개수, m 간선 개수
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현) 생성, 모든 값 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
 
# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
 
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # 입력 값 토대로 a에서 b로 가는 비용 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
 
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
# 모두 연결 되어 있다면, 자기 위에 몇명 & 아래에 몇명 있는지 파악 가능
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)