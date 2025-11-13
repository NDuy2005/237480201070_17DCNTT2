m = float(input("Nhập số thực dương m: "))

tong = 0
n = 0

while tong <= m:
    n += 1
    tong += 1 / n

print("Giá trị n nhỏ nhất sao cho tổng > m là:", n)
