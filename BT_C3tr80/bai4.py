# Nhập danh sách số nguyên, cách nhau bằng dấu cách
lst = input("Nhập các số (cách nhau bằng dấu cách): ").split()

# Chuyển từng phần tử trong danh sách sang kiểu int
for i in range(len(lst)):
    lst[i] = int(lst[i])

# Tìm giá trị lớn nhất
lon_nhat = lst[0]             # giả sử phần tử đầu tiên là lớn nhất
for x in lst:
    if x > lon_nhat:
        lon_nhat = x

print("Giá trị lớn nhất là:", lon_nhat)
