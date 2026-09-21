#!/usr/bin/env python3
"""Generate EngineerPro AI isometric-E mark as SVG + PNG."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "img"
BLUE = "#1862FF"


def iso_hex(cx: float, cy: float, s: float) -> list[tuple[float, float]]:
    """Isometric cube silhouette (vertical sides, 30°-ish roof). s = center→top."""
    w = s * 0.90
    h = s * 0.52
    return [
        (cx, cy - 2 * h),  # 0 top
        (cx + w, cy - h),  # 1 top-right
        (cx + w, cy + h),  # 2 bottom-right
        (cx, cy + 2 * h),  # 3 bottom
        (cx - w, cy + h),  # 4 bottom-left
        (cx - w, cy - h),  # 5 top-left
    ]


def chevron_band(s_outer: float, s_inner: float, cx: float, cy: float):
    # Open on the left vertical → hexagonal E / C
    seq = [5, 0, 1, 2, 3, 4]
    outer = iso_hex(cx, cy, s_outer)
    inner = iso_hex(cx, cy, s_inner)
    return [outer[i] for i in seq] + [inner[i] for i in reversed(seq)]


def poly(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def mark_paths(cx: float, cy: float, s: float) -> list[list[tuple[float, float]]]:
    # Three bands of similar weight, generous inner aperture (the E counter)
    stroke = s * 0.155
    gap = s * 0.095
    bands = []
    cursor = s
    for _ in range(3):
        bands.append(chevron_band(cursor, cursor - stroke, cx, cy))
        cursor = cursor - stroke - gap
    return bands


def svg_mark(size: int = 512) -> str:
    cx, cy, s = size * 0.52, size * 0.50, size * 0.36
    polys = "\n".join(
        f'  <polygon points="{poly(band)}" fill="{BLUE}"/>' for band in mark_paths(cx, cy, s)
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        f'role="img" aria-label="EngineerPro AI">\n{polys}\n</svg>\n'
    )


def png_from_svg(svg: str, dest: Path, width: int, height: int | None = None) -> None:
    import subprocess
    import tempfile

    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as f:
        f.write(svg)
        tmp = f.name
    geom = f"{width}x{height}" if height else f"{width}x{width}"
    subprocess.check_call(
        ["magick", "-background", "none", tmp, "-resize", geom, str(dest)]
    )


def og_png(dest: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont

    w, h = 1200, 630
    img = Image.new("RGB", (w, h), "#EAF1FF")
    draw = ImageDraw.Draw(img)

    # faint isometric diamonds
    for y_i, y in enumerate(range(-40, h + 80, 56)):
        for x in range(-40, w + 80, 64):
            ox = x + (32 if y_i % 2 else 0)
            draw.polygon(
                [(ox, y - 10), (ox + 16, y), (ox, y + 10), (ox - 16, y)],
                outline="#1862FF18",
            )

    mark = Image.open(OUT / "logo-mark.png").convert("RGBA")
    mark = mark.resize((460, 460), Image.Resampling.LANCZOS)
    img.paste(mark, (40, 85), mark)

    try:
        font_title = ImageFont.truetype(
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf", 54
        )
        font_sub = ImageFont.truetype(
            "/System/Library/Fonts/Supplemental/Arial.ttf", 24
        )
    except OSError:
        font_title = ImageFont.load_default()
        font_sub = font_title

    draw.text((520, 232), "ENGINEERPRO", fill="#1862FF", font=font_title)
    draw.text((520, 300), "AI", fill="#1862FF", font=font_title)
    draw.text((520, 390), "AI/ML Engineering Accelerator", fill="#12233F", font=font_sub)
    img.save(dest, "PNG", optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    mark = svg_mark(512)
    (OUT / "logo-mark.svg").write_text(mark)
    png_from_svg(mark, OUT / "logo-mark.png", 1024)
    png_from_svg(mark, OUT / "apple-touch-icon.png", 180)
    png_from_svg(mark, OUT / "favicon.png", 64)
    png_from_svg(mark, OUT / "favicon-32.png", 32)
    og_png(OUT / "og-share.png")
    print("wrote", sorted(p.name for p in OUT.iterdir()))


if __name__ == "__main__":
    main()
