# Nhập số nguyên dương
n = int(input("Nhập số nguyên dương: "))

# Kiểm tra chia hết cho 7
if n > 0:
    if n % 7 == 0:
        print("Là số chia hết cho 7")
    else:
        print("Không chia hết cho 7")
else:
    print("Vui lòng nhập số nguyên dương!")
