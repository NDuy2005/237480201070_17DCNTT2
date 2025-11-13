a = int(input("Nhập số a: "))
lst = list(map(int, input("Nhập các số (cách nhau bằng dấu cách): ").split()))

tong = 0
dem = 0

for x in lst:
    if x % a == 0:
        tong += x
        dem += 1

if dem > 0:
    print("Trung bình các số chia hết cho", a, "là:", tong / dem)
else:
    print("Không có số nào chia hết cho", a)
