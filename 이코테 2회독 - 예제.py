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
    
