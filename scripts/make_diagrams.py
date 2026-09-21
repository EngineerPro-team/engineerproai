#!/usr/bin/env python3
"""Brand diagrams for roadmap + 6 course syllabi."""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs" / "assets" / "img" / "diagrams"
BLUE = "#1862FF"
NAVY = "#0B1F3D"
MUTED = "#5A6B86"
ICE = "#EEF4FF"
WHITE = "#FFFFFF"
FONT = "Sora, Be Vietnam Pro, ui-sans-serif, system-ui, sans-serif"


def svg(w: int, h: int, inner: str, label: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="gline" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#7AA4FF"/>
      <stop offset="100%" stop-color="{BLUE}"/>
    </linearGradient>
    <linearGradient id="gcard" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7FAFF"/>
      <stop offset="100%" stop-color="#E4EEFF"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0B1F3D" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" rx="28" fill="url(#gcard)"/>
{inner}
</svg>
'''


def hexagon(cx: float, cy: float, r: float, fill: str, stroke: str | None = None) -> str:
    pts = []
    import math
    for i in range(6):
        a = math.radians(-90 + i * 60)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    s = f' stroke="{stroke}" stroke-width="2"' if stroke else ""
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"{s}/>'


def roadmap() -> str:
    nodes = [
        ("AE01", "T1–2", "Productivity", 110),
        ("AE02", "T3–4", "Math for ML", 290),
        ("AE03", "T5–6", "ML Foundations", 470),
        ("AE04", "T7–8", "Deep Learning", 650),
        ("AE05", "T9–10", "System Design", 830),
        ("AE06", "T11–12", "Frontier Lab", 1010),
    ]
    parts = [
        f'<text x="40" y="48" font-family="{FONT}" font-size="22" font-weight="700" fill="{NAVY}">Lộ trình 12 tháng · 6 học phần</text>',
        f'<text x="40" y="74" font-family="{FONT}" font-size="13" fill="{MUTED}">Mentor review từ Big Tech · GPU lab · portfolio có thể bảo vệ</text>',
        f'<path d="M110 200 H1010" stroke="url(#gline)" stroke-width="6" stroke-linecap="round"/>',
    ]
    for code, months, name, x in nodes:
        parts.append(f'<g filter="url(#soft)">')
        parts.append(hexagon(x, 200, 52, WHITE, BLUE))
        parts.append(hexagon(x, 200, 40, BLUE))
        parts.append(f'<text x="{x}" y="206" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="{WHITE}">{code}</text>')
        parts.append("</g>")
        parts.append(f'<text x="{x}" y="278" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="700" fill="{BLUE}">{months}</text>')
        parts.append(f'<text x="{x}" y="298" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{NAVY}">{name}</text>')
    parts.append(f'<text x="560" y="348" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{MUTED}">48 tuần học + 4 tuần dự phòng lễ / học bù / hoàn thiện portfolio</text>')
    return svg(1120, 380, "\n".join(parts), "Lộ trình 12 tháng sáu học phần AE01 đến AE06")


def ae01() -> str:
    steps = ["L0 Baseline", "L1 Assist", "L2 Collab", "L3 Delegate", "L4 Spec team", "L5 Factory"]
    parts = [
        f'<text x="40" y="46" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">AE01 · Năng suất AI theo cấp độ kỹ sư Big Tech</text>',
        f'<text x="40" y="70" font-family="{FONT}" font-size="13" fill="{MUTED}">Từ dùng AI hỗ trợ đến software factory — cùng mentor review</text>',
    ]
    for i, label in enumerate(steps):
        x = 70 + i * 175
        h = 70 + i * 22
        y = 300 - h
        parts.append(f'<rect x="{x}" y="{y}" width="150" height="{h}" rx="16" fill="{BLUE}" opacity="{0.45 + i * 0.09}"/>')
        parts.append(f'<text x="{x + 75}" y="{y - 12}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="{NAVY}">{label}</text>')
        if i < 5:
            parts.append(f'<path d="M{x + 158} {y + h/2} l14 0" stroke="{BLUE}" stroke-width="3" marker-end="url(#arr)"/>')
    parts.append(f'<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{BLUE}"/></marker></defs>')
    return svg(1120, 360, "\n".join(parts), "Thang năng lực AE01 từ L0 đến L5")


def ae02() -> str:
    boxes = [
        (80, "Đại số", "Vector · SVD"),
        (340, "Giải tích", "Gradient · chain"),
        (600, "Xác suất", "Bayes · MLE"),
        (860, "Tối ưu", "GD · regularize"),
    ]
    parts = [
        f'<text x="40" y="48" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">AE02 · Toán cho ML: trực giác → công thức → NumPy</text>',
        f'<path d="M155 190 H965" stroke="url(#gline)" stroke-width="5" stroke-linecap="round"/>',
    ]
    for x, t, s in boxes:
        parts.append(f'<g filter="url(#soft)"><rect x="{x}" y="130" width="190" height="120" rx="22" fill="{WHITE}" stroke="{BLUE}" stroke-width="1.5"/>')
        parts.append(hexagon(x + 95, 168, 22, BLUE))
        parts.append(f'<text x="{x + 95}" y="220" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="700" fill="{NAVY}">{t}</text>')
        parts.append(f'<text x="{x + 95}" y="242" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{MUTED}">{s}</text></g>')
    parts.append(f'<text x="560" y="310" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{MUTED}">Đầu ra: notebook kiểm tra gradient, similarity, projection, ước lượng xác suất</text>')
    return svg(1120, 340, "\n".join(parts), "Bốn trụ toán của AE02")


def ae03() -> str:
    labels = [
        ("1. Bài toán", "Target & baseline"),
        ("2. Split", "Tránh leakage"),
        ("3. Fit", "Model + tune"),
        ("4. Eval", "Error analysis"),
        ("5. Artifact", "Pipeline tái lập"),
    ]
    parts = [
        f'<text x="40" y="48" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">AE03 · Pipeline ML đáng tin — từ câu hỏi đến artifact</text>',
    ]
    for i, (t, s) in enumerate(labels):
        x = 50 + i * 215
        parts.append(f'<g filter="url(#soft)"><rect x="{x}" y="110" width="195" height="130" rx="20" fill="{WHITE}"/>')
        parts.append(f'<circle cx="{x + 28}" cy="148" r="16" fill="{BLUE}"/>')
        parts.append(f'<text x="{x + 28}" y="153" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="700" fill="{WHITE}">{i+1}</text>')
        parts.append(f'<text x="{x + 54}" y="154" font-family="{FONT}" font-size="15" font-weight="700" fill="{NAVY}">{t[3:]}</text>')
        parts.append(f'<text x="{x + 20}" y="200" font-family="{FONT}" font-size="13" fill="{MUTED}">{s}</text></g>')
        if i < 4:
            parts.append(f'<path d="M{x + 200} 175 l20 0" stroke="{BLUE}" stroke-width="3"/>')
    parts.append(f'<text x="560" y="290" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{MUTED}">Bảo vệ được: dữ liệu nào dùng để fit, tune, và test</text>')
    return svg(1120, 320, "\n".join(parts), "Pipeline machine learning AE03")


def ae04() -> str:
    layers = [
        (80, 120, "Tensor & Autograd"),
        (80, 190, "MLP · CNN"),
        (400, 120, "Attention / Transformer"),
        (400, 190, "Mini LM + LoRA"),
        (760, 120, "GPU train"),
        (760, 190, "Model card"),
    ]
    parts = [
        f'<text x="40" y="48" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">AE04 · Từ training loop đến mini language model trên GPU</text>',
        f'<rect x="60" y="90" width="300" height="160" rx="24" fill="{WHITE}" stroke="#D6E4FF"/>',
        f'<rect x="380" y="90" width="300" height="160" rx="24" fill="{WHITE}" stroke="#D6E4FF"/>',
        f'<rect x="740" y="90" width="300" height="160" rx="24" fill="{WHITE}" stroke="#D6E4FF"/>',
        f'<text x="210" y="250" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{BLUE}">Nền tảng</text>',
        f'<text x="530" y="250" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{BLUE}">Sequence models</text>',
        f'<text x="890" y="250" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{BLUE}">Bằng chứng</text>',
    ]
    for x, y, t in layers:
        parts.append(f'<rect x="{x}" y="{y}" width="260" height="44" rx="12" fill="{BLUE}"/>')
        parts.append(f'<text x="{x + 130}" y="{y + 28}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="{WHITE}">{t}</text>')
    return svg(1120, 300, "\n".join(parts), "Lộ trình deep learning AE04")


def ae05() -> str:
    left = ["Bài toán & ràng buộc", "Metric sản phẩm", "Kiến trúc tối thiểu", "Data & feature", "Model release", "Serving & online", "Scale & ops"]
    right = ["API vs self-host", "RAG kiểm chứng", "Inference budget", "Eval / judge", "Tool contract"]
    parts = [
        f'<text x="40" y="48" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">AE05 · System design: 9 bước ML + GenAI production</text>',
        f'<text x="80" y="88" font-family="{FONT}" font-size="13" font-weight="700" fill="{BLUE}">9 bước ML</text>',
        f'<text x="620" y="88" font-family="{FONT}" font-size="13" font-weight="700" fill="{BLUE}">GenAI stack</text>',
    ]
    for i, t in enumerate(left):
        y = 108 + i * 28
        parts.append(f'<rect x="80" y="{y}" width="420" height="24" rx="8" fill="{WHITE}"/>')
        parts.append(f'<rect x="80" y="{y}" width="8" height="24" rx="4" fill="{BLUE}"/>')
        parts.append(f'<text x="100" y="{y + 17}" font-family="{FONT}" font-size="12" fill="{NAVY}">{i+1}. {t}</text>')
    for i, t in enumerate(right):
        y = 108 + i * 36
        parts.append(f'<rect x="620" y="{y}" width="420" height="30" rx="10" fill="{BLUE}"/>')
        parts.append(f'<text x="830" y="{y + 20}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="600" fill="{WHITE}">{t}</text>')
    parts.append(f'<text x="560" y="330" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{MUTED}">Capstone: recommendation/ranking + mock interview LLM/RAG</text>')
    return svg(1120, 360, "\n".join(parts), "Thiết kế hệ thống ML và GenAI AE05")


def ae06() -> str:
    loop = [
        (220, 160, "Đọc paper"),
        (560, 90, "Câu hỏi & giả thuyết"),
        (900, 160, "Thí nghiệm / GPU"),
        (560, 250, "Report & bảo vệ"),
    ]
    parts = [
        f'<text x="40" y="48" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">AE06 · Frontier lab: nghiên cứu như một kỹ năng kỹ sư</text>',
        f'<path d="M300 160 C 380 80, 480 80, 560 110" fill="none" stroke="url(#gline)" stroke-width="4"/>',
        f'<path d="M700 110 C 820 80, 860 120, 900 160" fill="none" stroke="url(#gline)" stroke-width="4"/>',
        f'<path d="M900 190 C 860 250, 720 270, 640 260" fill="none" stroke="url(#gline)" stroke-width="4"/>',
        f'<path d="M480 260 C 360 250, 280 220, 250 190" fill="none" stroke="url(#gline)" stroke-width="4"/>',
    ]
    for x, y, t in loop:
        parts.append(f'<g filter="url(#soft)"><circle cx="{x}" cy="{y}" r="54" fill="{WHITE}" stroke="{BLUE}" stroke-width="3"/>')
        parts.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="{NAVY}">{t}</text></g>')
    return svg(1120, 340, "\n".join(parts), "Vòng nghiên cứu ứng dụng AE06")


def year_cal() -> str:
    months = [
        ("25/11/2026", "AE01", "T4 20:30–22:30 · CN 14:00–16:00"),
        ("23/12/2026", "AE02", "T5 20:30–22:30 · CN 20:30–22:30"),
        ("Sắp công bố", "AE03", "Machine Learning"),
        ("Sắp công bố", "AE04", "Deep Learning + GPU"),
        ("Sắp công bố", "AE05", "ML / GenAI System Design"),
        ("Sắp công bố", "AE06", "Frontier Lab"),
    ]
    parts = [
        f'<text x="40" y="46" font-family="{FONT}" font-size="20" font-weight="700" fill="{NAVY}">Lịch khai giảng — đợt AE01 &amp; AE02 đã chốt</text>',
        f'<text x="40" y="70" font-family="{FONT}" font-size="13" fill="{MUTED}">AE01: 16 buổi từ 25/11/2026. AE02: 16 buổi từ 23/12/2026. Giờ GMT+7.</text>',
    ]
    for i, (m, code, name) in enumerate(months):
        col, row = i % 3, i // 3
        x = 50 + col * 350
        y = 100 + row * 175
        parts.append(f'<g filter="url(#soft)"><rect x="{x}" y="{y}" width="330" height="150" rx="22" fill="{WHITE}"/>')
        parts.append(f'<rect x="{x}" y="{y}" width="330" height="8" rx="4" fill="{BLUE}"/>')
        parts.append(f'<text x="{x + 165}" y="{y + 48}" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{BLUE}">{m}</text>')
        parts.append(f'<text x="{x + 165}" y="{y + 84}" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="{NAVY}">{code}</text>')
        parts.append(f'<text x="{x + 165}" y="{y + 116}" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{MUTED}">{name}</text></g>')
    parts.append(f'<text x="560" y="460" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{MUTED}">AE01–AE02: 2 giờ / buổi · 2 buổi / tuần · 8 tuần · GMT+7</text>')
    return svg(1120, 490, "\n".join(parts), "Lịch khai giảng AE01 25/11/2026 và AE02 23/12/2026")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "roadmap-12.svg": roadmap(),
        "ae01-levels.svg": ae01(),
        "ae02-math.svg": ae02(),
        "ae03-pipeline.svg": ae03(),
        "ae04-dl.svg": ae04(),
        "ae05-system.svg": ae05(),
        "ae06-research.svg": ae06(),
        "year-calendar.svg": year_cal(),
    }
    for name, content in files.items():
        (OUT / name).write_text(content)
        print("wrote", name)


if __name__ == "__main__":
    main()
