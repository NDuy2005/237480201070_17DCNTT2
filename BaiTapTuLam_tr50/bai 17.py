n = int(input("Nhập số nguyên dương n: "))

# Tính tổng các số lẻ nhỏ hơn n
tong_le = 0
for i in range(1, n, 2):
    tong_le += i

# Tính tổng các số chẵn nhỏ hơn n
tong_chan = 0
for i in range(2, n, 2):
    tong_chan += i

print("Tổng các số lẻ nhỏ hơn", n, "là:", tong_le)
print("Tổng các số chẵn nhỏ hơn", n, "là:", tong_chan)
