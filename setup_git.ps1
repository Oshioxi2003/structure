# Automated Git Setup Script for PowerShell
# Run this script: .\setup_git.ps1

Write-Host "=== EDU Project - Git Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    git --version | Out-Null
} catch {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Initialize git repository
Write-Host "1. Initializing Git repository..." -ForegroundColor Green
git init

# Add .gitignore first
Write-Host "2. Adding .gitignore..." -ForegroundColor Green
git add .gitignore
git add README.md
git commit -m "chore: initial commit with gitignore and readme"

# Backend configuration files
Write-Host "3. Adding backend configuration..." -ForegroundColor Green
git add backend\.env
git add backend\.gitignore
git add backend\pyproject.toml
git add backend\requirements.txt
git add backend\Makefile
git add backend\README.md
git add backend\conftest.py
git commit -m "feat: add backend configuration files"

# Django project structure
Write-Host "4. Adding Django project structure..." -ForegroundColor Green
git add backend\manage.py
git add backend\config\
git commit -m "feat: add Django project configuration"

# Common app
Write-Host "5. Adding common app..." -ForegroundColor Green
git add backend\apps\__init__.py
git add backend\apps\common\
git commit -m "feat: add common app with utilities"

# Users app
Write-Host "6. Adding users app..." -ForegroundColor Green
git add backend\apps\users\
git commit -m "feat: add users app with custom User model"

# Docker files
Write-Host "7. Adding Docker configuration..." -ForegroundColor Green
git add backend\Dockerfile
git add backend\docker-compose.yml
git commit -m "feat: add backend Docker configuration"

# Scripts
Write-Host "8. Adding utility scripts..." -ForegroundColor Green
git add backend\scripts\
git commit -m "feat: add utility scripts"

# Requirements
Write-Host "9. Adding requirements..." -ForegroundColor Green
git add backend\requirements\
git commit -m "feat: add Python requirements"

# Static directories
Write-Host "10. Adding static directories..." -ForegroundColor Green
git add backend\templates\
git add backend\static\
git add backend\media\
git commit -m "feat: add static directories"

# Frontend structure
Write-Host "11. Adding frontend structure..." -ForegroundColor Green
git add frontend\src\
git add frontend\public\
git add frontend\package.json
git add frontend\next.config.mjs
git add frontend\jsconfig.json
git add frontend\.env.local
git add frontend\.gitignore
git commit -m "feat: add Next.js frontend structure"

# Frontend Docker
Write-Host "12. Adding frontend Docker..." -ForegroundColor Green
git add frontend\Dockerfile
git add frontend\docker-compose.yml
git commit -m "feat: add frontend Docker configuration"

# Documentation
Write-Host "13. Adding documentation..." -ForegroundColor Green
git add BACKEND_GUIDE.md
git commit -m "docs: add backend documentation"

# Set main branch
Write-Host "14. Setting main branch..." -ForegroundColor Green
git branch -M main

# Add remote origin
Write-Host "15. Adding remote origin..." -ForegroundColor Green
try {
    git remote add origin https://github.com/Oshioxi2003/structure.git
} catch {
    Write-Host "Remote 'origin' already exists, skipping..." -ForegroundColor Yellow
}

# Push to GitHub
Write-Host "16. Pushing to GitHub..." -ForegroundColor Green
Write-Host ""
Write-Host "IMPORTANT: You may need to authenticate with GitHub!" -ForegroundColor Yellow
Write-Host "If you haven't set up Git credentials, you'll be prompted to login." -ForegroundColor Yellow
Write-Host ""

$confirm = Read-Host "Ready to push to GitHub? (Y/N)"
if ($confirm -eq 'Y' -or $confirm -eq 'y') {
    git push -u origin main
    Write-Host ""
    Write-Host "=== Git Setup Complete! ===" -ForegroundColor Green
    Write-Host "Repository: https://github.com/Oshioxi2003/structure" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "Skipped pushing. Run 'git push -u origin main' when ready." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Summary of commits:" -ForegroundColor Cyan
git log --oneline
