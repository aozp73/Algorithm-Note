n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액일 경우 탈출
    if target < x:
        break
    # target이 만들 수 있는 금액임을 확인한 이 후임 
    # target += x : 1 ~ (target + x - 1) 까지 만들 수 있다는 의미
    target += x

# 만들 수 없는 금액 출력
print(target)