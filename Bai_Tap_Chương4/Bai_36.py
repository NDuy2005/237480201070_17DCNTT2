# Mạng dữ liệu sinh viên (giả lập)
mang_sinh_vien = {
    "Nguyen Van A": {"tuoi": 20, "lop": "12A1", "diem": 8.5},
    "Tran Thi B": {"tuoi": 21, "lop": "12A2", "diem": 9.0},
    "Le Van C": {"tuoi": 22, "lop": "12A3", "diem": 7.5},
    "Pham Thi D": {"tuoi": 20, "lop": "12A1", "diem": 8.0}
}

# Nhập danh sách tên sinh viên cần tìm (cách nhau bởi dấu phẩy)
nhap = input("Nhập danh sách tên sinh viên cần tìm (cách nhau bởi dấu ','): ")
danh_sach_can_tim = [ten.strip() for ten in nhap.split(",")]

# Tìm kiếm và in thông tin
for ten in danh_sach_can_tim:
    if ten in mang_sinh_vien:
        print(f"Thông tin {ten}: {mang_sinh_vien[ten]}")
    else:
        print(f"{ten} không có trong mạng dữ liệu.")
