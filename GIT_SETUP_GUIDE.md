# 📝 Hướng dẫn Git Setup

## ⚠️ Yêu cầu

1. **Cài đặt Git** (nếu chưa có):
   - Download: https://git-scm.com/download/win
   - Hoặc: `winget install Git.Git`
   - Kiểm tra: `git --version`

2. **Cài đặt Git Credential Manager** (cho xác thực GitHub):
   - Thường được cài tự động với Git for Windows
   - Hoặc: https://github.com/git-ecosystem/git-credential-manager

## 🚀 Cách 1: Automatic (Khuyến nghị)

### Option A: Quick Setup (1 commit duy nhất)

```powershell
.\quick_git.ps1
```

Script này sẽ:
- ✅ Init git repository
- ✅ Add tất cả files
- ✅ Commit với message: "Initial commit: Django + Next.js full stack project structure"
- ✅ Set main branch
- ✅ Add remote origin
- ✅ Push to GitHub

### Option B: Detailed Setup (nhiều commits có tổ chức)

```powershell
.\setup_git.ps1
```

Script này sẽ tạo các commits riêng biệt:
1. Initial commit (gitignore, readme)
2. Backend configuration
3. Django project structure
4. Common app
5. Users app
6. Docker configuration
7. Scripts
8. Requirements
9. Static directories
10. Frontend structure
11. Frontend Docker
12. Documentation

## 🔧 Cách 2: Manual (Từng bước)

### Bước 1: Initialize Git

```powershell
git init
```

### Bước 2: Add files và commit

#### Root files
```powershell
git add .gitignore README.md
git commit -m "chore: initial commit"
```

#### Backend files
```powershell
# Configuration
git add backend\.env backend\.gitignore backend\pyproject.toml backend\requirements.txt backend\Makefile backend\README.md
git commit -m "feat: add backend configuration"

# Django project
git add backend\manage.py backend\config\
git commit -m "feat: add Django configuration"

# Apps
git add backend\apps\
git commit -m "feat: add Django apps"

# Docker
git add backend\Dockerfile backend\docker-compose.yml
git commit -m "feat: add backend Docker"

# Other
git add backend\scripts\ backend\requirements\ backend\templates\ backend\static\ backend\media\
git commit -m "feat: add backend utilities"
```

#### Frontend files
```powershell
git add frontend\
git commit -m "feat: add Next.js frontend"
```

#### Documentation
```powershell
git add BACKEND_GUIDE.md
git commit -m "docs: add documentation"
```

### Bước 3: Set main branch

```powershell
git branch -M main
```

### Bước 4: Add remote

```powershell
git remote add origin https://github.com/Oshioxi2003/structure.git
```

### Bước 5: Push to GitHub

```powershell
git push -u origin main
```

## 🔐 Xác thực GitHub

Khi push lần đầu, bạn sẽ được yêu cầu xác thực:

### Option 1: GitHub CLI (Khuyến nghị)
```powershell
# Cài đặt GitHub CLI
winget install GitHub.cli

# Đăng nhập
gh auth login
```

### Option 2: Personal Access Token
1. Vào: https://github.com/settings/tokens
2. Tạo token mới (classic)
3. Chọn quyền: `repo`
4. Copy token
5. Khi push, dùng token làm password

### Option 3: SSH Key
```powershell
# Tạo SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
Get-Content ~\.ssh\id_ed25519.pub | Set-Clipboard

# Add to GitHub: https://github.com/settings/ssh/new

# Change remote to SSH
git remote set-url origin git@github.com:Oshioxi2003/structure.git
```

## 🔍 Kiểm tra

```powershell
# Xem status
git status

# Xem commits
git log --oneline

# Xem remote
git remote -v

# Xem branches
git branch -a
```

## 🛠️ Troubleshooting

### Lỗi: "git: command not found"
- Cài đặt Git: https://git-scm.com/download/win
- Restart PowerShell

### Lỗi: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/Oshioxi2003/structure.git
```

### Lỗi: "failed to push"
```powershell
# Pull trước nếu repo không rỗng
git pull origin main --allow-unrelated-histories

# Hoặc force push (chỉ nếu chắc chắn)
git push -u origin main --force
```

### Lỗi: Authentication failed
- Dùng GitHub CLI: `gh auth login`
- Hoặc tạo Personal Access Token
- Hoặc setup SSH key

## 📚 Resources

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- Git Credential Manager: https://github.com/git-ecosystem/git-credential-manager

## ✅ Checklist

- [ ] Git đã được cài đặt
- [ ] Repository GitHub đã tạo
- [ ] Đã chọn phương thức xác thực
- [ ] Đã chạy script hoặc commands
- [ ] Đã push thành công
- [ ] Kiểm tra trên GitHub: https://github.com/Oshioxi2003/structure

---

**Tip**: Sau khi setup xong, các lần commit sau chỉ cần:
```powershell
git add .
git commit -m "your message"
git push
```
