
'''
[Input Example 1]
5 8 3
2 4 5 4 6
[Output Example 1]
46
'''


# 1. 단순 풀이

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-2]
second = data[n-1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
     break
    result += second
    m -= 1

print(result)


##########################################


# 2. 연산횟수 간소화

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력