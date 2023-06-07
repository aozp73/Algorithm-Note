n = int(input())
data = list(map(int, input().split()))
data.sort()

group_cnt = 0
person_cnt = 0

for i in data:
    person_cnt += 1
    if person_cnt >= i:
        group_cnt += 1
        person_cnt = 0
        
print(group_cnt)