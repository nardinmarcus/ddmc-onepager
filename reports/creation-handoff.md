# Creation Handoff — ddmc-onepager v1.0.0

## What Shipped

面向叮咚买菜上海东区「一线下发」场景的单文件竖版长图生成 skill：
四型模板（T1 宣导 / T2 红线 / T3 解读杂志风 / T4 战报 DATA 驱动）+ 5W2H 检查透镜 +
内容契约（references/content-contract.md）+ 已验证产线（references/production.md）。

## Reference Skills Studied

`ddmc-referral-poster`、`ddmc-analysis-report`、`ddmc-summer-pk-diagnostic`、
`ddmc-electricity-usage-analyzer`、`kami`、`lieflat-charts`（见 reports/prior-art-research.md 台账）。

## Candidate-Specific Lessons（用户 2026-11-11 定版）

1. 内容主权高于模板完备性：源内容没有的模块一律不造
2. 零分隔线：卡片 + 色块面板 + 胶囊，替代一切线条
3. 默认一屏 ≤1700px；压高度靠间距与删内容，不缩字号
4. 能图不文：可图化内容（对比/流程/数量）画 SVG/图形
5. 页眉「上海东区」全页仅品牌牌一处；页脚仅发文单位+日期
6. 交付物只有 HTML，PNG 由使用者浏览器一键导出；生成后默认浏览器打开

## Evidence Inventory

- 结构校验：namoo-skill-creator `validate_skill.py` 全项 pass（本仓库 reports 同步）
- 触发评估：`trigger_eval.py` 词法冒烟（lexical smoke），非 provider-backed 证据
- 版式 QA：六件产物（4 模板 + 2 成品）截图 vision 自检通过；全部模板 `node --check` 通过
- 内容忠实：大闸蟹成品逐段对照原始内容，零自造模块

## Missing Evidence（如实声明）

- 未运行 provider-backed 行为对照评估（with-skill/baseline）
- 未做人工盲评（human blind review）
- 外部先例未逐一拉源码（仅 skills.sh 元数据级审阅）

## Rejections

- 外部三个 skills.sh 候选（图像生成路线/证据不足）
- V1 多线条大字报版式（用户否决，本版废弃）
- examples 含内部 SOP 的真实成品**未**随公开发布（发布版不含 examples/）
