from itertools import permutations

n = int(input())
m = n - 1 
num = list(map(int, input().split()))
plus, minus, multi, divide = list(map(int, input().split()))
oper = ['+', '-', '*', '//']

max_val = -1e9-1
min_val = 1e9+1


def dfs(m, now):
    global max_val, min_val, plus, minus, multi, divide
    
    if m == n:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
        return
    
    if plus > 0:
        plus -= 1
        dfs(m + 1, now + num[m])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(m + 1, now - num[m])
        minus += 1
    if multi > 0:
        multi -= 1
        dfs(m + 1, now * num[m])
        multi += 1
    if divide > 0:
        divide -= 1
        if now < 0:
          dfs(m + 1, -(-now // num[m]))
        else:
          dfs(m + 1, now // num[m])
        divide += 1

dfs(1, num[0])
print(max_val)
print(min_val)
