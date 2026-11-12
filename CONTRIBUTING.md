# Đóng góp addon Blender

Ai cũng đóng góp được, cần một tài khoản GitHub. Mọi đóng góp đi qua **Pull Request** và được chủ repo duyệt trước khi gộp.

## Cách làm

1. Mở https://github.com/minhdv-zz/team-blender-addons/upload/main/addons (hoặc tab **Đóng góp** trên https://minhdv-zz.github.io/team-skills/).
2. Kéo thả **nguyên thư mục addon** vào trang. Thư mục phải nằm trực tiếp trong `addons/`.
3. Chưa có quyền ghi thì GitHub tự tạo bản sao (fork). Bấm **Propose changes** rồi **Create pull request**.

## Yêu cầu

- Thư mục có `__init__.py` (addon kiểu cũ) hoặc `blender_manifest.toml` (extension) ở ngay đầu thư mục.
- **Ghi tên tác giả**: `bl_info["author"]` trong `__init__.py`, hoặc `maintainer` trong `blender_manifest.toml`. Thiếu tên thì bị từ chối.
- Có file giấy phép (`LICENSE`...) cho phép chia sẻ lại. **Addon trả phí hoặc không có giấy phép rõ ràng thì không nhận.**
- Tên thư mục: 2-64 ký tự gồm chữ, số, `-` hoặc `_`.
- Không file quá 25 MB, không khóa hay token.
- File biên dịch sẵn (`.dll`, `.pyd`, `.so`...) cần giải thích nguồn gốc trong mô tả Pull Request.

## Kiểm tra tự động

Pull Request chạy `scripts/validate.py` (cấu trúc, giấy phép, kích thước, quét khóa). Chạy thử trên máy: `python scripts/validate.py`.

## Sau khi gộp

Repo `team-skills` có bot chạy hằng ngày (và mỗi lần có thay đổi) đọc repo này và thêm addon mới vào danh sách trên trang web. Mô tả lấy từ `bl_info` của addon. Chủ repo có thể chỉnh lại tiêu đề, mô tả trong `docs/addons.json` của `team-skills`.

## Lưu ý an toàn

Addon là mã Python chạy trong Blender của người cài. Chủ repo sẽ đọc kỹ trước khi gộp.
