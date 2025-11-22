

students = []  # danh sách sinh viên rỗng ban đầu


def add_student(ma, ten):
    """Thêm sinh viên mới"""
    students.append({"ma": ma, "ten": ten})


def remove_student(ma):
    """Xóa sinh viên theo mã"""
    for sv in students:
        if sv["ma"] == ma:
            students.remove(sv)
            return True
    return False


def update_student(ma, ten_moi):
    """Sửa tên sinh viên theo mã"""
    for sv in students:
        if sv["ma"] == ma:
            sv["ten"] = ten_moi
            return True
    return False


def get_students():
    """Trả về danh sách sinh viên"""
    return students