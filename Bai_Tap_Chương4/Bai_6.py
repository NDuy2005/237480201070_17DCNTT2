s=input("Nhập chuỗi :")
tong=0
so=0
for ky_tu in s:
    if ky_tu.isdigit():#ký tự số
        tong+=int(ky_tu)
print("tong ky tu so:",tong)