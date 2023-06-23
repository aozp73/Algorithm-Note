from copy import deepcopy
from itertools import combinations

n, m = map(int, input().split())

data = []

temp = [[0] * m for _ in range(n)]
virus_posi = []
no_wall = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        check = data[i][j]
        if check == 2:
            virus_posi.append((i, j))
        elif check == 0:
            no_wall.append((i, j))

total_combi = list(combinations(no_wall, 3))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs():
    global res, temp
    
    for combi in total_combi:
        temp = deepcopy(data)
        
        for x, y in combi:
            temp[x][y] = 1
            
        for x, y in virus_posi:
            virus(x, y)
            
        res = max(res, get_score())
        
dfs()
print(res)