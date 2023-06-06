from itertools import permutations

def solution(n, weak, dist):
    
    length = len(weak)
    
    # 주어진 원형을 일자로 만듬 
    # (9/10 지점에서 시작해도 한 바퀴만 더 돌면 되므로 2배로 확장)
    for i in range(length):
        weak.append(weak[i] + n)
        
    # 모든 친구를 투입해도 점검이 안되는 경우 체크용 (+1)
    answer = len(dist) + 1
    
    # 완전 탐색 : 모든 취약지점을 시작점으로 탐색
    for start in range(length):
        
        # 1. 친구들을 줄 세우는 모든 경우의수에 대해 확인 (순열)
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            
            # 현재 투입 된 친구가 점검할 수 있는 마지막 위치
            last_check = weak[start] + friends[cnt - 1]
            
            # 2. 시작 취약점부터 마지막 취약점 까지 확인
            for index in range(start, start + length):
                # 만약 다음 취약점을 점검할 수 없다면
                if last_check < weak[index]:
                    # 다음 친구 투입
                    cnt += 1
                    # 점검 마치기 전 투입할 친구가 없다면 해당 순서 경우의수 종료
                    if cnt > len(dist):
                        break
                    # 다음 반복문에서 사용할 투입된 친구의 마지막 점검 가능 위치 세팅
                    last_check = weak[index] + friends[cnt - 1]
            
            # 해당 순서에서의 친구 투입 수를 비교하여 갱신
            answer = min(answer, cnt)
            
    if answer > len(dist):
        return -1
    return answer