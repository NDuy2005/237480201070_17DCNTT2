n = int(input("Nhập số nguyên dương n: "))

count = 0
while n > 0:
    n = n // 10
    count += 1

print("Số chữ số là:", count)
