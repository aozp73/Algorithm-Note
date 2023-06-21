'그리디, 모험가 길드'
# n = int(input())
# data = list(map(int, input().split()))

# data.sort()

# people_cnt = 0
# group_cnt = 0

# for i in range(n):
#     people_cnt += 1
#     if people_cnt >= data[i]:
#         group_cnt += 1
#         people_cnt = 0

# print(group_cnt)

'그리디, 곱하기 혹은 더하기'
# data = input()

# res = int(data[0])
# for i in range(1, len(data)):
#     next_num = int(data[i])
#     if next_num <= 1 or res <= 1:
#         res += next_num
#     else:
#         res *= next_num
        
# print(res)

'그리디, 문자열 뒤집기'
# data = input()
# now_num = data[0]
# zero_cnt = 0
# one_cnt = 0

# for i in range(1, len(data)):
#     if now_num != data[i] and now_num == '0':
#         zero_cnt += 1
#         now_num = '1'
#     elif now_num != data[i] and now_num == '1':
#         one_cnt += 1
#         now_num = '0'

# if now_num == '1':
#     one_cnt += 1
# else:
#     zero_cnt += 1

# print(min(zero_cnt, one_cnt))

'그리디, 만들 수 없는 금액'
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for x in data:
#     if target < x:
#         break
#     target += x
# print(target)

'그리디, 볼링공 고르기'
# n, m = map(int, input().split())
# data = [0] * 11
# check = set()
# for x in (input().split()):
#     x = int(x)
#     data[x] += 1
#     check.add(x)

# cnt = 0
# check = list(check)
# for i in range(len(check) - 1):
#     for j in range(i + 1, len(check)):
#      cnt += data[check[i]] * data[check[j]]

# print(cnt)

'그리디, 무지의 먹방 라이브'

import heapq
def solution(food_times, k):
    
    # 초기 입력 상태 확인 - 모든 음식 시간 <-> 정전 시간 비교
    if sum(food_times) <= k:
        return -1
 
    # 우선순위 큐 활용 (최소힙, 가장 시간이 적게 걸리는 음식부터 처리)   
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    now_time = 0 # 현재까지 걸린 시간
    previous_food_time = 0 # 이전 음식 시간 (동일한 1초 단위 이므로, 음식 수로 생각해도 좋음)
    remainder_food_cnt = len(food_times) # 남은 음식 개수 (우선순위 큐 크기)
    
    # x : 현재 걸린 시간 + (현재 가장 빨리 없어지는 음식의 시간 - 직전에 다 먹은 음식 시간) * 남은 음식 수
    # 직전에 음식을 다 먹었을 경우 남은 모든 음식도 해당 시간만큼 차감해야함 
    # x가 k보다 작을 동안만 반복하고, 클 경우 남은 음식끼리 나머지 연산자를 통해 비교
    while now_time + ((q[0][0] - previous_food_time) * remainder_food_cnt) <= k:
        now_food_time = heapq.heappop(q)[0]
        now_time += (now_food_time - previous_food_time) * remainder_food_cnt
        remainder_food_cnt -= 1
        previous_food_time = now_food_time
        
    # 남은 음식을 번호 순으로 정렬
    res = sorted(q, key=lambda x: x[1])
    # 나머지 연산을 통해 정전 후 순번의 음식번호 계산
    return res[(k - now_time) % remainder_food_cnt][1]