from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n): # 행
    data = list(map(int, input().split()))
    for c in range(n): # 열
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
            
# chicken 리스트에서 m개를 뽑는 조합을 뽑아서 리스트로 저장
candidates = list(combinations(chicken, m))

def distance_cal(candidate):
    res = 0
    # 1. 각 집에서의
    for hx, hy in house:
        temp = 1e9
        # 2. 각 치킨집 까지
        for cs, cy in candidate:
            # 3. 거리 중 가장 가까운 치킨집과의 거리 저장
            temp = min(temp, abs(hx - cs) + abs(hy - cy))
        
        # 모든 집에서의 최소 치킨거리 저장 (도시의 치킨 거리)
        res += temp
    
    return res

res = 1e9
for candidate in candidates:
    # 각 조합에서 도시의 치킨거리가 가장 짧은 경우 계산
    res = min(res, distance_cal(candidate))
    
print(res)