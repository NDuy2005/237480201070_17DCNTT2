n = int(input("Nhập số nguyên dương: "))

if n > 0:
    if n % 5 == 0 and n % 7 == 0:
        print("Có")
    else:
        print("Không")
else:
    print("Vui lòng nhập số nguyên dương!")


