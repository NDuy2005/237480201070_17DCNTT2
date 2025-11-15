# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
nhap_list = nhap.split()

# Chuyển từng phần tử sang số nguyên
L = []
for x in nhap_list:
    L.append(int(x))

# Tìm giá trị dương đầu tiên
tim_thay = False
for so in L:
    if so > 0:
        print("Giá trị dương đầu tiên là:", so)
        tim_thay = True
        break

if not tim_thay:
    print(-1)
