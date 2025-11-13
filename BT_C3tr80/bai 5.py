# Bước 1: Nhập danh sách số nguyên
lst = input("Nhập các số (cách nhau bằng dấu cách): ").split()

# Bước 2: Chuyển từng phần tử thành số nguyên
for i in range(len(lst)):
    lst[i] = int(lst[i])

# Bước 3: Nhập giá trị cần tìm
k = int(input("Nhập giá trị k cần tìm: "))

# Bước 4: Tạo list rỗng để lưu vị trí tìm được
vitri = []

# Bước 5: Duyệt qua danh sách
for i in range(len(lst)):   # i = 0, 1, 2, ...
    if lst[i] == k:         # nếu phần tử bằng k
        vitri.append(i)     # thì lưu lại vị trí i

# Bước 6: In kết quả
if len(vitri) == 0:
    print("Không có giá trị", k, "trong danh sách.")
else:
    print("Vị trí của", k, "là:", vitri)
