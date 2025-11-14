# Tạo list rỗng
lst = []

# Nhập số lượng phần tử
n = int(input("Nhập số phần tử n: "))

# Nhập từng phần tử và thêm vào list
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

# Tạo các list theo yêu cầu
chan = []
chia_2_hoac_3 = []
tong = 0

for x in lst:
    # Số chẵn
    if x % 2 == 0:
        chan.append(x)

    # Số chia hết cho 2 hoặc 3
    if x % 2 == 0 or x % 3 == 0:
        chia_2_hoac_3.append(x)

    # Tính tổng
    tong += x

# Ghi vào file
with open("bai3.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, chan)) + "\n")
    f.write(" ".join(map(str, chia_2_hoac_3)) + "\n")
    f.write(str(tong))
