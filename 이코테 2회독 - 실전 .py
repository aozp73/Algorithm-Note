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

'그리디, 무지의 먹방 라이브, TP'
# import heapq
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
    
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i + 1))
        
#     now_time = 0
#     previous_food_time = 0
#     remainder_food_cnt = len(food_times)
    
#     while now_time + ((q[0][0] - previous_food_time) * remainder_food_cnt) <= k:
#         now_food_time = heapq.heappop(q)[0]
#         now_time += (now_food_time - previous_food_time) * remainder_food_cnt
#         remainder_food_cnt -= 1
#         previous_food_time = now_food_time
        
#     res = sorted(q, key=lambda x: x[1])
#     return res[(k - now_time) % remainder_food_cnt][1]

