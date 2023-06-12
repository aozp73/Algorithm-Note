# 입력 : 집의 개수, 공유기의 개수
n, c = list(map(int, input().split()))

# 입력 : 각 집의 좌표 정보
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행 전 정렬

start = 1 # start : 가능한 최소 거리
end = array[-1] - array[0] # end : 가능한 최대 거리
res = 0 # 결과값 저장

while(start <= end):
    mid = (start + end) // 2
    value = array[0] # 설치할 때마다의 좌표 저장
    cnt = 1 # 공유기 개수
    
    # 인접 최소 거리를 조절하면서 공유기 설치
    for i in range(1, n): 
        # 현재 최소 거리에 만족하면 공유기 설치
        if array[i] >= value + mid:
            value = array[i]
            cnt += 1
        # C개 이상 공유기 설치 가능하다면, 최소 거리 mid 증가
    if cnt >= c:
        start = mid + 1
        res = mid
    # C개 미만 설치될 경우 최소 거리 mid 감소
    else:
        end = mid - 1
    
print(res)