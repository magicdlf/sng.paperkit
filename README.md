# sng.paperkit

PaperBuilder 的示例论文与功能练习库。应用代码在 https://github.com/magicdlf/sng.paperbuilder ，本库地址为 https://github.com/magicdlf/sng.paperkit 。两者独立克隆，不能用本库替代应用。

## 选一份打开

| 目录 | 内容 |
| --- | --- |
| paperbuilder-guide | 中文操作练习册，每章演示一个功能：编辑、公式、图表、引用、批注、团队分工、Git、导出、代码与 AI 记录 |
| bee-mini-01 | HiMCM 2022 A 蜜蜂主题短草稿，一张种群图，适合快速讨论模型边界 |
| himcm-2022-a-12821 | Outstanding 原文试导入：12821 队，五章正文、图表与参考文献；尚需逐式校对，用于本地样式对比 |
| bee-mini-02 | 同主题三个短段落、两张图，练习季节模型和授粉结论的论证 |

两份蜜蜂材料来自现有原创课堂工地，数字是教学假设，不是实际蜂群观测，也不是获奖论文。刻意保留的缺陷由学生讨论；本库不附教师答案。

## 给本地 AI

先读取应用的 README 与 AI_INSTALL_INSTRUCTIONS.md。询问用户要克隆 PaperKit 体验还是新建自己的论文 Git 仓库；已有论文仓库则让用户提供地址。体验直接使用本库 URL，推荐打开 paperbuilder-guide；新建则在应用与本库之外创建独立目录、git init 并复制内置模板或选定示例。安装前说明依赖内容和大陆 npmmirror 地址，不安装 TeX，教师统一编译即可。

```bash
# 在应用目录之外克隆本库；Windows 也可用 HTTPS
# git clone https://github.com/magicdlf/sng.paperkit.git PaperKit
# 然后回到 PaperBuilder 应用根目录执行
npm ci --registry=https://registry.npmmirror.com --loglevel=info
npm run dev -- --paper "/absolute/path/to/PaperKit/paperbuilder-guide"
# 浏览器打开 http://localhost:5173
```

切换示例：顶栏“打开其它路径…”输入具体论文目录的绝对路径。若要在顶栏列出三份示例，启动前设置 HIMCM_PAPERS_ROOT 为 PaperKit 的绝对路径；仅设置 --paper 不改变列表扫描根目录。不要将库根目录直接作为 --paper。

## 正式团队使用

本库只有一个 Git 仓库，所有示例共享历史；适合练习，不提供组间隔离。选定示例后将其目录内容复制到本库之外的新目录（不要带 .git/build），在新目录 git init，再配置团队自己的私有 remote。不要直接 fork 整个示例库作为正式论文。

学生只拿到可编辑材料，不要将教师说明或答案加入团队仓库。不要提交个人 token、SSH 私钥或真实身份资料。

## Git 与编译

应用内提交是本地提交，而且会纳入整个库工作区；push/pull 通过外部 Git 工具。同步前关闭编辑页面；不要强推。build/ 与 .last-paper 已忽略。

中文指南只用于浏览器演示，不承诺默认 pdflatex 编译。英文蜜蜂示例可用于教师编译验证；其中结论仍须学生核实。
