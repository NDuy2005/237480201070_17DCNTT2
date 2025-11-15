# Khởi tạo danh sách sinh viên (dictionary)
# Key: mã sinh viên, Value: tên sinh viên
danh_sach_sinh_vien = {}


def xem_danh_sach():
    if not danh_sach_sinh_vien:
        print("Danh sách sinh viên trống.")
    else:
        print("Danh sách sinh viên:")
        print("Mã SV\tTên SV")
        for ma, ten in danh_sach_sinh_vien.items():
            print(f"{ma}\t{ten}")


def them_sinh_vien():
    ma = input("Nhập mã sinh viên: ").strip()
    if ma in danh_sach_sinh_vien:
        print("Mã sinh viên đã tồn tại!")
        return
    ten = input("Nhập tên sinh viên: ").strip()
    danh_sach_sinh_vien[ma] = ten
    print("Thêm sinh viên thành công.")


def xoa_sinh_vien():
    ma = input("Nhập mã sinh viên cần xóa: ").strip()
    if ma in danh_sach_sinh_vien:
        del danh_sach_sinh_vien[ma]
        print("Xóa sinh viên thành công.")
    else:
        print("Không tìm thấy mã sinh viên.")


def sua_sinh_vien():
    ma = input("Nhập mã sinh viên cần sửa: ").strip()
    if ma in danh_sach_sinh_vien:
        ten_moi = input("Nhập tên sinh viên mới: ").strip()
        danh_sach_sinh_vien[ma] = ten_moi
        print("Sửa sinh viên thành công.")
    else:
        print("Không tìm thấy mã sinh viên.")


# Vòng lặp menu chính
while True:
    print("\n===== QUẢN LÝ SINH VIÊN =====")
    print("1. Xem danh sách sinh viên")
    print("2. Thêm sinh viên")
    print("3. Xóa sinh viên")
    print("4. Sửa sinh viên")
    print("0. Thoát")

    chon = input("Chọn chức năng: ").strip()

    if chon == "1":
        xem_danh_sach()
    elif chon == "2":
        them_sinh_vien()
    elif chon == "3":
        xoa_sinh_vien()
    elif chon == "4":
        sua_sinh_vien()
    elif chon == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
