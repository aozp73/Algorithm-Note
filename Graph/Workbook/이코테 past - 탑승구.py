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

# g 탑승구의 개수
g = int(input())
# p 비행기의 개수
p = int(input())
parent = [0] * (g + 1)

for i in range(1, g + 1):
    parent[i] = i

res = 0
for _ in range(p):
    # 현재 비행기의 탑승 루트노드 확인
    data = find_parent(parent, int(input()))
    # 루트 노드가 0이라면 도킹할 수 있는 모든 탑승구 가득 차 있는 상황 (종료)
    if data == 0:
        break
    # 자리가 있다면 루트 노드의 왼쪽 집합과 합치기
    union_parent(parent, data, data - 1)
    res += 1
 
print(res)   