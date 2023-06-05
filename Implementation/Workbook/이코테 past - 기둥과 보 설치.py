def check(answer):
    for x, y, a in answer:
        if a == 0: # 설치되어 있는게 '기둥'
            # 기둥 조건 : '바닥 위' or '보의 한쪽 끝 위' or '다른 기둥 위'
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] or [x, y - 1, 0] in answer:
                continue
            return False
        elif a == 1: # 설치되어 있는게 '보'
            # 보 조건 : '한쪽 끝이 기둥 위' or '양쪽 끝이 다른 보와 동시 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0: # 삭제
            answer.remove([x, y, a]) # 1. 일단 삭제 후
            if not check(answer): # 2. 이전 건축물들의 성립여부 확인
                answer.append([x, y, a]) # 3. 성립 x -> 원상태
        if b == 1: # 추가
            answer.append([x, y, a]) # 1. 일단 추가 후
            if not check(answer): # 2. 이전 건축물들의 성립여부 확인
                answer.remove([x, y, a]) # 3. 성립 x -> 원상태
    return sorted(answer)