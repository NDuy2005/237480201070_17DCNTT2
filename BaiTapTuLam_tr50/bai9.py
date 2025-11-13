# Nhập số tiền
money = int(input("Nhập số tiền: "))

# Danh sách mệnh giá tờ tiền từ lớn đến nhỏ
menh_gia = [50000, 20000, 10000, 5000, 2000, 1000]

# Xử lý và in kết quả
for menh in menh_gia:
    so_to = money // menh
    if so_to > 0:
        print(f"{so_to} tờ {menh}")
    money %= menh
