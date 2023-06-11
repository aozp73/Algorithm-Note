n = int(input())
a = list(map(int, input().split()))
a.sort() # 정렬

# 중간값 출력
print(a[(n - 1) // 2])