#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Khóa và IV phải là bytes, độ dài mỗi cái là 16 byte cho AES-128
key = b"aaaabbbbccccdddd"
iv = b"0000111122223333"

# Tạo cipher AES chế độ CBC
cipher = AES.new(key, AES.MODE_CBC, iv)

# Đọc nội dung file ảnh gốc
with open("tux.bmp", "rb") as f:
    clear = f.read()

# Tách phần header và phần dữ liệu cần mã hóa
header = clear[0:64]
body = clear[64:-2]
footer = clear[-2:]

# Padding phần nội dung để phù hợp block size
padded_body = pad(body, AES.block_size)

# Thực hiện mã hóa
ciphertext = cipher.encrypt(padded_body)

# Ghép thành nội dung ảnh mới: header + dữ liệu mã hóa + footer
final_data = header + ciphertext + footer

# Ghi ra file ảnh đã mã hóa
with open("tux_cbc.bmp", "wb") as f:
    f.write(final_data)
