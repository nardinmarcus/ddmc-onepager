#!/usr/bin/env python3
"""ddmc-onepager 产线：组装 + JS 校验（无截图环节，2026-11-19 用户定版）。

用法:
  py -3 build_qa.py assemble <模板.html> <内容区.html> <输出.html>

约定:
  - 模板直接引用 skill 内 templates/ 原文件（中文文件名无碍——python 读文件
    不走 CDP），无需复制；输出文件名直接用归档名（title/下载名自动同步）。
  - 内容区文件 = <div class="sheet"> 之后到 </div> 之前的全部 section，
    logo 用 __LOGO__ 占位（脚本注入模板中的 base64）。
  - 禁止一次性 write 整页 HTML：模板 logo base64 约 8KB，整页写会超
    LLM 单次输出上限截断；内容区单独写永不超限。
  - 交付：explorer.exe 打开 HTML，使用者点「保存为图片」导出 PNG；
    产线不做截图/vision 质检。
"""
import re
import subprocess
import sys
from pathlib import Path

SHEET_OPEN = '<div class="sheet" id="sheet">'
TAIL_MARK = '<script src="https://cdn.jsdelivr'


def die(msg: str) -> None:
    print(f"[build_qa] ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def node_check(out: str) -> None:
    js = "".join(re.findall(r"<script[^>]*>(.*?)</script>", out, re.S))
    Path("_check.js").write_text(js, encoding="utf-8")
    # stdin=DEVNULL：node 在继承的管道 stdin 下可能挂起（实测）
    r = subprocess.run("node --check _check.js", shell=True, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=60,
                       stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        die(f"node --check failed:\n{(r.stdout or '') + (r.stderr or '')}")
    print("[build_qa] node --check OK")


def assemble(tpl_p: Path, body_p: Path, out_p: Path) -> None:
    tpl = tpl_p.read_text(encoding="utf-8")
    body = body_p.read_text(encoding="utf-8")

    # 组装：模板头 + 内容区(注入 logo) + 模板尾
    m = re.search(r'bp-area">[^<]*</span><img src="data:image/jpeg;base64,([^"]+)', tpl)
    if not m or SHEET_OPEN not in tpl or TAIL_MARK not in tpl:
        die("模板缺少品牌牌 base64 / sheet 开标签 / jsdelivr 脚本标记")
    out = (tpl[:tpl.index(SHEET_OPEN) + len(SHEET_OPEN)]
           + "\n" + body.replace("__LOGO__", m.group(1))
           + "\n</div>\n\n" + tpl[tpl.index(TAIL_MARK):])
    stem = out_p.stem
    out = re.sub(r"<title>.*?</title>", f"<title>{stem}</title>", out, count=1)
    out = re.sub(r"link\.download='[^']*'", f"link.download='{stem}.png'", out)
    out_p.write_text(out, encoding="utf-8")
    print(f"[build_qa] assembled -> {out_p} ({len(out)} chars)")
    node_check(out)


def main() -> None:
    if len(sys.argv) == 5 and sys.argv[1] == "assemble":
        assemble(*[Path(p) for p in sys.argv[2:5]])
    else:
        die("usage: build_qa.py assemble <模板.html> <内容区.html> <输出.html>")


if __name__ == "__main__":
    main()
