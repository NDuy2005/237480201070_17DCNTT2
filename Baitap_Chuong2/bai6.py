# Đọc file input
f = open("input6.txt", "r")
lst = f.readlines()
f.close()

# Tách 2 số trên cùng 1 dòng
a, b = lst[0].split()
num1 = int(a)
num2 = int(b)

# Hàm tính UCLN
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tính BCNN
def bcnn(a, b):
    return a * b // ucln(a, b)

ucln_val = ucln(num1, num2)
bcnn_val = bcnn(num1, num2)

# Ghi file output
f = open("output6.txt", "w")
f.write("UCLN: " + str(ucln_val) + "\n")
f.write("BCNN: " + str(bcnn_val) + "\n")
f.close()
