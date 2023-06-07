n, m = map(int, input().split())
data = list(map(int, input().split()))

# 문제에서 주어진 1 ~ 10 무게별 갯수 담는 리스트
array = [0] * 11

for x in data:
    # 각 무게 별 볼링공 개수 카운트
    array[x] += 1

res = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # A가 선택한 종류의 볼링공은 제외
    res += array[i] * n # A가 선택한 종류의 볼링공 갯수 x 남은 볼링공들을 B가 선택하는 경우의 수

print(res)

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if j == i:
#             continue
        
#         if data[i] != data[j]:
#             cnt += 1

# print(cnt // 2)