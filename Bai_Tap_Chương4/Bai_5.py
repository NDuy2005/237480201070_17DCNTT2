s = input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0

for kytu in s:
    if kytu.isupper():  #ktra ký tự Hoa
        hoa += 1 #tăng lên 1 đơn vị
    elif kytu.islower():#ký tự thường
        thuong += 1
    elif kytu.isdigit():#ký tự số
        so += 1

print("Số ký tự in hoa:", hoa)
print("Số ký tự in thường:", thuong)
print("Số ký tự số:", so)
