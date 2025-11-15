s = input("Nhập mật khẩu: ")

co_hoa = False
co_thuong = False
co_so = False
co_dac_biet = False

for ky_tu in s:
    if ky_tu.isupper():
        co_hoa = True
    elif ky_tu.islower():
        co_thuong = True
    elif ky_tu.isdigit():
        co_so = True
    else:
        co_dac_biet = True   # còn lại là ký tự đặc biệt

# kiểm tra độ dài và các điều kiện
if len(s) > 6 and co_hoa and co_thuong and co_so and co_dac_biet:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu KHÔNG mạnh")
