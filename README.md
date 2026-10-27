# company-research-skill

**边界：** 本 skill 只辅助复现 2026-10-27 个贷报告最终版的水准，不另立标准、不扭曲今天已定的结构与规则。Alexandria／Superpowers 只借目录与硬门槛写法。

Grok Bot skill：**公司课题研究**（本地 workflows id 可能仍为 `cross-country-credit-report`）。

结构参考 **Alexandria**（硬门槛、`references/`、`scripts/`、交付前检查）与 **Superpowers**（先 brainstorm／HARD-GATE、verification-before-completion、红旗表）。

## 布局

```
SKILL.md                 # 编排：何时用、硬门槛、工作流
references/
  story-outline.md       # 第 1 页六个问题
  page-architecture.md
  writing-rules.md
  self-audit.md
  codex-review.md
  pitfalls.md
scripts/
  pdf_audit.py           # 孤行／越界／禁用词
README.md
```

## 使用

1. 用户给标题 → 先出故事大纲，等确认。
2. 再研究、排版、自查、Codex 复核。
3. 只交一份 PDF。

Bot 内 pill：以当前 workflows 里登记的名为准。改本仓后请同步到 bot workflows。
