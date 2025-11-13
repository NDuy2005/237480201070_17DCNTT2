L = list(map(int, input("Nhập các số (cách nhau bằng dấu cách): ").split()))
a = int(input("Nhập số nguyên dương a: "))

# Sắp xếp list giảm dần (từ lớn đến nhỏ)
L.sort(reverse=True)

if a <= len(L):
    print(f"Giá trị lớn thứ {a} là:", L[a - 1])
else:
    print("a lớn hơn số phần tử trong danh sách!")
