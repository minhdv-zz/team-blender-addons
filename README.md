# team-blender-addons

Addon Blender dùng chung của team. Tách riêng khỏi repo skill (`team-skills`).

## Danh sách addon

| Addon | Thư mục | Ghi chú |
|---|---|---|
| Asset Creation Toolset (ACT) 2023.1 | `addons/Asset_Creation_Toolset_2023_1_Bl361` | Dùng cho skill `export_hoidz` (Import/Export Tools → Export FBX to Unity). Nguồn gốc: https://github.com/mrven/Blender-Asset-Creation-Toolset (GPL) |

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
