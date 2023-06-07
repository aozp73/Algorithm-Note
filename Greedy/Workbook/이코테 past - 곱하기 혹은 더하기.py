data = input()

res = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if res <= 1 or i <= 1:
        res += num
    else:
        res *= num
        
print(res)