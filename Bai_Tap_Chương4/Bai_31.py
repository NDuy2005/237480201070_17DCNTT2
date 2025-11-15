def key_gia_tri_lon_nhat(d):
    """
    Nhận vào dictionary d, trả về key có giá trị lớn nhất.
    """
    if not d:  # nếu dictionary rỗng
        return None

    # Lấy key đầu tiên làm tham chiếu
    key_lon_nhat = list(d.keys())[0]
    gia_tri_lon_nhat = d[key_lon_nhat]

    # Duyệt các key khác
    for k, v in d.items():
        if v > gia_tri_lon_nhat:
            gia_tri_lon_nhat = v
            key_lon_nhat = k

    return key_lon_nhat

# --- Ví dụ sử dụng ---
d = {'a': 5, 'b': 10, 'c': 7}
print("Key có giá trị lớn nhất:", key_gia_tri_lon_nhat(d))
