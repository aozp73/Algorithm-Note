# Key 90도 회전
def rotate_90_degree(a):
    # 회전한 리스트를 사전에 생성하기 위해 행, 열의 길이 계산
    n = len(a)
    m = len(a[0])
    res = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            res[j][n - i - 1] = a[i][j]
    return res

# 중앙 자물쇠 부분의 합이 모두 1 인지 확인 (unlock)
def unlock_check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True
        

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 1. 자물쇠 이동 가능 : key 이동을 위해 자물쇠 크기 3배로 확장
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 확장된 자물쇠 판의 중앙에 기존 자물쇠 세팅
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # 2. 자물쇠 회전 가능 : 4방향에 대해 확인
    for rotate in range(4):
        key = rotate_90_degree(key)
        
        for x in range(1, n * 2):
            for y in range(1, n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                if unlock_check(new_lock) == True:
                    return True
                
                # 해당 차수에서 풀지 못했다면, 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False