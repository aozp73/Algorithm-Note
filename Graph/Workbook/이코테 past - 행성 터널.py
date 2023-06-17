# find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# n 노드 개수
n = int(input())
# 부모 테이블 초기화
parent = [0] * (n + 1)

# edges 모든 간선 담을 리스트, res 최종 비용 담을 변수
edges = []
res = 0

for i in range(1, n + 1):
    parent[i] = i
    
x = []
y = []
z = []

# 입력: 모든 노드에 대한 좌표
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[0], i))
    z.append((data[0], i))
    
x.sort()
y.sort()
z.sort()

# 정렬 이후 인접 노드들로부터 간선 정보 추출
for i in range(n - 1):
    # 첫번째 튜플 원소 비용: 비용순으로 정렬하기 위함
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선 비용순 정렬
edges.sort()

# 모든 간선 - 3(n-1)을 하나씩 순회
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우(이미 최소값으로 집합 포함 한 경우) 집합 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        
print(res)