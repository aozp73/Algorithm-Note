'그리디, 거스럼돈' 
# import sys
# input = sys.stdin.readline

# n = int(input())
# coin_types = [500, 100, 50, 10]

# cnt = 0
# for coin in coin_types:
#     cnt += n // coin
#     n %= coin
    
# print(cnt)

'그리디, 큰 수의 법칙 ' 
# import sys
# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort(reverse=True)

# q = m // (k + 1)
# r = m % (k + 1)

# res = 0
# res += (q * k * data[0] + q * data[1])

# if r != 0:
#         res += (r * data[0])

# print(res)

'그리디, 숫자 카드 게임'
# list내 최솟값 min()함수 활용 가능
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())

# store_data = []
# index = 0

# for _ in range(n):
#    min_value = 10001
#    data = list(map(int, input().split()))
#    for i in range(m):
#       if data[i] < min_value:
#          min_value = data[i]
#    store_data.append(min_value)
   
# store_data.sort()

# print(store_data[n-1])

'그리드, 1이 될 때까지'
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())

# cnt = 0

# while True:
#   target = (n // k) * k
#   cnt += (n - target)
#   n = target
  
#   if n < k:
#      break
  
#   cnt += 1
#   n //= k
  
# cnt += n - 1
# print(cnt)

'구현, 상하좌우'
# n = int(input())
# data_list = input().split()

#  # L R U D
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_tpyes = ['L', 'R', 'U', 'D']
# x, y = 1, 1
# nx, ny = 0, 0
# for data in data_list:
#    for i in range(4):
#       if data == move_tpyes[i]:
#          nx = x + dx[i]
#          ny = y + dy[i]
      
#    if 1 <= nx <= n and 1 <= ny <= n:
#       x, y = nx, ny
      
# print(x, y)

'구현, 시각'
# n = int(input())

# cnt = 0
# for h in range(n + 1):
#    for m in range(60):
#       for s in range(60):
#          if '3' in str(h) + str(m) + str(s):
#             cnt += 1
            
# print(cnt)

'구현, 왕실의 나이트'
# data = input()
# x = int(data[1])
# y = ord(data[0]) - ord('a') + 1
# cnt = 0
# move_types = [(-2, -1), (-2, 1),  (-1, 2),  (1, 2),  (2, 1),  (2, -1),  (1, -2),  (-1, -2)]
# for i in range(len(move_types)):
#     nx = x + move_types[i][0]
#     ny = y + move_types[i][1]
    
#     if 1 <= nx <= 8 and 1 <= ny <= 8:
#         cnt += 1
        
# print(cnt)

'구현, 게임 개발'
# n, m = list(map(int, input().split()))

# # 동 북 서 남
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# x, y, direction = map(int, input().split())
# maps = []
# for _ in range(n):
#     maps.append(list(map(int, input().split())))

# visited = [[0] * m for _ in range(n)]
# visited[x][y] = 1

# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# cnt = 1
# turn_time = 0
# while True:
#     turn_left()
    
#     nx = x + dx[direction]
#     ny = y + dy[direction]
    
#     if maps[nx][ny] == 0 and visited[nx][ny] == 0:
#         visited[nx][ny] = 1
#         x, y = nx, ny
#         cnt += 1
#         turn_time = 0
        
#         continue
#     else:
#         turn_time += 1
    
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
        
#         if maps[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0
        
# print(cnt)
    
'탐색, 음료수 얼려 먹기 TP'
# n, m = map(int, input().split())
# maps = []
# for _ in range(n):
#     maps.append(list(map(int, input().split())))

# def dfs(x, y):
#     if not ( -1 < x < n and -1 < y < m):
#         return False
    
#     if maps[x][y] == 0:
#         maps[x][y] = 1
#         # 동 남 서 북 재귀 호출
#         dfs(x, y+1)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x-1, y)
#         return True
    
#     return False
        
# cnt = 0
# for i in range(n):
#     for j in range(m):
        
#         if dfs(i, j) == True:
#             cnt += 1
            
# print(cnt)

'탐색, 미로 탈출 TP'
# from collections import deque

# n, m = map(int, input().split())
# maps = []
# for _ in range(n):
#     maps.append(list(map(int, input())))
# # 동 남 서 북
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
    
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if not (0 <= nx < n and 0 <= ny < m):
#                 continue
#             if maps[nx][ny] == 0:
#                 continue
            
#             if maps[nx][ny] == 1:
#                 maps[nx][ny] = maps[x][y] + 1
#                 queue.append((nx, ny))
                
#     return maps[n - 1][m - 1]
    
# print(bfs(0, 0))
                
    
'이진 탐색, 부품 찾기'
# n = int(input())
# sell_data = list(map(int, input().split()))
# m = int(input())
# search_data = list(map(int, input().split()))

# def binary_search(sell_data, target, start, end):
#     if start > end:
#         return 'no'
#     mid = (start + end) // 2
    
#     if sell_data[mid] == target:
#         return 'yes'
#     elif sell_data[mid] > target:
#         return binary_search(sell_data, target, start, mid-1)
#     else:
#         return binary_search(sell_data, target, mid+1, end)
    
# for k in search_data:
#     print(binary_search(sell_data, k, 0, n-1))

# n = int(input())
# array = [0] * 10001

# for i in input().split():
#     array[int(i)] = 1
    
# m = int(input())
# for k in input().split():
#     if array[int(k)] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

'이진 탐색, 떡볶이 떡 만들기 TP'
# n, m = list(map(int, input().split()))
# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# res = 0
# while(start <= end):
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         if x > mid:
#             total += (x - mid)
    
#     if total < m:
#         end = mid - 1
#     else:
#         res = mid
#         start = mid + 1
        
# print(res)

'다이나믹, 피보나치'
# 일반 재귀
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)

# print(fibo(4))

# 탑다운 - 메모제이션 
# d = [0] * 100

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
    
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# 보텀업 - 반복
# d = [0] * 100

# d[1] = 1
# d[2] = 2
# n = 99

# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]

# print(d[n])

'다이나믹, 1로 만들기 TP'
# x = int(input())

# d = [0] * 30001

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1 
    
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2])
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3])
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5])
        
# print(d[x])

'다이나믹, 개미 전사'
# n = int(input())
# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0], array[1])

# for i in range(2, n): 
#     d[i] = max(d[i-1], d[i-2]+array[i])
    
# print(d[n - 1])

'다이나믹, 바닥 공사 TP'
# n = int(input())

# d = [0] * 1001

# d[1] = 1
# d[2] = 3
# for i in range(3, n+1):
#     d[i] = (d[i-1] + d[i-2] * 2) % 796796

# print(d[n])

'다이나믹, 효율적인 화폐 구성 TP'
# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(int(input()))

# d = [10001] * (m + 1)

# for i in range(n):
#     for j in range(array[i], m + 1):
#         d[j] = min(d[j], d[j - array[i]] + 1)

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])
    
    