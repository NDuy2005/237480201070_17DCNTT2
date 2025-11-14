import math
tong=0
n=int(input("Nhập n:"))
with open("Bai2.txt",'w') as f:
    for i in range(1,n):
        if i % 2 == 0:
            tong += i
            f.write(str(i) + "\n")
if tong == n:
    print(n, "là số hoàn hảo nè")
else:
    print(n, "không phải số hoàn hảo ^^")
