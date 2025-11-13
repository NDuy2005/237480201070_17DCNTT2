n = int(input("Nhập số nguyên dương n: "))

count = 0          # Tổng số chữ số
even_count = 0     # Số chữ số chẵn
odd_count = 0      # Số chữ số lẻ

temp = n           # Lưu tạm n để xử lý

while temp > 0:
    digit = temp % 10
    count += 1
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    temp = temp // 10

print("Số chữ số là:", count)
print("Số chữ số chẵn là:", even_count)
print("Số chữ số lẻ là:", odd_count)
