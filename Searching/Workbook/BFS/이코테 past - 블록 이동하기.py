from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 현재 위치 기준, 비용 1로 이동 가능한 위치 저장
    pos = list(pos) # 집합 -> 리스트 변환 (집합: in으로 목표 좌표 검색)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1]   , pos[1][0], pos[1][1]

    # 1. 상, 하, 좌, 우로 이동하는 경우 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
         # 이동하고자 하는 곳이 비어있다면, 이동 가능 리스트에 추가
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 2. 가로로 놓여있을 때 회전하는 경우 처리
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽 또는 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                # 회전 가능하다면, 이동 가능 리스트에 추가
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 3. 세로로 놓여있을 때 회전하는 경우 처리
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽 또는 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                # 회전 가능하다면, 이동 가능 리스트에 추가
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    # 진행을 편하게 하기 위해 외각에 벽을 두어 진행 (가로 2줄, 세로 2줄 추가)
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    # BFS 진행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 각 진행에서 시작 위치
    q.append((pos, 0)) # 시작위치, 해당 위치까지의 최단 비용
    visited.append(pos) # 방문 처리
    
    while q:
        pos, cost = q.popleft()
        # 목표 지점에 도착했다면, 결과 return
        if(n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            # 방문한적 없는 곳이라면, 다음 진행을 위해 큐에 넣고 비용 1 증가
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

