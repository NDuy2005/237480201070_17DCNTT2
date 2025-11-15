# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
nhap_list = nhap.split()

# Chuyển từng phần tử sang số nguyên
L = []
for x in nhap_list:
    L.append(int(x))

# Kiểm tra xem list có sắp xếp tăng dần không
tang_dan = True  # giả sử list tăng dần

for i in range(len(L)-1):
    if L[i] > L[i+1]:
        tang_dan = False
        break

# In kết quả
if tang_dan:
    print("True")
else:
    print("False")
