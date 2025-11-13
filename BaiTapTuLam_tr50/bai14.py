# Nhập điểm 3 môn
van = float(input("Nhập điểm môn Văn: "))
toan = float(input("Nhập điểm môn Toán: "))
anh = float(input("Nhập điểm môn Tiếng Anh: "))

# Tính điểm trung bình
diem_tb = (van + toan + anh) / 3

# In điểm trung bình
print("Điểm trung bình:", round(diem_tb, 2))

# Xét điều kiện đậu chuyên
if diem_tb >= 8.5:
    if toan >= 9 and toan > van and toan > anh:
        print("Học sinh đậu chuyên Toán.")
    elif van >= 9 and van > anh:
        print("Học sinh đậu chuyên Văn.")
    elif anh >= 8.0:
        print("Học sinh đậu chuyên Tiếng Anh.")
    else:
        print("Học sinh đậu chuyên Tin học.")
else:
    print("Học sinh không đậu chuyên.")
