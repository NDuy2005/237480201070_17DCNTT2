# Nhập list số nguyên dạng chuỗi
nhap = input("Nhập list số nguyên (cách nhau bởi khoảng trắng): ")
nhap_list = nhap.split()  # tách chuỗi thành các phần tử

# chuyển từng phần tử sang số nguyên
L = []
for x in nhap_list:
    L.append(int(x))

# Nhập A và B
A = int(input("Nhập A: "))
B = int(input("Nhập B: "))

# Kiểm tra điều kiện
if A < B and B < len(L):
    # Lấy đoạn từ A đến B (bao gồm cả A và B)
    doan = L[A:B+1]

    # Tìm số nhỏ nhất thủ công
    nho_nhat = doan[0]
    for so in doan:
        if so < nho_nhat:
            nho_nhat = so

    print("Số nhỏ nhất từ vị trí", A, "đến", B, "là:", nho_nhat)
else:
    print("A, B không hợp lệ!")
