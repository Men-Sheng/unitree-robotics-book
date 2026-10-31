# 宇树机器人深度拆解书 - GitHub 上传脚本
# 使用方法：右键点击此文件 -> 使用 PowerShell 运行

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  宇树机器人深度拆解书 - GitHub 上传  " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# 检查 Git 是否已安装
Write-Host "检查 Git 安装状态..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git 已安装: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git 未安装!" -ForegroundColor Red
    Write-Host ""
    Write-Host "请先安装 Git:" -ForegroundColor Yellow
    Write-Host "  方法1: 访问 https://git-scm.com/download/win" -ForegroundColor White
    Write-Host "  方法2: 运行命令 winget install --id Git.Git -e" -ForegroundColor White
    Write-Host ""
    Read-Host "按任意键退出"
    exit 1
}

# 检查 GitHub CLI 是否已安装
Write-Host ""
Write-Host "检查 GitHub CLI 安装状态..." -ForegroundColor Yellow
try {
    $ghVersion = gh --version
    Write-Host "✓ GitHub CLI 已安装" -ForegroundColor Green
    $useGH = $true
} catch {
    Write-Host "! GitHub CLI 未安装，将使用传统方式" -ForegroundColor Yellow
    $useGH = $false
}

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan

# 配置 Git 用户信息
Write-Host ""
Write-Host "配置 Git 用户信息" -ForegroundColor Yellow
$userName = Read-Host "请输入你的 GitHub 用户名"
$userEmail = Read-Host "请输入你的 GitHub 邮箱"

git config --global user.name "$userName"
git config --global user.email "$userEmail"
Write-Host "✓ Git 用户信息配置完成" -ForegroundColor Green

# 初始化 Git 仓库
Write-Host ""
Write-Host "初始化 Git 仓库..." -ForegroundColor Yellow
git init
Write-Host "✓ Git 仓库初始化完成" -ForegroundColor Green

# 添加所有文件
Write-Host ""
Write-Host "添加文件到 Git..." -ForegroundColor Yellow
git add .
Write-Host "✓ 文件添加完成" -ForegroundColor Green

# 创建第一次提交
Write-Host ""
Write-Host "创建提交..." -ForegroundColor Yellow
git commit -m "首次提交：全球首本宇树机器人深度拆解书"
Write-Host "✓ 提交创建完成" -ForegroundColor Green

# 推送到 GitHub
Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  准备上传到 GitHub  " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

if ($useGH) {
    # 使用 GitHub CLI
    Write-Host "使用 GitHub CLI 创建仓库..." -ForegroundColor Yellow
    Write-Host ""

    # 检查是否已登录
    $authStatus = gh auth status 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "需要登录 GitHub..." -ForegroundColor Yellow
        gh auth login
    }

    $repoName = Read-Host "请输入仓库名称 (默认: unitree-robotics-book)"
    if ([string]::IsNullOrWhiteSpace($repoName)) {
        $repoName = "unitree-robotics-book"
    }

    $isPublic = Read-Host "设为公开仓库? (Y/n)"
    $visibility = if ($isPublic -eq "n" -or $isPublic -eq "N") { "--private" } else { "--public" }

    Write-Host ""
    Write-Host "正在创建仓库并推送..." -ForegroundColor Yellow
    gh repo create $repoName $visibility --source=. --remote=origin --push

    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "=====================================" -ForegroundColor Green
        Write-Host "  ✓ 上传成功！  " -ForegroundColor Green
        Write-Host "=====================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "仓库地址: https://github.com/$userName/$repoName" -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "✗ 上传失败，请检查错误信息" -ForegroundColor Red
    }

} else {
    # 传统方式
    Write-Host "使用传统方式上传" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "请手动完成以下步骤:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. 访问 https://github.com/new" -ForegroundColor White
    Write-Host "2. 创建新仓库，建议名称: unitree-robotics-book" -ForegroundColor White
    Write-Host "3. 设为公开仓库（Public）" -ForegroundColor White
    Write-Host "4. 不要勾选 'Initialize with README'" -ForegroundColor White
    Write-Host "5. 点击 'Create repository'" -ForegroundColor White
    Write-Host ""

    $repoUrl = Read-Host "创建完成后，请输入仓库 URL (例如: https://github.com/username/repo-name.git)"

    Write-Host ""
    Write-Host "正在添加远程仓库..." -ForegroundColor Yellow
    git remote add origin $repoUrl
    git branch -M main

    Write-Host "正在推送到 GitHub..." -ForegroundColor Yellow
    git push -u origin main

    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "=====================================" -ForegroundColor Green
        Write-Host "  ✓ 上传成功！  " -ForegroundColor Green
        Write-Host "=====================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "仓库地址: $repoUrl" -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "✗ 推送失败" -ForegroundColor Red
        Write-Host ""
        Write-Host "可能的原因:" -ForegroundColor Yellow
        Write-Host "  1. 仓库 URL 不正确" -ForegroundColor White
        Write-Host "  2. 需要配置 GitHub 身份验证" -ForegroundColor White
        Write-Host "  3. 需要使用个人访问令牌（PAT）" -ForegroundColor White
        Write-Host ""
        Write-Host "请参考 '如何上传到GitHub.md' 文件获取详细帮助" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "接下来你可以:" -ForegroundColor Yellow
Write-Host "  • 访问 GitHub 仓库页面查看效果" -ForegroundColor White
Write-Host "  • 分享仓库链接给其他人" -ForegroundColor White
Write-Host "  • 在 Issues 中收集反馈" -ForegroundColor White
Write-Host "  • 继续完善书籍内容" -ForegroundColor White
Write-Host ""

Read-Host "按回车键退出"
