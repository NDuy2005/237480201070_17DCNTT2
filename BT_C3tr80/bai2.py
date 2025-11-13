a = int(input("Nhập số nguyên a: "))

def la_so_nguyen_to(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

if la_so_nguyen_to(a):
    print(a, "là số nguyên tố")
else:
    print(a, "không phải số nguyên tố")
