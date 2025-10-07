# 🚀 Git Setup Scripts

## Available Scripts

### 1. `quick_git.ps1` - Fast Setup ⚡
**Khuyến nghị cho người mới bắt đầu**

Tạo 1 commit duy nhất với tất cả files.

```powershell
.\quick_git.ps1
```

**Kết quả:**
- 1 commit: "Initial commit: Django + Next.js full stack project structure"
- Push to GitHub

---

### 2. `setup_git.ps1` - Organized Setup 📦
**Khuyến nghị cho dự án production**

Tạo nhiều commits có tổ chức theo chức năng.

```powershell
.\setup_git.ps1
```

**Kết quả:**
- 13 commits riêng biệt
- Lịch sử commit rõ ràng
- Dễ review và rollback

---

### 3. `git_commands.ps1` - Manual Commands 📝

File chứa tất cả commands để bạn copy/paste thủ công.

**Cách dùng:**
1. Mở file `git_commands.ps1`
2. Copy từng khối lệnh
3. Paste vào PowerShell
4. Chạy từng bước

---

## 🎯 Nên chọn script nào?

| Script | Tốc độ | Tổ chức | Phù hợp cho |
|--------|--------|---------|-------------|
| `quick_git.ps1` | ⚡⚡⚡ | ⭐ | Prototype, demo |
| `setup_git.ps1` | ⚡⚡ | ⭐⭐⭐ | Production, team |
| `git_commands.ps1` | ⚡ | ⭐⭐ | Học Git, custom |

---

## 📋 Before Running

1. ✅ Git đã cài đặt
2. ✅ Đã tạo repo trên GitHub
3. ✅ Đã setup authentication

**Xem chi tiết:** [GIT_SETUP_GUIDE.md](./GIT_SETUP_GUIDE.md)

---

## 🔥 Quick Start (Recommended)

```powershell
# Kiểm tra Git
git --version

# Chạy quick setup
.\quick_git.ps1

# Done! ✅
```

---

## 📖 Detailed Guide

Xem file [GIT_SETUP_GUIDE.md](./GIT_SETUP_GUIDE.md) để biết:
- Hướng dẫn cài đặt Git
- Authentication methods
- Troubleshooting
- Manual commands
