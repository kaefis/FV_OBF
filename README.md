# FutureVisions Obfuscator

Công cụ obfuscation Python mạnh mẽ được viết bởi 16z (kaefis). Bảo vệ code Python khỏi reverse engineering bằng nhiều kỹ thuật obfuscation.

## Tại sao cần obfuscation?

Python code có thể dễ dàng đọc được. Obfuscation giúp:
- Bảo vệ thuật toán và logic kinh doanh
- Làm khó reverse engineering
- Ẩn thông tin nhạy cảm trong code
- Tăng độ phức tạp khi phân tích


## Cài đặt

### Yêu cầu

- Python 3.7+
- pip

### Dependencies

```bash
pip install pycryptodome fade
```


## Sử dụng

### Chạy tool

```bash
python 1.py
```

### Ví dụ

```
[+] Path: my_script.py
[+] Tên file xuất: obfuscated_script.py
[~] Anti-Debug? (y/n): y
[~] Anti-VM? (y/n): y
[~] Dead Code Injection? (y/n, mặc định: y): y
[~] Import Obfuscation? (y/n, mặc định: y): n
[~] 1-line obfuscate?: n
[~][WIP] Compile thành exe? (y/n): n
```

## Lưu ý

### Không nên

- Obfuscate file đã obfuscate (tool sẽ cảnh báo)
- Sửa đổi file obfuscated (sẽ phá tính toàn vẹn)
- Obfuscate code có nonlocal phức tạp

## Recovery Key

Sau mỗi lần obfuscate, bạn sẽ nhận được recovery key:

```
[KEY] abc123def456ghi789...
```

Lưu ý:
- Key này dùng để deobfuscate nếu cần
- KHÔNG chia sẻ key này
- Lưu key ở nơi an toàn

## So sánh

| Tính năng | FutureVisions | PyArmor | Opy |
|---------|--------------|---------|-----|
| Variable Renaming | ✅ | ✅ | ✅ |
| Control Flow Flattening | ✅ | ❌ | ❌ |
| String Encryption | ✅ | ✅ | ✅ |
| Constant Obfuscation | ✅ | ❌ | ❌ |
| Import Obfuscation | ✅ | ❌ | ❌ |
| Dead Code Injection | ✅ | ❌ | ❌ |
| Anti-Debug | ✅ | ✅ | ❌ |
| Anti-VM | ✅ | ✅ | ❌ |
| Free | ✅ | ❌ | ✅ |
| Open Source | ✅ | ❌ | ✅ |

## Đóng góp

Đóng góp luôn có ích đối với project,fork và tạo pull request

## License

MIT License
