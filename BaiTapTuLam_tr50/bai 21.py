n = int(input("Nhập số nguyên dương n: "))

if n < 2:
    print(n, "không phải số nguyên tố.")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải số nguyên tố.")
