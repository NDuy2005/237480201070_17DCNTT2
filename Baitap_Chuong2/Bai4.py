# Mở file INPUT4.TXT ở chế độ đọc
f = open("input4.txt", "r")

# Đọc nội dung file
data = f.read()

# Đóng file sau khi đọc xong
f.close()

# Tách các phần tử thành danh sách
lst = data.split()

# Tạo danh sách chứa số chẵn
chan = []

# Duyệt từng phần tử trong list
for x in lst:
    x = int(x)        # chuyển chuỗi thành số
    if x % 2 == 0:    # nếu là số chẵn
        chan.append(x)

# Mở file OUTPUT4.TXT ở chế độ ghi
f = open("output4.TXT", "w")

# Ghi từng số chẵn vào file
for x in chan:
    f.write(str(x) + "\n")

# Đóng file
f.close()
