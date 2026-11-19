# 生产流程 — 契约 → 填槽 → 校验 → 归档交付

> **交付物只有 HTML。** PNG 由使用者打开 HTML 点「保存为图片」按钮自行导出
> （html2canvas，scale=2 高清）。**产线无截图环节**（2026-11-19 用户定版：
> 生成阶段不截图，质量靠组装脚本确定性 + node --check + 写内容时对照契约自查）。

## 流程

1. **契约先行**：按 `content-contract.md` 在对话里先列 5W2H 七槽位草稿；
   用户输入缺关键槽位（无生效日期/无处罚标准）→ 一句话问补，其余自主填。
2. **选模板**：直接引用 `templates/` 内对应 Tx 原文件（中文文件名无碍——
   python 读文件不走 CDP），**无需复制改名**。
3. **填槽**：只动内容区与 DATA 块，**不动版式 CSS、结构 class、尺寸（960px 宽）**；
   每个槽位有 `═══ 槽位` 注释定位。模板里的示例内容必须整段替换，不得残留。
   **品牌牌已内嵌**：头带右侧「上海东区 | 叮咚买菜logo」白色圆角牌在四套模板中统一内置
   （base64 data URI，母版 `assets/ddmc-logo.jpg`），填槽时不需要动。
   **快速产线（默认走法）**：内容区**单独写一个文件**（logo 用 `__LOGO__` 占位），组装+校验
   交给 `scripts/build_qa.py`；**禁一次性 write 整页 HTML**——logo base64 约 8KB
   会超 LLM 单次输出上限截断整轮（实测浪费 30+ 分钟）。
   写内容区时直接对照契约自查：无自造模块、零分隔线、字号地板、色板角色。
4. **组装 + JS 校验**（秒级）：
   ```bash
   py -3 <skill目录>/scripts/build_qa.py assemble <模板.html> <内容区.html> <输出.html>
   ```
   自动：提取品牌牌 base64 注入 → 头尾拼接（title/下载名同步输出文件名）→
   提内联 script `node --check`。输出文件名直接用归档名。
5. **归档**：assemble 输出即归档，命名 `一页纸_{模块}_{主题}_{YYYYMMDD}.html`。
   - 标准宣导/红线类 → `30_Resources/运营标准/一页纸/`
   - 考核解读类 → `30_Resources/绩效考核/`
   - 项目/战报类 → `20_Projects/<对应项目>/`
   - 实在归属不明 → `30_Resources/运营标准/一页纸/`
6. **交付**：**默认直接在浏览器打开生成的 HTML**：
   `explorer.exe "D:\...\一页纸_xxx.html"`（调用默认浏览器，供即时复核与点「保存为图片」导出；
   explorer 返回非零码属正常）。需要在线转发时按 `ddmc-analysis-report` 坑位里的
   QuickShare API 方式上传（JSON POST，非 share.sh）。

## 坑位（一页纸场景特有 + 继承）

1. **html2canvas CDN 离线/被墙**：使用者点「保存为图片」会 alert 失败——联网后重试即可；
   大字报系模板刻意零 web font 依赖（系统字体栈），页面渲染本身不受影响。
2. **CDP/浏览器（agent-browser）开中文 file:// 路径报 main-frame-error**（继承）：
   仅当例外场景需要 CDP 截图时，先复制成 ASCII 文件名再开，检完删临时件；
   explorer.exe 交付路径不受影响。
3. **T4 进度条以「目标×1.4」为满格**：超目标很多的指标会顶满格，视觉上"好到溢出"，
   属预期；若要更精确比例，改渲染函数里的 1.4 系数，其余不动。
4. **数字 tabular-nums 已全局开**（T3/T4），填数字不要手动对齐空格。
5. **导出按钮在 `#sheet` 之外**（fixed 定位）：不进页内导出 PNG（html2canvas 只截 `#sheet`）。
6. **品牌牌 logo 是 base64 内嵌**：无 CORS/离线问题；如需换 logo，替换
   `assets/ddmc-logo.jpg` 后重新 base64 注入（模板 4 处 + 存量成品同步）。
7. **python subprocess 调 agent-browser daemon 冷启动必挂**（bash 正常；实测多轮）：
   涉及 agent-browser 的操作一律 bash 层直接调，勿写进 python 脚本；
   截图路径用绝对路径（相对路径基于 daemon 启动 cwd）。

## 产出自检底线

- node --check 通过 + 数字抽查（每张至少核对一个数字出处），才允许交付 HTML。
- 视觉问题由使用者打开 HTML 即时复核发现，迭代修改只重写内容区文件重跑 assemble。
