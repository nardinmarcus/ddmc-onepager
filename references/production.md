# 生产流程 — 契约 → 填槽 → 校验 → 质检 → 归档交付

> **交付物只有 HTML。** PNG 由使用者打开 HTML 点「保存为图片」按钮自行导出
> （html2canvas，scale=2 高清）。产线中的截图仅作内部 vision 质检，不归档、不交付。

## 流程

1. **契约先行**：按 `content-contract.md` 在对话里先列 5W2H 七槽位草稿；
   用户输入缺关键槽位（无生效日期/无处罚标准）→ 一句话问补，其余自主填。
2. **选模板**：从 `templates/` 整份复制对应 Tx 到产出目录（先复制成 ASCII 临时名再改中文名，
   原因见坑位①）。
3. **填槽**：只动内容区与 DATA 块，**不动版式 CSS、结构 class、尺寸（960px 宽）**；
   每个槽位有 `═══ 槽位` 注释定位。模板里的示例内容必须整段替换，不得残留。
   **品牌牌已内嵌**：头带右侧「上海东区 | 叮咚买菜logo」白色圆角牌在四套模板中统一内置
   （base64 data URI，母版 `assets/ddmc-logo.jpg`），填槽时不需要动。
4. **JS 校验**：
   ```bash
   py -3 -c "import re,sys; open(r'<tmp>.js','w',encoding='utf-8').write(''.join(re.findall(r'<script[^>]*>(.*?)</script>', open(r'<file>.html',encoding='utf-8').read(), re.S)))" && node --check <tmp>.js
   ```
   （CDN script 标签无内容不影响；内联 script 全部提出来 check。）
5. **内部质检截图**（仅 vision 自检用，产物不交付）：
   ```bash
   agent-browser open "file:///C:/.../ascii-name.html"
   agent-browser set viewport 1280 4000   # 高度≥成品高度，否则元素截图被视口截断
   agent-browser screenshot "#sheet" qa.png
   ```
   元素截图是 1x 清晰度——自检足够；不依赖 html2canvas CDN，离线可跑。
6. **vision 自检**（read qa 截图逐项查）：
   - 截图里**不得出现「保存为图片」按钮**（出现=用了整页截图，重截）；
   - 品牌牌完整（上海东区 + logo 无变形）；
   - **忠于内容**：无自造模块（源内容没有的 FAQ/WHY/考核一律不存在）；
   - **零分隔线**：全页无实线/虚线分隔（面板/胶囊边缘不算）；
   - 无溢出/重叠/截断；长标题折行是否压到徽章；
   - 图表/SVG 标签互不重叠、形不压字；
   - 色板角色正确：青蓝=结构、绿=正向、朱砂=禁止、爱马仕橙=注意、墨色=文字（无纯黑）；
   - 字号不低于地板（正文 14.5px/步骤动作 17px/H1 44px/footer 12.5px）；
   - 大字报系浅色底完整（html2canvas backgroundColor 已内置）。
7. **归档**：只归档 HTML，命名 `一页纸_{模块}_{主题}_{YYYYMMDD}.html`。
   - 标准宣导/红线类 → `30_Resources/运营标准/一页纸/`
   - 考核解读类 → `30_Resources/绩效考核/`
   - 项目/战报类 → `20_Projects/<对应项目>/`
   - 实在归属不明 → `30_Resources/运营标准/一页纸/`
8. **交付**：**默认直接在浏览器打开生成的 HTML**：
   `explorer.exe "D:\...\一页纸_xxx.html"`（调用默认浏览器，供即时复核与点「保存为图片」导出；
   explorer 返回非零码属正常）。需要在线转发时按 `ddmc-analysis-report` 坑位里的
   QuickShare API 方式上传（JSON POST，非 share.sh）。

## 坑位（一页纸场景特有 + 继承）

1. **CDP/浏览器开中文 file:// 路径报 main-frame-error**（继承）：QA 截图先复制成
   ASCII 文件名再开，检完删临时件。
2. **html2canvas CDN 离线/被墙**：使用者点「保存为图片」会 alert 失败——联网后重试即可；
   大字报系模板刻意零 web font 依赖（系统字体栈），页面渲染本身不受影响。
3. **agent-browser 元素截图视口截断**：先 `set viewport <宽> <≥成品高度>` 再截；
   元素截图 1x 清晰度，只用于自检，不代表交付质量。
4. **T4 进度条以「目标×1.4」为满格**：超目标很多的指标会顶满格，视觉上"好到溢出"，
   属预期；若要更精确比例，改渲染函数里的 1.4 系数，其余不动。
5. **数字 tabular-nums 已全局开**（T3/T4），填数字不要手动对齐空格。
6. **导出按钮在 `#sheet` 之外**（fixed 定位）：不会进 QA 截图（选择器截图排除），
   也不会进页内导出 PNG（html2canvas 只截 `#sheet`）。
7. **品牌牌 logo 是 base64 内嵌**：无 CORS/离线问题；如需换 logo，替换
   `assets/ddmc-logo.jpg` 后重新 base64 注入（模板 4 处 + 存量成品同步）。

## 产出自检底线

- QA 截图 vision 检查通过，才允许交付 HTML。
- 每张一页纸至少核对一个数字的出处（抽查即可，不必全部）。
