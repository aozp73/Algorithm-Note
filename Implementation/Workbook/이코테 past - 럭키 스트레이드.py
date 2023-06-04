n = input()
half_length = int(len(n)) // 2
res = 0

for i in range(half_length):
    res += int(n[i])

for i in range(half_length, half_length * 2):
    res -= int(n[i])

if res == 0:
    print("LUCKY")
else:
    print("READY")