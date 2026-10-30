# company-research-skill

通用研究报告框架与汇报模板 skill（公司／行业／管理课题 → 给决策者看的中文决策简报，默认 A3 横版 PDF）。

只收通用的方法：逻辑与证据、页面框架、排版规范、可填空的汇报模板、流程与交付自查；不含任何一份具体报告的内容。

## 布局

```
SKILL.md                    # 何时用、硬门槛、工作流
references/
  story-outline.md          # 先写回理解与故事大纲
  framework.md              # 首页摘要＋案例页＋借鉴汇总＋附件
  report-template.md        # 各页填空骨架
  logic-and-evidence.md
  layout-rules.md
  review-checklist.md
  self-audit.md
  workflow-delivery.md
  pitfalls.md
scripts/
  pdf_audit.py              # PDF 自查（孤行／越界／禁用词）
```

## 在不同 AI 里使用

- **Codex／Claude Code**：把整个文件夹放进各自的 skills 文件夹（如 `~/.codex/skills/`、`~/.claude/skills/`）。
- **ChatGPT**：把 `SKILL.md` 和 `references/` 下的文件上传为 Project 知识（或自定义 GPT 知识库）；`scripts/` 需在能运行 Python 的环境里使用。
