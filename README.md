# EngineerPro AI

Website tĩnh cho chương trình **AI/ML Engineering Accelerator** (6 học phần / 12 tháng).

Live (sau khi bật GitHub Pages):  
https://engineerpro-team.github.io/engineerproai/

Fanpage tư vấn: [facebook.com/EngineerProAI](https://www.facebook.com/EngineerProAI)

## Cấu trúc

```
docs/                 ← GitHub Pages root (Source: main / docs)
  index.html
  khoa-hoc/           ← 6 khoá AE01–AE06 + diagram syllabus
  lich-khai-giang/    ← lịch năm học / nhận ngày khai giảng
  giang-vien/         ← Đạt Phạm (NVIDIA); cố vấn Lâm Phạm (ex-Senior SWE TikTok, Grab), Harry Lê Quang Hoà (SWE @ Amazon, ex-Tech Lead TikTok)
  assets/
  .nojekyll
  sitemap.xml
  robots.txt
  404.html
scripts/
  build_site.py       ← sinh HTML từ nội dung khoá
  make_logo.py        ← mark isometric SVG/PNG
```

Không cần Jekyll, Node, hay build trên CI. Push `docs/` lên `main` là đủ.

## Bật GitHub Pages

1. Repo: `EngineerPro-team/engineerproai`
2. **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: **`main`**
5. Folder: **`/docs`**
6. Save. Site lên sau ~1 phút.

File `docs/.nojekyll` bắt Pages phục vụ file tĩnh, không chạy Jekyll.

## Preview local

```bash
cd docs
python3 -m http.server 8080
```

Mở http://127.0.0.1:8080/

## Sửa nội dung rồi build lại

```bash
python3 scripts/make_diagrams.py   # hình lộ trình / syllabus
python3 scripts/build_site.py      # HTML
python3 scripts/make_logo.py       # logo / favicon / OG
```

`docs/assets/css/style.css` và `docs/assets/js/main.js` sửa trực tiếp, không qua script.

Profile giảng viên nằm trong `PEOPLE` / `instructors()` ở `scripts/build_site.py`. Sửa rồi chạy lại `python3 scripts/build_site.py`.
