# 🎯 Quick Start Guide

## 📋 Tóm tắt nhanh

Bạn có **3 options** để setup Git:

```
┌─────────────────────────────────────────────────────┐
│  Option 1: QUICK (⚡ Nhanh nhất - 1 commit)         │
│  .\quick_git.ps1                                    │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Option 2: ORGANIZED (📦 Có tổ chức - 13 commits)  │
│  .\setup_git.ps1                                    │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Option 3: MANUAL (🔧 Tự làm - copy/paste)         │
│  Mở git_commands.ps1                                │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Chạy ngay (5 phút)

### Bước 1: Kiểm tra Git
```powershell
git --version
```

**Nếu lỗi:** Cài Git từ https://git-scm.com/download/win

### Bước 2: Chọn script và chạy
```powershell
# Chọn 1 trong 3:
.\quick_git.ps1      # ← Khuyến nghị
.\setup_git.ps1
# hoặc copy từ git_commands.ps1
```

### Bước 3: Xác thực GitHub
Khi được hỏi, chọn:
- Browser authentication (dễ nhất)
- Hoặc Personal Access Token
- Hoặc SSH key

### Bước 4: Done! ✅
Check: https://github.com/Oshioxi2003/structure

---

## 📊 So sánh Options

| Feature | Quick | Organized | Manual |
|---------|-------|-----------|--------|
| Thời gian | 2 phút | 3 phút | 5-10 phút |
| Số commits | 1 | 13 | Tùy ý |
| Dễ dùng | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Cho team | ⭐ | ⭐⭐⭐ | ⭐⭐ |
| Học Git | ⭐ | ⭐⭐ | ⭐⭐⭐ |

---

## 🎯 Recommendation

### Bạn muốn gì?
- 🏃 **Nhanh nhất**: `.\quick_git.ps1`
- 📝 **Lịch sử rõ ràng**: `.\setup_git.ps1`
- 🎓 **Học Git**: Copy từ `git_commands.ps1`

---

## ⚠️ Lưu ý

1. **Backend server đang chạy** → Không ảnh hưởng Git
2. **File .env** → Đã có trong .gitignore (an toàn)
3. **db.sqlite3** → Không được commit (đúng)
4. **node_modules/** → Sẽ không commit (đúng)

---

## 📚 Chi tiết hơn?

- **Git setup**: Xem `GIT_SETUP_GUIDE.md`
- **Backend**: Xem `BACKEND_GUIDE.md`
- **Scripts**: Xem `SCRIPTS_README.md`
- **Tổng quan**: Xem `PROJECT_SUMMARY.md`

---

## 🆘 Gặp vấn đề?

### "git: command not found"
```powershell
winget install Git.Git
# Restart PowerShell sau khi cài
```

### "Authentication failed"
```powershell
# Cài GitHub CLI (dễ nhất)
winget install GitHub.cli
gh auth login
```

### "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/Oshioxi2003/structure.git
```

---

## ✅ After Setup

Sau khi push xong, các lần sau chỉ cần:

```powershell
# Làm việc bình thường...
# Khi muốn commit:

git add .
git commit -m "your message here"
git push
```

---

**🎉 Bắt đầu nào!**

Chạy lệnh sau trong PowerShell:
```powershell
.\quick_git.ps1
```
