lst = input("Nhập các chuỗi (cách nhau bằng dấu cách): ").split()

ngan_nhat = lst[0]
for s in lst:
    if len(s) < len(ngan_nhat):
        ngan_nhat = s

print("Chuỗi ngắn nhất là:", ngan_nhat)
