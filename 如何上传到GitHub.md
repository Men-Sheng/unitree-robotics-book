# 如何上传到 GitHub

由于系统权限限制，需要你手动完成以下步骤：

## 第一步：安装必要工具

### 1. 安装 Git

访问 https://git-scm.com/download/win 下载并安装 Git for Windows

或者使用 winget 命令：
```powershell
winget install --id Git.Git -e --source winget
```

### 2. 安装 GitHub CLI（可选，但推荐）

访问 https://cli.github.com/ 下载

或者使用 winget：
```powershell
winget install --id GitHub.cli -e --source winget
```

安装完成后，**重启 PowerShell 终端**

---

## 第二步：配置 Git

打开 PowerShell，运行以下命令：

```powershell
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱@example.com"
```

---

## 第三步：登录 GitHub

使用 GitHub CLI 登录（推荐）：

```powershell
gh auth login
```

按照提示选择：
1. GitHub.com
2. HTTPS
3. Yes (使用 GitHub 凭据)
4. Login with a web browser
5. 复制一次性代码，在浏览器中粘贴

---

## 第四步：初始化并推送到 GitHub

在项目目录 `D:\project\YU-SHU` 中运行：

```powershell
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 创建第一次提交
git commit -m "首次提交：宇树机器人深度拆解书"

# 在 GitHub 上创建仓库（使用 GitHub CLI）
gh repo create unitree-robotics-book --public --source=. --remote=origin --push

# 或者手动创建（如果没有 GitHub CLI）
# 1. 访问 https://github.com/new
# 2. 创建名为 unitree-robotics-book 的公开仓库
# 3. 然后运行：
git remote add origin https://github.com/你的用户名/unitree-robotics-book.git
git branch -M main
git push -u origin main
```

---

## 第五步：验证上传

访问你的 GitHub 仓库页面，应该能看到：

- ✅ README.md 显示精美的介绍页面
- ✅ 所有文件都已上传
- ✅ 封面图、PDF、EPUB 文件都在
- ✅ 目录截图和介绍图都在对应文件夹中

---

## 常见问题

### Q: 推送时要求输入用户名和密码？

A: GitHub 已不支持密码认证，需要使用：
- **方法1**：使用 GitHub CLI（推荐）：`gh auth login`
- **方法2**：创建个人访问令牌（PAT）
  1. 访问 https://github.com/settings/tokens
  2. 生成新令牌（classic）
  3. 勾选 `repo` 权限
  4. 复制令牌，在推送时作为密码使用

### Q: 文件太大无法推送？

A: Git 对单个文件有 100MB 限制。如果 PDF 或 EPUB 过大：
- 考虑使用 Git LFS：`git lfs install`
- 或者在 Releases 页面上传大文件

### Q: 想修改仓库名称？

A: 在 GitHub 仓库页面 → Settings → Repository name 修改

---

## 🎉 完成！

现在你可以：
- 分享你的 GitHub 仓库链接
- 在 README 中添加更多内容
- 接受其他人的 Pull Request 贡献
- 在 Issues 中收集反馈

祝你的书籍项目成功！🚀
