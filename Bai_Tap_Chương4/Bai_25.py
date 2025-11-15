# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
L = []
for x in nhap.split():
    L.append(int(x))

# Tạo 3 list phụ
chan = []
khong = []
le = []

for so in L:
    if so == 0:
        khong.append(so)
    elif so % 2 == 0:
        chan.append(so)
    else:
        le.append(so)

# Ghép lại theo thứ tự: chẵn + 0 + lẻ
L_moi = chan + khong + le

print("List sau khi sắp xếp:", L_moi)
