# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
nhap_list = nhap.split()

# Chuyển từng phần tử sang số nguyên
L = []
for x in nhap_list:
    L.append(int(x))

# Nhập X
X = int(input("Nhập số nguyên X: "))

# Tìm giá trị xa X nhất
xa_nhat = L[0]  # giả sử giá trị đầu tiên là xa nhất
khoang_cach_max = abs(L[0] - X)

for so in L:
    khoang_cach = abs(so - X)
    if khoang_cach > khoang_cach_max:
        khoang_cach_max = khoang_cach
        xa_nhat = so

print("Giá trị xa X nhất là:", xa_nhat)
