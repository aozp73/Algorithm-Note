def solution(N, stages):
    answer = []
    length = len(stages)
    
    # 모든 스테이지 순회 (오름차순)
    for i in range(1, N + 1):
        # 해당 스테이지에 올라간 사람 수 count
        cnt = stages.count(i)
        
        # 낮은 순부터 사용자가 있는 스테이까지 처리 후,
        # 남은 단계들에서 클리어한 사람이 없을 경우
        # length = 0이 됨, 해당 경우 fail = 0으로 처리
        if length == 0:
            fail = 0
        else:
            # 나머지는 cnt가 0이거나 있을 때 실패율 연산 진행
            fail = cnt / length
            
        answer.append((i, fail))
        length -= cnt
        
    # 실패율을 기준으로 내림차순
    # 실패율이 같다면 t[0]으로 돌아가 번호에 대해 오름차순 정렬 수행
    answer = sorted(answer, key=lambda t: -t[1])
    
    # 정렬된 스테이지의 번호 리스트에 저장하여 반환
    answer = [i[0] for i in answer]
    return answer