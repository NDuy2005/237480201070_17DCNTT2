# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
L = []
for x in nhap.split():
    L.append(int(x))

# Sắp xếp L theo thứ tự tăng dần
for i in range(len(L)):
    for j in range(0, len(L)-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

print("List sau khi sắp xếp:", L)
