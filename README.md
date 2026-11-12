# team-blender-addons

Addon Blender dùng chung của team. Tách riêng khỏi repo skill (`team-skills`).

## Danh sách addon

| Addon | Thư mục | Giấy phép / nguồn |
|---|---|---|
| Asset Creation Toolset (ACT) 2023.1 | `addons/Asset_Creation_Toolset_2023_1_Bl361` | GPL. https://github.com/mrven/Blender-Asset-Creation-Toolset (dùng cho skill `export_hoidz`) |
| EdgeFlow | `addons/EdgeFlow` | GPL v3, Benjamin Sauder |
| Simple Renaming Panel | `addons/simple_renaming_panel` | GPL v3, Matthias Patscheider |
| Interactive Tools | `addons/interactive_tools` | GPL v3, Maxi Vazquez, Ajfurey |
| UV Toolkit 2.1.2 | `addons/uv_toolkit` | GPL v3 |

Mỗi addon giữ nguyên file giấy phép của tác giả trong thư mục của nó.

Cài nhanh: dùng trang https://minhdv-zz.github.io/team-skills/ (tab Addon) khi đã cài plugin Paseo.

## Cài đặt

### Cách 1: cài từ zip
1. Nén thư mục addon (ví dụ `Asset_Creation_Toolset_2023_1_Bl361`) thành `.zip`, trong zip phải có thư mục addon ở gốc.
2. Blender → Edit → Preferences → Add-ons → Install from Disk → chọn zip.
3. Tick bật addon.

### Cách 2: clone + link (cập nhật bằng git pull)
```
git clone https://github.com/minhdv-zz/team-blender-addons.git
```
Rồi tạo junction từ thư mục addon vào `%APPDATA%\Blender Foundation\Blender\<phiên bản>\scripts\addons`:
```
mklink /J "%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\Asset_Creation_Toolset_2023_1_Bl361" "<đường-dẫn-repo>\addons\Asset_Creation_Toolset_2023_1_Bl361"
```

## Quy tắc
- Mỗi addon một thư mục trong `addons/`.
- Chỉ đưa addon miễn phí/được phép phân phối lại. Addon trả phí (HOps, UVPackmaster...) không đưa lên.
- Không đưa file nặng (.blend, .zip, ảnh lớn) vào repo.
