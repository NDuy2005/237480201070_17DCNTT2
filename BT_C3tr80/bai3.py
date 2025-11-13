a = int(input("Nhập số nguyên a: "))

def la_so_armstrong(a):
    s = str(a)             # đổi số thành chuỗi
    tong = 0
    for ch in s:           # duyệt từng chữ số
        so = int(ch)       # chuyển từng ký tự thành số
        tong += so ** len(s)  # cộng lũy thừa từng số
    if tong == a:
        return True
    else:
        return False

if la_so_armstrong(a):
    print(a, "là số Armstrong")
else:
    print(a, "không phải số Armstrong")
