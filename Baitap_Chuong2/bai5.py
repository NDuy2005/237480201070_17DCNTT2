# Mở file INPUT4.TXT ở chế độ đọc
f = open("input5.txt", "r")

# Đọc nội dung file
data = f.read()

# Đóng file sau khi đọc xong
f.close()

# Tách các phần tử thành danh sách
lst = data.split()

# Tạo danh sách chứa các số
sapxep = []

# Duyệt từng phần tử trong list
for x in lst:
    x = int(x)        # chuyển chuỗi thành số
    sapxep.append(x)  # thêm tất cả số

# Sắp xếp tăng dần
sapxep.sort()

# Mở file OUTPUT4.TXT ở chế độ ghi
f = open("output5.TXT", "w")

# Ghi từng số vào file
for x in sapxep:
    f.write(str(x) + "\n")

# Đóng file
f.close()
