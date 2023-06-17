def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [0] * (n + 1)

# edges 간선정보
edges = []
# res 최종 비용
res = 0

for i in range(1, n + 1):
    parent[i] = i
    
for _ in range(m):
    x, y, z = map(int, input().split())
    # z가 튜플의 첫번째 원소 : 비용순으로 정렬하여 최소 신장 트리 진행
    edges.append((z, x, y))

edges.sort()
# 모든 간선의 비용 합
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost
    
    # 사이클이 발생하지 않는 경우에만 집합 합치기
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        
print(total - res)
    