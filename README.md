# ddmc-onepager · 叮咚一页纸生成器

把**一个具体业务方面**讲清楚成一页竖版长图 HTML（960px 宽，默认一屏 ≤1700px），发到一线微信群。
为叮咚买菜·上海东区前置仓运营场景定制，方法论通用于任何需要"一页纸下发"的团队。

![type:skill](https://img.shields.io/badge/type-agent--skill-blue) ![version](https://img.shields.io/badge/version-1.1.0-green)

## 它解决什么问题

一线下发最怕两件事：**信息失真**（层层转发后走样）和**没人看**（长文档刷屏即沉）。
一页纸用一张竖版长图解决：结构忠于原始内容、3 秒抓住重点、手机上直接看。

四条设计铁律（详见 [references/content-contract.md](references/content-contract.md)）：

1. **忠于内容** —— 页面结构由内容决定；源内容没有的模块（FAQ/WHY/考核）不造不补。5W2H 只是检查透镜，不是填空表
2. **零分隔线** —— 模块用白卡片 + 色块面板 + 留白区分，禁一切实线/虚线
3. **胶囊化** —— 标签、标记、徽章一律圆角胶囊
4. **能图不文** —— 流程/对比/构成/数量关系用静态 SVG/图形表达，不写干瘪文字

## 安装

```bash
npx skills add nardinmarcus/ddmc-onepager
```

## 四型模板

| 型 | 文件 | 用途 |
|---|---|---|
| T1 宣导 | [templates/T1-宣导-大字报.html](templates/T1-宣导-大字报.html) | SOP/标准变更/操作宣导 |
| T2 红线 | [templates/T2-红线-大字报.html](templates/T2-红线-大字报.html) | 红线/安全/合规/稽核（处罚胶囊 + 警示面板） |
| T3 解读 | [templates/T3-解读-杂志风.html](templates/T3-解读-杂志风.html) | 考核/制度解读（衬线杂志风 + SVG 图表） |
| T4 战报 | [templates/T4-战报-大字报.html](templates/T4-战报-大字报.html) | 数据战报/排名/复盘（DATA 块驱动） |

每套模板：头带品牌牌（左模块名 + 右「上海东区 \| logo」）→ 内容卡片 → 极简页脚。
色板：主色 `#009999` 青蓝 · 次要 `#00A500` 绿 · 强调 `#E34234` 朱砂红 · 文字 `#32312D` 墨色 · 警示 `#F37021` 爱马仕橙。

## 用法（对 agent 说）

```
出「捆绑大闸蟹操作」一页纸，内容如下：
① 到货及暂养：到货要求不打样不得拒收；……
```

Agent 会：读内容 → 给卡片结构规划 → 选型填充 → 内容区单独成文 → `scripts/build_qa.py` 组装（logo 注入 + 头尾拼接 + node --check，秒级）→ **默认浏览器打开 HTML**。产线无截图环节，质量靠组装脚本确定性 + 校验 + 契约自查。

## 导出 PNG

浏览器打开 HTML → 点右下角「**保存为图片**」（html2canvas，scale=2 高清）→ 直接发微信群。
Skill 只交付 HTML，PNG 由使用者自行导出。

## 自然触发示例（你可以直接这样说）

- 「出『捆绑大闸蟹操作』一页纸，内容如下：……」
- 「把这条打包新标准做成宣导页下发一线」
- 「仓内六条红线做成红线宣导一页纸」
- 「9 月考核权重变化，出一页考核解读」
- 「M9 上半场经营战报一页纸，KPI 和战区排名」

## 验证

```bash
# 结构校验（namoo 包标准）
py -3 validate_skill.py <skill目录>
# 触发冒烟评估
py -3 trigger_eval.py <skill目录> --cases evals/trigger_cases.json
# 全部模板 JS 语法
node --check <提取的内联脚本>
```

## Troubleshooting

- **点「保存为图片」没反应/报错**：html2canvas 走 CDN，需联网；离线时用浏览器自带截图或无头浏览器截 \ 元素
- **T3 衬线字体没生效**：Google Fonts 加载慢，等字体就绪后重截
- **浏览器打不开中文路径**：先把 HTML 复制成 ASCII 文件名再开
- **内容超一屏太多**：按契约删减顺序压缩（去重复 → 短句化 → 拆页），别缩字号

## 定制

- **换 logo**：替换 `assets/ddmc-logo.jpg`，重新 base64 注入各模板头带
- **归档路径**：模板内的归档路径是 ddmcvault 仓库约定，可按自己仓库结构修改
- **触发词**：一页纸 / 宣导 / 下发一线 / 红线宣导 / 考核解读 / 战报通报 / one-pager

## 结构

```
├── SKILL.md                    # 路由 + 四条铁律 + 硬规则
├── references/
│   ├── content-contract.md     # 内容契约（忠于内容/零线条/胶囊/色板/高度）
│   └── production.md           # 生产流程 + QA 清单 + 坑位
├── scripts/build_qa.py         # 组装产线：logo 注入 + 头尾拼接 + node --check
├── templates/                  # 四型单文件 HTML 模板（零外部依赖，仅 html2canvas CDN）
├── examples/                   # 成品示例（T1 宣导）
├── assets/ddmc-logo.jpg        # 品牌牌 logo 母版
├── agents/interface.yaml
├── evals/trigger_cases.json
├── manifest.json
└── reports/skill-ir.json
```

## 前提与边界

- 需要 agent 具备文件读写能力 + Python 3 与 Node.js（组装与 JS 校验用）
- 不用于：多页分析报告、数据看板、通用 PPT —— 一页纸是**执行宣导文体**，不是分析文体
- 本 skill 为叮咚买菜内部运营场景定制；模板与契约可复用，品牌元素请替换为自己的

## License

MIT
