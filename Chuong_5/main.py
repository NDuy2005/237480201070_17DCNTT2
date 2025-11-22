# main.py
import quanlySV


def menu():
    print("\n===== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách sinh viên")
    print("5. Thoát")


while True:
    menu()
    chon = input("Chọn chức năng: ")

    if chon == "1":
        ma = input("Nhập mã sinh viên: ")
        ten = input("Nhập tên sinh viên: ")
        quanlySV.add_student(ma, ten)
        print(">> Thêm thành công!")

    elif chon == "2":
        ma = input("Nhập mã sinh viên cần xóa: ")
        if quanlySV.remove_student(ma):
            print(">> Đã xóa!")
        else:
            print(">> Không tìm thấy sinh viên!")

    elif chon == "3":
        ma = input("Nhập mã sinh viên cần sửa: ")
        ten_moi = input("Nhập tên mới: ")
        if quanlySV.update_student(ma, ten_moi):
            print(">> Sửa thành công!")
        else:
            print(">> Không tìm thấy sinh viên!")

    elif chon == "4":
        ds = quanlySV.get_students()
        print("\n===== DANH SÁCH SINH VIÊN =====")
        if len(ds) == 0:
            print("Danh sách rỗng.")
        else:
            for sv in ds:
                print(f"Mã: {sv['ma']} - Tên: {sv['ten']}")

    elif chon == "5":
        print("Thoát chương trình.")
        break

    else:
        print(">> Lựa chọn không hợp lệ!")