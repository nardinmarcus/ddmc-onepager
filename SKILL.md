---
name: ddmc-onepager
description: |
  设计并生成叮咚买菜上海东区「一线下发一页纸」：单主题竖版长图 HTML（960px 宽，默认一屏 ≤1700px，html2canvas 一键导出 PNG，微信群直发）。
  用户要「出一页纸 / 宣导页 / 下发一线 / 大字报 / 红线宣导 / SOP 变更宣导 / 新标准宣导 / 考核解读一页纸 / 战报通报一页纸 / 讲清楚一件事 / one-pager」时使用。
  四型模板：T1 宣导（SOP/标准/操作）、T2 红线（安全/合规/稽核）、T3 解读（考核/制度，杂志风）、T4 战报（数据通报，DATA 块驱动）。
  内容主权：结构忠于原始内容，源内容没有的模块（FAQ/WHY/考核）不造不补；零分隔线；标签胶囊化；能图不文。
  不要用于：UE/费用分析报告（ddmc-analysis-report）、夏战 PK 诊断（ddmc-summer-pk-diagnostic）、内推排名海报（ddmc-referral-poster）、多页深度报告——一页纸是执行宣导文体。
argument-hint: 出XX一页纸（T1宣导/T2红线/T3解读/T4战报）| 主题 + 内容来源
---

# 一页纸生成器 V2（忠于内容 × 卡片胶囊 × 能图不文）

把一个具体业务方面讲清楚成一页竖版长图，发到一线微信群。
规范全文：[references/content-contract.md](references/content-contract.md)（内容契约）、[references/production.md](references/production.md)（产线+QA）。

## 四条铁律

1. **忠于内容**：结构由内容决定；源内容没有的模块（FAQ/WHY/考核/责任人）不造不补，对应 section 直接删；5W2H 只是检查透镜。
2. **零分隔线**：白卡片 + 色块面板 + 留白区分模块，禁一切实线/虚线。
3. **胶囊化**：标签、标记、徽章一律圆角胶囊。
4. **能图不文**：流程/对比/构成/数量关系用静态内嵌 SVG/图形，不写干瘪文字。

## 模板矩阵

| 型 | 文件 | 用途 |
|---|---|---|
| T1 | templates/T1-宣导-大字报.html | SOP/标准/操作宣导 |
| T2 | templates/T2-红线-大字报.html | 红线/安全/合规/稽核 |
| T3 | templates/T3-解读-杂志风.html | 考核/制度/政策解读（衬线杂志风） |
| T4 | templates/T4-战报-大字报.html | 数据战报/排名/复盘（DATA 块驱动） |

## 硬规则

1. 内容先行：先读原始内容、列卡片结构规划；按契约 §1 选型；一个主题只出一张。
2. 只填不改：只动内容区/DATA 块与增删 section，不动版式 CSS 与 960px 宽度。
3. 数字回源：所有数字从源文件/看板核对；处罚/达标线不确定就问，不编。
4. 色板：主 #009999 青蓝 / 次 #00A500 绿（正向）/ 强调 #E34234 朱砂（禁止）/ 文字 #32312D 墨色（禁纯黑）/ 警示 #F37021 爱马仕橙（注意）。
5. 密度：默认一屏 ≤1700px；字号地板 14.5/17/44/12.5px；压高度靠间距与删内容，不缩字号。
6. 交付前 node --check + QA 截图 vision 自检（production.md），不通过不交付；**交付物只有 HTML**，PNG 由使用者浏览器内点「保存为图片」导出。

## 流程

读内容 → 卡片结构规划 → 复制模板（ASCII 临时名）→ 填槽/删多余 section → JS 校验 → QA 截图自检 → 归档 `一页纸_{模块}_{主题}_{YYYYMMDD}.html` → 默认 `explorer.exe` 浏览器打开交付。
归档：标准/红线类 `30_Resources/运营标准/一页纸/`；考核类 `30_Resources/绩效考核/`；项目类 `20_Projects/<项目>/`。

## 示例

- examples/宣导示例-前置仓6S要点.html（T1）
- 30_Resources/运营标准/一页纸/一页纸_水产运营_捆绑大闸蟹操作_20261111.html（T1，含 SVG 图示示范）

## Task-End Skill Improvement Review

任务结束如出现可复用修正，在交付说明里列出「Skill 改进待审」条目（**明确 item ID**：问题→建议→影响范围），经 Daddy 确认后逐条回写本 SKILL.md 或 references，不自动改、不合并默认通过。
