A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

ket_qua = ""
i = 0

while i < len(A):
    # nếu đoạn từ A[i] trùng với chuỗi B
    if A[i:i+len(B)] == B:
        i += len(B)   # bỏ qua chuỗi B, không thêm vào kết quả
    else:
        ket_qua += A[i]
        i += 1

print("Chuỗi A sau khi xóa B:", ket_qua)
