import math

# Nhập n
n = int(input("Nhập n: "))

# Mở file ở chế độ ghi
with open("bai1.txt", "w") as f:
    # Duyệt từng số từ 1..n
    for i in range(1, n + 1):
        # Kiểm tra số chính phương
        if int(math.sqrt(i)) ** 2 == i:
            f.write(str(i) + "\n")

print("Đã ghi các số chính phương vào tập tin bai1.txt")
