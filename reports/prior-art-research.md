# Prior-Art Research — ddmc-onepager（2026-11-11）

## Sources Consulted

1. **Vault 内部 skill（一手先例，最高相关）**
   - `ddmc-referral-poster`：单文件竖版 HTML（960×1707）+ DATA 块填充 + html2canvas 导出 PNG + 品牌色板 — **adapt**
   - `ddmc-analysis-report`：lieflat 报告产线（字号密度红线、node --check、CDP 截图、vision 自检、坑位清单）— **adapt**
   - `ddmc-summer-pk-diagnostic` / `ddmc-electricity-usage-analyzer`：bento/minimal 日报速览、Bold Poster 仪表盘 — **reference**（版式语言素材）
   - `kami`（全局）：契约锁定 + content IR + gap report 方法论 — **adapt**（方法论，不用其模板）
   - `lieflat-charts`（全局）：63 图 catalog、PORCELAIN 色板正本、Glance 快读系 — **reference**（T3/T4 图表选型权威）
2. **外部（skills.sh，`npx skills find "one-pager poster announcement template generator"`，2026-11-11）**
   - `inference-sh/skills@ai-image-generation`（14 installs）— **reject**：图像生成路线，非排版路线
   - `skills.volces.com@poster-designer`（4 installs）— **reject**：同上，且无质量证据
   - `sananthanarayan/skilldrop@marketing-flyer`（1 install）— **reject**：无证据质量，场景不符

## Contribution Ledger

- **invent**：5W2H 作为检查透镜而非填空表（内容主权原则）、零分隔线卡片胶囊视觉系统、默认一屏高度纪律、能图不文原则、页眉去重与页脚精简规范
- **adapt**：referral-poster 的模板+DATA+导出交付形态；analysis-report 的 QA 产线与坑位；kami 的契约先行与 IR 分离
- **reject**：外部三案（见上）；early V1 大字报风的多线条版式（用户 2026-11-11 否决）

## Missing Evidence

- 外部候选仅审至 skills.sh 元数据与索引描述，未逐一拉源码审查
- 未发现与「叮咚前置仓一线下发」同域的公开 skill；同域先例以 vault 内部四个 skill 为准
