# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập danh sách và số a
L = list(map(int, input("Nhập các số (cách nhau bằng dấu cách): ").split()))
a = int(input("Nhập số nguyên dương a: "))

# Tạo list mới gồm a và các số nguyên tố tìm được
ket_qua = [a]
for x in L:
    if la_so_nguyen_to(x):
        ket_qua.append(x)

print("List mới là:", ket_qua)
