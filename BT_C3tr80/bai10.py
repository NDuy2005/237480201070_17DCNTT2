import math

# 1️⃣ Kiểm tra số chẵn
def so_chan(n):
    return n % 2 == 0

# 2️⃣ Kiểm tra số hoàn hảo
def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

# 3️⃣ Kiểm tra số nguyên tố
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4️⃣ Kiểm tra số chính phương
def so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n

# 5️⃣ Tìm UCLN (Ước chung lớn nhất)
def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 6️⃣ Tìm BCNN (Bội chung nhỏ nhất)
def BCNN(a, b):
    return abs(a * b) // UCLN(a, b)

# 7️⃣ Kiểm tra hai số có nguyên tố cùng nhau hay không
def nguyen_to_cung_nhau(a, b):
    return UCLN(a, b) == 1


# 🌟 Phần chạy chính – nhập và in kết quả
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("\n----- KẾT QUẢ -----")
print(f"{a} là số chẵn? {so_chan(a)}")
print(f"{a} là số hoàn hảo? {so_hoan_hao(a)}")
print(f"{a} là số nguyên tố? {so_nguyen_to(a)}")
print(f"{a} là số chính phương? {so_chinh_phuong(a)}")
print(f"UCLN của {a} và {b} là: {UCLN(a, b)}")
print(f"BCNN của {a} và {b} là: {BCNN(a, b)}")
print(f"Hai số {a} và {b} có nguyên tố cùng nhau không? {nguyen_to_cung_nhau(a, b)}")
