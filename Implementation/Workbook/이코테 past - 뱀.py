n = int(input())
k = int(input())

# data : 맵 정보
data = [[0] * (n + 1) for _ in range(n + 1)]
# info : 방향 회전 입력 값
info = []

# 사과 입력 받기, 맵 정보 리스트에 1 세팅
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 입력값 세팅
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 시계방향 : index 0(동), 1(남), 2(서), 3(북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 회전 처리
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2 # 뱀이 있는 곳은 2로 표시
    direction = 0 # 문제에서 시작 방향은 동쪽
    time = 0
    index = 0 # 회전 처리에 사용되는 변수
    q = [(x, y)] # 사과가 없을 경우, 꼬리를 자르기 위한 저장용 리스트
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과 없을 경우
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0) # 꼬리 정보 확인
                data[px][py] = 0 # 꼬리 제거
            # 사과 있을 경우
            if data[nx][ny] == 1:
                data[nx][ny] == 2
                q.append((nx, ny))
        # 벽, 몸에 부딪힐 경우
        else:
            time +=1
            break
        x, y = nx, ny
        time += 1
        # 가장 가까운 시간을 index로 판단하여 회전 처리
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())