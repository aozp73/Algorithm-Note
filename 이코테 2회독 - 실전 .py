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

'구현, 럭키 스트레이트'
# data = input()
# half_len = len(data) // 2

# left_sum = 0
# right_sum = 0
# for i in range(half_len):
#     left_sum += int(data[i])
# for j in range(half_len, 2 * half_len):
#     right_sum += int(data[j])

# if left_sum == right_sum:
#     print('LUCKY')
# else:
#     print('READY')


'구현, 문자열 재정렬'
# data = input()
# list = []
# cnt = 0
# for i in data:
#     if i.isalpha():
#         list.append(i)
#     else:
#         cnt += int(i)

# list.sort()
# if cnt != 0:
#     list.append(cnt)

# for i in list:
#     print(i, end='') 
# # print(''.join(list))

'구현, 문자열 압축 DP'
# def solution(s):
#     answer = len(s)
    
#     for step in range(1, len(s) // 2 + 1):
#         compressed = ""
#         prev = s[0:step]
#         cnt = 1
        
#         for j in range(step, len(s), step):
#             if prev == s[j:j + step]:
#                 cnt += 1
#             else:
#                 compressed += str(cnt) + prev if cnt >= 2 else prev
#                 prev = s[j:j + step]
#                 cnt = 1
#         compressed += str(cnt) + prev if cnt >= 2 else prev
#         answer = min(answer, len(compressed))
        
#     return answer

'구현, 자물쇠와 열쇠'
# def rotate_90_degree(a):
#     # 회전한 리스트를 사전에 생성하기 위해 행, 열의 길이 계산
#     n = len(a)
#     m = len(a[0])
#     res = [[0] * n for _ in range(m)]

#     for i in range(n):
#         for j in range(m):
#             res[j][n - i - 1] = a[i][j]
#     return res

# def unlock_check(new_lock, m, n):
#     for i in range(m, m + n):
#         for j in range(m, m + n):
#             if new_lock[i][j] != 1:
#                 return False
    
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
    
#     new_lock = [[0] * (n + 2 * m) for _ in range(n + 2 * m)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+m][j+m] = lock[i][j]
    
#     for rotate in range(4):
#         key = rotate_90_degree(key)
        
#         for i in range(1, n + m):
#             for j in range(1, n + m):

#                 for x in range(m):
#                     for y in range(m):
#                         new_lock[i + x][j + y] += key[x][y]
                
#                 if unlock_check(new_lock, m, n):
#                     return True
                
#                 for x in range(m):
#                     for y in range(m):
#                         new_lock[i + x][j + y] -= key[x][y]
            
#     return False

'구현, 뱀'
# from collections import deque

# n = int(input())
# k = int(input())

# maps = [[0] * (n + 1) for _ in range (n + 1)] # 맵 기본 0
# for _ in range(k):
#     x, y = map(int, input().split())
#     maps[x][y] = 2 # 사과 있으면 2 
    
# l = int(input())
# move_info = []
# for _ in range(l):
#     time, direction = input().split()
#     move_info.append((int(time), direction))

# # 동 남 북 서
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
    
# def turn_direction(direction, move_info):
#     if move_info == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# def simulate():
#     x, y = 1, 1
#     maps[x][y] = 1 # 뱀이 차지하는 곳 1
#     queue = deque()
#     queue.append((x, y)) # 뱀의 꼬리 위치 저장
    
#     time_now = 0
#     time_index = 0
#     direction = 0

#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]
        
#         # 이동 한 위치가 맵 밖, 자기 몸이 아닐 경우
#         if 1 <= nx <= n and 1 <= ny <= n and maps[nx][ny] != 1:
#             # 사과가 있는 경우
#             if maps[nx][ny] == 2:
#                 maps[nx][ny] = 1
#                 queue.append((nx, ny))
                
#             if maps[nx][ny] == 0:
#                 maps[nx][ny] = 1
#                 queue.append((nx, ny))
#                 # 꼬리 이동
#                 a, b = queue.popleft()
#                 maps[a][b] = 0
#         # 벽이나 꼬리에 부딪힌 경우   
#         else:
#             time_now += 1
#             break
        
#         x, y = nx, ny
#         time_now += 1
        
#         # 도착한 곳 회전여부 확인
#         if time_index < l and time_now == move_info[time_index][0]:
#             direction = turn_direction(direction, move_info[time_index][1])
#             time_index += 1
            
#     return time_now
            
# print(simulate())
            
'구현, 기둥과 보 설치'
# def frame_check(answer):

#     for x, y, a in answer:
#         # 기둥일 경우
#         if a == 0:
#             if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y - 1, 0] in answer:
#                 continue
#             else:
#                 return False
        
#         # 보일 경우
#         elif a == 1:
#             if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
#                 continue
#             else:
#                 return False
#     return True
            
# def solution(n, build_frame):
#     answer = []
#     for x, y, a, b in build_frame:
#         # 설치
#         if b == 1:
#             answer.append([x, y, a])
#             if not frame_check(answer):
#                 answer.remove([x, y, a])
            
#         # 삭제
#         if b == 0:
#             answer.remove([x, y, a])
#             if not frame_check(answer):
#                 answer.append([x, y, a])

#     return sorted(answer)

'구현, 치킨 배달 TP'
# from itertools import combinations

# n, m = map(int, input().split())

# house = []
# chicken = []
# for i in range(n):
#     map_data = list(map(int, input().split()))
#     for j in range(n):
#         if map_data[j] == 1:
#             house.append((i, j))
#         elif map_data[j] == 2:
#             chicken.append((i, j))
            
# candidates = list(combinations(chicken, m))

# def city_chicken_distance(candidate):
#     city_chicken_distance_val = 0

#     for h1, h2 in house:
#         chicken_distance_val = int(1e9)
#         for c1, c2  in candidate:
#             chicken_distance_val = min(chicken_distance_val, abs(h1 - c1) + abs(h2 - c2))
        
#         city_chicken_distance_val += chicken_distance_val
        
#     return city_chicken_distance_val

# res = int(1e9)
# for candidate in candidates:
#     res = min(res, city_chicken_distance(candidate))
    
# print(res)

'구현, 외벽 점검 TP'
# from itertools import permutations
# def solution(n, weak, dist):
#     length = len(weak)
#     for i in range(length):
#         weak.append(weak[i] + n)
        
#     answer = len(dist) + 1
    
#     for start in range(length):

#         for friends in list(permutations(dist, len(dist))):
#             cnt = 1
            
#             last_check = weak[start] + friends[cnt - 1]
            
#             for index in range(start, start + length):
                
#                 if last_check < weak[index]:
#                     cnt += 1
                    
#                     if cnt > len(dist):
#                         break
                    
#                     last_check = weak[index] + friends[cnt - 1]
        
#             answer = min(answer, cnt)
    
#     if answer == len(dist) + 1:
#         return -1
#     return answer


'DFS/BFS, 특정 거리의 도시 찾기 TP'
# from collections import deque

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
    
# distance = [-1] * (n + 1)
# distance[x] = 0

# q = deque([x])
# while q:
#     now = q.popleft()
    
#     for near_node in graph[now]:
#         if near_node != -1:
#             distance[near_node] = distance[now] + 1
#             q.append(near_node)
            
# check = False
# for i in (1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True
        
# if check == False:
#     print(-1)

'BFS/DFS, 연구소 TP'
# from copy import deepcopy
# from itertools import combinations

# n, m = map(int, input().split())

# data = []

# temp = [[0] * m for _ in range(n)]
# virus_posi = []
# no_wall = []

# for i in range(n):
#     data.append(list(map(int, input().split())))
#     for j in range(m):
#         check = data[i][j]
#         if check == 2:
#             virus_posi.append((i, j))
#         elif check == 0:
#             no_wall.append((i, j))

# total_combi = list(combinations(no_wall, 3))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# res = 0

# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < n and 0 <= ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)
                
# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score

# def dfs():
#     global res
    
#     for combi in total_combi:
#         temp = deepcopy(data)
        
#         for x, y in combi:
#             temp[x][y] = 1
            
#         for x, y in virus_posi:
#             virus(x, y)
            
#         res = max(res, get_score())
        
# dfs()
# print(res)

'BFS/DFS 경쟁적 전염 TP'
# from collections import deque

# n, k = map(int, input().split())

# graph = []
# data = []

# for i in range(n):
#     graph.append(list(map(int, input().split())))
    
#     for j in range(n):
#         if graph[i][j] != 0:
#             data.append((graph[i][j], 0, i, j))
    
# data.sort()
# q = deque(data)

# target_s, target_x, target_y = map(int, input().split())

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# while q:
#     virus_num, s, x, y = q.popleft()
    
#     if s == target_s:
#         break
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < n and 0 <= ny < n:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus_num
                
#                 q.append((virus_num, s+1, nx, ny))
                
# print(graph[target_x - 1][target_y - 1])

'DFS/BFS 괄호 변환'
def cal_1(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        
        if cnt == 0:
            return i
        
    return 0

def cal_2(u):
    cnt = 0
    for i in u:
        if i == '(':
            cnt += 1

        else:
            if cnt == 0:
              return False
            cnt -= 1
            
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    
    balanced_index = cal_1(p)
    u = p[:balanced_index + 1]
    v = p[balanced_index + 1:]
    
    if cal_2(u):
        answer = u + solution(v)
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        
        answer += "".join(u)
        
    return answer
    
