from bisect import bisect_left, bisect_right

# 리스트 내 tesaaa ~ teszzz 개수 세기
# left_value : 가장 왼쪽에 해당하는 값 인덱스 반환, 
#              없다면 해당 값 보다 큰 값 중 최소값 인덱스 반환
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# array : xxx?? 체크용, reversed_array : ??xxx 체크용
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    # 값 입력
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
        
    # 각각의 자리수 저장 공간 정렬
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        # xxx?? 접미사에 ?가 올 경우
        if q[0] != '?':
            # xxxaa ~ xxxzz 범위 내 단어 개수 세기
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        # ????? 또는 ??xxx 접두사에 ?가 올 경우
        else:
            # 뒤집어서 # xxxaa ~ xxxzz 범위 내 단어 개수 세기
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer