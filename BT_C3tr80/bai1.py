a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

def bang_cuu_chuong(a, b):
    n = max(a, b)  # lấy số lớn hơn
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# gọi hàm để thực thi
bang_cuu_chuong(a, b)
