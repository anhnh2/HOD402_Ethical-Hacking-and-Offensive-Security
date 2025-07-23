#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Khóa mã hóa phải có độ dài đúng chuẩn (16, 24 hoặc 32 byte cho AES)
key = b"aaaabbbbccccdddd"  # Đảm bảo kiểu dữ liệu là bytes

# Tạo đối tượng AES với chế độ ECB
cipher = AES.new(key, AES.MODE_ECB)

# Đọc file hình ảnh gốc
with open("tux.bmp", "rb") as f:
    clear = f.read()

# Tách phần đầu và cuối ảnh BMP để giữ nguyên header & padding
header = clear[0:64]
body = clear[64:-2]
footer = clear[-2:]

# Padding dữ liệu chính để đảm bảo độ dài là bội số của block size
padded_body = pad(body, AES.block_size)

# Mã hóa phần dữ liệu chính
ciphertext = cipher.encrypt(padded_body)

# Ghép lại thành dữ liệu cuối cùng: header + dữ liệu mã hóa + footer
final_data = header + ciphertext + footer

# Ghi dữ liệu vào file mới
with open("tux_ecb.bmp", "wb") as f:
    f.write(final_data)
