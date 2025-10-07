# Quick Git Setup - All at Once
# Run: .\quick_git.ps1

Write-Host "=== Quick Git Setup ===" -ForegroundColor Cyan

# Check git
try { git --version | Out-Null } 
catch { 
    Write-Host "ERROR: Install Git first!" -ForegroundColor Red
    exit 1 
}

# Init
Write-Host "Initializing..." -ForegroundColor Green
git init

# Add all files
Write-Host "Adding all files..." -ForegroundColor Green
git add .

# Commit
Write-Host "Committing..." -ForegroundColor Green
git commit -m "Initial commit: Django + Next.js full stack project structure"

# Set main branch
Write-Host "Setting main branch..." -ForegroundColor Green
git branch -M main

# Add remote
Write-Host "Adding remote..." -ForegroundColor Green
git remote add origin https://github.com/Oshioxi2003/structure.git 2>$null

# Push
Write-Host ""
Write-Host "Ready to push to GitHub!" -ForegroundColor Yellow
$confirm = Read-Host "Continue? (Y/N)"

if ($confirm -eq 'Y' -or $confirm -eq 'y') {
    git push -u origin main
    Write-Host ""
    Write-Host "Done! Check: https://github.com/Oshioxi2003/structure" -ForegroundColor Green
} else {
    Write-Host "Run 'git push -u origin main' when ready." -ForegroundColor Yellow
}
