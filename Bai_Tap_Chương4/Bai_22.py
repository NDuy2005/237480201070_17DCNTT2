# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
NL = []
for x in nhap.split():
    NL.append(int(x))

# Kiểm tra xem tất cả phần tử đều lẻ không
la_chan_le = True  # giả sử tất cả lẻ

for so in NL:
    if so % 2 == 0:  # nếu gặp số chẵn
        la_chan_le = False
        break

# In kết quả
if la_chan_le:
    print("Đúng")
else:
    print("Sai")
