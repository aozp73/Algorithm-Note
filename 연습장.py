# 입력 순서 : + - x /

# max 연산 순서 : / - + x (3 1 0 2) 
# min 연산 순서 : x + - / (2 0 1 3)



def cal_divide(num, cnt, cal):
    num_parse = num
    if (cal[3] != 0):
        for i in range (cnt, cnt + cal[3]):
            num_parse = abs(num) // data[i]
            num = -num_parse if num < 0 else num_parse
    cnt += cal[3]
    return num, cnt

def cal_minus(num, cnt, cal):
    if (cal[1] != 0):
        for i in range (cnt, cnt + cal[1]):
            num -= data[i]
    cnt += cal[1]
    return num, cnt

def cal_plus(num, cnt, cal):  
    if (cal[0] != 0):
        for i in range (cnt, cnt + cal[0]):
            num += data[i]
    cnt += cal[0]
    return num, cnt     

def cal_multiply(num, cnt, cal): 
    if (cal[2] != 0):
        for i in range (cnt, cnt + cal[2]):
            num *= data[i] 
    cnt += cal[2]
    return num, cnt

def cal_max(max_val, cal):
    cnt = 1
    max_val, cnt = cal_divide(max_val, cnt, cal)
    max_val, cnt = cal_minus(max_val, cnt, cal)
    max_val, cnt = cal_plus(max_val, cnt, cal)
    max_val, cnt = cal_multiply(max_val, cnt, cal)
    return max_val

# def cal_min(min_val, cal):
#     cnt = 1
#     min_val, cnt = cal_multiply(min_val, cnt, cal)
#     min_val, cnt = cal_plus(min_val, cnt, cal)
#     min_val, cnt = cal_minus(min_val, cnt, cal)
#     min_val, cnt = cal_divide(min_val, cnt, cal)
#     return min_val


n = int(input())
data = list(map(int, input().split()))
cal = list(map(int, input().split()))

data_len = len(data)
max_val = data[0]
min_val = data[0]
max_val = cal_max(max_val, cal)
# min_val = cal_min(min_val, cal)
print(max_val)
# print(min_val)


            
