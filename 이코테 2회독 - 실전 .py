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
# def cal_1(p):
#     cnt = 0
#     for i in range(len(p)):
#         if p[i] == '(':
#             cnt += 1
#         elif p[i] == ')':
#             cnt -= 1
        
#         if cnt == 0:
#             return i
        
#     return 0

# def cal_2(u):
#     cnt = 0
#     for i in u:
#         if i == '(':
#             cnt += 1

#         else:
#             if cnt == 0:
#               return False
#             cnt -= 1
            
#     return True

# def solution(p):
#     answer = ''
#     if p == '':
#         return answer
    
#     balanced_index = cal_1(p)
#     u = p[:balanced_index + 1]
#     v = p[balanced_index + 1:]
    
#     if cal_2(u):
#         answer = u + solution(v)
#     else :
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#         u = list(u[1:-1])
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
        
#         answer += "".join(u)
        
#     return answer

'BFS/DFS, 연산자 끼워넣기 TP'
## 순열 라이브러리
# from itertools import permutations

# n = int(input())
# num = list(map(int, input().split()))
# input_oper = list(map(int, input().split()))
# oper = ['+', '-', '*', '//']

# oper_data = []
# for i in range(len(input_oper)):
#     for _ in range(input_oper[i]):
#         oper_data.append(oper[i])
    
# max_val = -1e9-1
# min_val = 1e9+1
    
# def sol():
#     global max_val, min_val
#     for case in set(permutations(oper_data, n - 1)):
#         res = num[0]
        
#         for k in range(1, n):
#             if case[k-1] == '+':
#                 res += num[k]
#             elif case[k-1] == '-':
#                 res -= num[k]
#             elif case[k-1] == '*':
#                 res *= num[k]
#             elif case[k-1] == '//':
#                 if res < 0:
#                     res = -1 * (-res // num[k])
#                 else:
#                     res = res // num[k]
#         if res > max_val:
#             max_val = max(res, max_val)
#         if res < min_val:
#             min_val = min(res, min_val)
        
# sol()
# print(max_val)
# print(min_val)

## DFS (백 트래킹)
# from itertools import permutations

# n = int(input())
# m = n - 1 
# num = list(map(int, input().split()))
# plus, minus, multi, divide = list(map(int, input().split()))
# oper = ['+', '-', '*', '//']

# max_val = -1e9-1
# min_val = 1e9+1


# def dfs(m, now):
#     global max_val, min_val, plus, minus, multi, divide
    
#     if m == n:
#         max_val = max(max_val, now)
#         min_val = min(min_val, now)
#         return
    
#     if plus > 0:
#         plus -= 1
#         dfs(m + 1, now + num[m])
#         plus += 1
#     if minus > 0:
#         minus -= 1
#         dfs(m + 1, now - num[m])
#         minus += 1
#     if multi > 0:
#         multi -= 1
#         dfs(m + 1, now * num[m])
#         multi += 1
#     if divide > 0:
#         divide -= 1
#         if now < 0:
#           dfs(m + 1, -(-now // num[m]))
#         else:
#           dfs(m + 1, now // num[m])
#         divide += 1

# dfs(1, num[0])
# print(max_val)
# print(min_val)

'BFS/DFS, 감시 피하기'
# from itertools import combinations

# n = int(input())
# spaces = []
# teacher = []
# empty = []

# # 선생님, 빈 공간 위치 저장
# for i in range(n):
#     spaces.append(input().split())    
#     for j in range(n):
#         if spaces[i][j] == 'T':
#             teacher.append((i, j))
#         if spaces[i][j] == 'X':
#             empty.append((i, j))

# def find_bad_student(tx, ty, i):
#     # 동쪽
#     if i == 0:
#         while ty < n - 1:
#             ty += 1
#             if spaces[tx][ty] == 'S':
#                 return True
#             if spaces[tx][ty] == 'O':
#                 return False
        
#     # 남쪽
#     elif i == 1:
#         while tx < n - 1:
#             tx += 1
#             if spaces[tx][ty] == 'S':
#                 return True
#             if spaces[tx][ty] == 'O':
#                 return False
#     # 서쪽
#     elif i == 2:
#         while ty > 0:
#             ty -= 1
#             if spaces[tx][ty] == 'S':
#                 return True
#             if spaces[tx][ty] == 'O':
#                 return False
#     # 북쪽
#     elif i == 3:
#         while tx > 0:
#             tx -= 1
#             if spaces[tx][ty] == 'S':
#                 return True
#             if spaces[tx][ty] == 'O':
#                 return False
        
#     return False
        

# # 빈 공간에 벽 세우는 각각 경우
# def sol():

#     for empty_case in combinations(empty, 3):
#         check = False
#         for ox, oy in empty_case:
#             spaces[ox][oy] = 'O'
        
#         # 각 선생님 마다 동,서,남,북 진행
#         for tx, ty in teacher:
#             for i in range(4):
#                 if find_bad_student(tx, ty, i):
#                     check = True
        
#         for ox, oy in empty_case:
#             spaces[ox][oy] = 'X'
            
#         if not check:
#             return True 
        
# if sol():
#     print("YES")
# else:
#     print("NO")

'BFS/DFS, 인구 이동 TP'
# from collections import deque

# n, l, r = map(int, input().split())
# # 원본 맵 
# maps = []
# for _ in range(n):
#     maps.append(list(map(int, input().split())))
    
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]


# def process(i, j, index):
#     # 계산 정보
#     united = []
#     united.append((i, j))
#     cnt = 1
#     summary = maps[i][j]

#     # 방문 정보
#     union[i][j] = index

#     # BFS 순회
#     q = deque()
#     q.append((i, j))
    
#     while q:
#         x, y = q.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
        
#             if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
#                 if l <= abs(maps[nx][ny] - maps[x][y]) <= r:
#                     united.append((nx, ny))
#                     summary += maps[nx][ny]
#                     cnt += 1
                    
#                     union[nx][ny] = index
                    
#                     q.append((nx, ny))
                    
#     for x, y in united:
#         maps[x][y] = summary // cnt
                    
            
# total_cnt = 0

# while True:
#     union = [[-1] * n for _ in range(n)]
#     index = 0
    
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 process(i, j, index)
                
#                 index += 1
    
#     if index == n * n:
#         break
    
#     total_cnt += 1
    
# print(total_cnt)

'BFS/DFS, 블록 이동 TP'
# from collections import deque

# def get_next_pos(pos, board):
#     next_pos = []
#     pos = list(pos)
#     pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

#     # 상 하 좌 우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     # 1. 상 하 좌 우
#     for i in range(4):
#         pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
#         if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
#             next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
#     # 2. 가로 상태에서 회전
#     if pos1_x == pos2_x:
#         for i in [-1, 1]: # 위쪽 또는 아래쪽으로 회전
#             if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
#                 # 회전 가능하다면, 이동 가능 리스트에 추가
#                 next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
#                 next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    
#     # 3. 세로 상태에서 회전
#     elif pos1_y == pos2_y:
#         for i in [-1, 1]: # 왼쪽 또는 오른쪽으로 회전
#             if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
#                 # 회전 가능하다면, 이동 가능 리스트에 추가
#                 next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
#                 next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    
#     return next_pos


# def solutions(board):
#     n = len(board)
#     new_board = [[1] * (n + 2) for _ in range(n + 2)]
#     for i in range(n):
#         for j in range(n):
#             new_board[i + 1][j + 1] = board[i][j]
            
#     q = deque()
#     visited = []
#     pos = {(1, 1), (1, 2)}
#     q.append((pos, 0))
#     visited.append(pos)
    
#     while q:
#         pos, cost = q.popleft()
#         if(n, n) in pos:
#             return cost
#         for next_pos in get_next_pos(pos, new_board):
#             if next_pos not in visited:
#                 q.append((next_pos, cost + 1))
#                 visited.append(next_pos)
    
#     return 0


'정렬, 국영수'
# n = int(input())

# student_data = []
# for _ in range(n):
#     student_data.append(input().split())
    
# student_data.sort(key=lambda x: ( -int(x[1]), int(x[2]), -int(x[3]), x[0]))

# for student in student_data:
#     print(student[0])

'정렬, 안테나'
# n = int(input())
# house_data = list(map(int, input().split()))
# house_data.sort()

# print(house_data[(n - 1) // 2])

'정렬, 실패율'
# def solution(N, stages):

#     total_people = len(stages)
#     answer = []
#     checks = []
#     for i in range(N + 1):
#         checks.append(0);
#     print(checks)
#     stages.sort()
#     for data in stages[0: total_people - 1]:
#         checks[data] += 1
#     print(checks)

#     for check in checks:
#         answer.append(check // total_people)
#         total_people -= check

#     return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# print(solution(N, stages))

'정렬, 카드 정렬하기 TP'
# import heapq

# n = int(input())

# heap = []
# for i in range(n):
#     data = int(input())
#     heapq.heappush(heap, data)
    
# res = 0

# while len(heap) != 1:
#     one = heapq.heappop(heap)
#     two = heapq.heappop(heap)
#     sum_value = one + two
#     res += sum_value
#     heapq.heappush(heap, sum_value)
    
# print(res)