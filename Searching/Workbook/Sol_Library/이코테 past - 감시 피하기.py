# 복도 내 모든 지점에 벽 설치하는 경우의 수 (조합)
from itertools import combinations

n = int(input()) # 복도 크기
board = [] # 복도 정보 (N x X, 선생님&학생 정보 포함)
teachers = [] # 각 선생님 위치 저장용도
spaces = [] # 모든 빈 공간 위치 저장용도

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 각 선생님 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 빈 공간 위치 저장 (모든 경우의 수에서 각 위치 장애물 설치)
        if board[i][j] == 'X':
            spaces.append((i, j))
            
# 동,서,남,북에서 감시 진행 (학생 발견: True, 미발견: False)
# 각 방향마다 학생이 장애물보다 먼저 발견되면 해당 루프 끝
# 아무것도 발견되지 않았다면 미발견
def watch(x, y, direction):
    # 서쪽 감시
     if direction == 0:
         while y >= 0:
             if board[x][y] == 'S':
                 return True
             if board[x][y] == 'O':
                 return False
             y -= 1
    # 북쪽 감시
     if direction == 1:
         while x >= 0:
             if board[x][y] == 'S':
                 return True
             if board[x][y] == 'O':
                 return False
             x -= 1
    # 동쪽 감시
     if direction == 2:
         while y < n:
             if board[x][y] == 'S':
                 return True
             if board[x][y] == 'O':
                 return False
             y += 1
    # 남쪽 감시
     if direction == 3:
         while x < n:
             if board[x][y] == 'S':
                 return True
             if board[x][y] == 'O':
                 return False
             x += 1
             
    # 학생, 감시물이 걸리지 않았다면 감시 실패
     return False

def process():
    # 각 선생님마다
    for x, y in teachers:
        # 동,서,남,북 감시 Check
        for i in range(4):
            # watch() True : 감시성공
            if watch(x, y, i):
                # 학생이 진행에 실패 False
                return False
    # 학생이 진행에 성공 True
    return True

# 해당 조합의 장애물 설치 환경에서 감시망에 걸리지 않으면 True
find = False
for data in combinations(spaces, 3):
    # 해당 조합에서 장애물 설치
    for x, y in data:
        board[x][y] = 'O'
    
    # process() True : 학생이 걸리지 않음
    if process():
        find = True
        break
    
    # 해당 조합에선 감시에 걸림, 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'
        
if find:
    print('YES')
else:
    print('NO')