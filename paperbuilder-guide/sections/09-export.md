# 导出与教师编译

先保存正文，再导出 LaTeX。生成文件位于当前论文 build 目录，图片会复制进去。PDF 编译需要 latexmk 和 TeX 环境；学生端缺少它们是允许的。

本指南包含中文。新版 PaperBuilder 会自动切换为 XeLaTeX，并加载 ctex 与 TeX Live 自带 Fandol 字体；安装完整 TeX 环境后可以直接编译。英文论文默认仍用 pdflatex。自动切换会在编译提示中说明，不会更改你保存的引擎设置。

教师拉取最新正文和图片，核对版本后编译 PDF。build 默认被 Git 忽略；交付 PDF 需要单独传送。页数警告是辅助检查，不替代实际比赛规则核对。
