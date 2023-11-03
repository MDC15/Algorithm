import hashlib

# Nhập dữ liệu từ bàn phím
input_string = input("Nhập chuỗi cần mã hóa: ")

# Tạo một đối tượng hash SHA-256
hash_object = hashlib.sha256()


# Cập nhật đối tượng hash với dữ liệu đầu vào
hash_object.update(input_string.encode('utf-8'))

# Lấy giá trị băm (hash)
hashed_string = hash_object.hexdigest()

print("Chuỗi gốc:", input_string)
print("\nHash SHA-256:", hashed_string)

# Lưu giá trị hash vào tệp tin
with open('file.txt', 'w') as file:
    file.write(hashed_string)

print("\nGiá trị hash đã được lưu vào file.txt.")