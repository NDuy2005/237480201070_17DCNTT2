# Nhập list số nguyên
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
L = []
for x in nhap.split():
    L.append(int(x))

# Tìm vị trí thỏa điều kiện
vi_tri = -1  # mặc định là -1 nếu không tìm thấy

for i in range(1, len(L)-1):
    if L[i] == L[i-1] * L[i+1]:
        vi_tri = i
        break

print(vi_tri)
