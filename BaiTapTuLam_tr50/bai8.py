# Nhập số nguyên có 4 chữ số
number = input("Nhập số nguyên có 4 chữ số: ")

# Kiểm tra độ dài
if len(number) == 4 and number.isdigit():
    total = sum(int(digit) for digit in number)
    print("Tổng các chữ số là:", total)
else:
    print("Vui lòng nhập số nguyên dương có đúng 4 chữ số.")
