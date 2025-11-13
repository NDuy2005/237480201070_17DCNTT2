# Hàm tìm UCLN (Ước chung lớn nhất)
def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tìm BCNN (Bội chung nhỏ nhất)
def BCNN(a, b):
    return abs(a * b) // UCLN(a, b)

# Hàm kiểm tra 2 số có nguyên tố cùng nhau không
def nguyen_to_cung_nhau(a, b):
    return UCLN(a, b) == 1


# 🌟 Phần chạy chính
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

ucln = UCLN(a, b)
bcnn = BCNN(a, b)
cung_nhau = nguyen_to_cung_nhau(a, b)

print("\n----- KẾT QUẢ -----")
print(f"UCLN của {a} và {b} là: {ucln}")
print(f"BCNN của {a} và {b} là: {bcnn}")
print(f"Hai số {a} và {b} có nguyên tố cùng nhau không? {cung_nhau}")
