#!/usr/bin/env python3
"""Build static HTML into docs/ for GitHub Pages."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = "https://engineerpro-team.github.io/engineerproai"
FB = "https://www.facebook.com/EngineerProAI"
MSG = "https://m.me/EngineerProAI"
COMPANIES = [
    ("nvidia.svg", "NVIDIA"),
    ("tiktok.svg", "TikTok"),
    ("amazon.svg", "Amazon"),
    ("grab.svg", "Grab"),
]
PEOPLE = [
    {
        "name": "Đạt Phạm",
        "badge": "Giảng viên",
        "photo": "dat-pham.jpg",
        "role": "Software Engineer",
        "company": "NVIDIA",
        "tags": [("nvidia.svg", "NVIDIA")],
        "track": "Phụ trách giảng dạy AI/ML Engineering — GPU lab, training, model card.",
        "linkedin": "https://www.linkedin.com/in/datphamvn/",
    },
    {
        "name": "Lâm Phạm",
        "badge": "Cố vấn",
        "photo": "lam-pham.jpg",
        "role": "ex-Senior SWE",
        "company": "TikTok, Grab",
        "tags": [("tiktok.svg", "TikTok"), ("grab.svg", "Grab")],
        "track": "Cố vấn chương trình.",
        "linkedin": "https://www.linkedin.com/in/lam0895/",
    },
    {
        "name": "Harry Lê Quang Hoà",
        "badge": "Cố vấn",
        "photo": "harry-le-quang-hoa.jpg",
        "role": "SWE",
        "company": "Amazon",
        "tags": [("amazon.svg", "Amazon"), ("tiktok.svg", "ex TikTok")],
        "track": "ex-Tech Lead @ TikTok.",
        "linkedin": "https://www.linkedin.com/in/harry-le-quang-hoa-32210066/",
    },
]
DIAGRAMS = {
    "ae01": ("ae01-levels.svg", "Thang năng lực AE01 từ L0 đến L5"),
    "ae02": ("ae02-math.svg", "Bốn trụ toán của AE02"),
    "ae03": ("ae03-pipeline.svg", "Pipeline machine learning AE03"),
    "ae04": ("ae04-dl.svg", "Lộ trình deep learning AE04"),
    "ae05": ("ae05-system.svg", "Thiết kế hệ thống ML và GenAI AE05"),
    "ae06": ("ae06-research.svg", "Vòng nghiên cứu ứng dụng AE06"),
}

COURSES = [
    {
        "slug": "ae01",
        "code": "AE01",
        "months": "Tháng 1–2",
        "intake": {
            "start": "25/11/2026",
            "slots": [
                "Tối Thứ Tư 20:30–22:30 GMT+7",
                "Chiều Chủ Nhật 14:00–16:00 GMT+7",
            ],
            "hours": "2 giờ / buổi",
        },
        "title": "AI Productivity & Harnesses",
        "tagline": "Work with AI like an engineer at Big Tech.",
        "audience": "PM, BA, vận hành, marketer, knowledge worker và developer muốn tăng năng suất.",
        "capability": "Đi từ L0 đến L5: hỗ trợ cá nhân, giao việc, điều phối và vận hành workflow AI.",
        "prereq": "Biết dùng máy tính, file và ứng dụng văn phòng. Nhánh non-tech không yêu cầu lập trình. Nhánh kỹ thuật dành cho người đọc và sửa được code.",
        "goal": "Dùng AI để hoàn thành công việc và tăng năng suất đo được. Thực hành với tài liệu, bảng dữ liệu, thông tin công việc và AI coding để tạo tiện ích cho nhu cầu thật.",
        "outcome": "Chọn việc phù hợp để giao AI, cộng tác ở nhiều mức tự chủ, tạo tiện ích bằng AI coding, cấu hình đội agent, vận hành workflow theo mục tiêu và chọn mức tự chủ hợp lý.",
        "tools": "Tài khoản AI trả phí trong hai tháng, workspace chạy tiện ích, template, hỗ trợ setup. Lab dùng API có ngân sách riêng.",
        "proof": "Tiện ích, harness, log điều phối, hồ sơ L0–L5 và báo cáo năng suất.",
        "weeks": [
            ("1", "B1. L0 — Chọn tác vụ, ghi baseline và tiêu chí hoàn thành", "B2. L1 — Kích hoạt tài khoản, dùng AI cho phần việc nhỏ, kiểm tra lỗi"),
            ("2", "B3. L2 — Cung cấp yêu cầu, context, ví dụ; cộng tác qua checkpoint", "B4. L2 — AI coding tạo tiện ích nhỏ cho tài liệu hoặc dữ liệu"),
            ("3", "B5. L2 — Sửa lỗi cùng AI, test nghiệp vụ, lưu phiên bản", "B6. L3 — Chuyển yêu cầu thành nhiệm vụ trọn gói, artifact và nghiệm thu"),
            ("4", "B7. L3 — Custom harness: instructions, context, skill, template, công cụ, test", "B8. L3 — Agent chạy độc lập trong workspace riêng, thu artifact và log"),
            ("5", "B9. L3 — Nghiệm thu, thử thiếu dữ liệu, sửa cấu hình", "B10. L4 — Đặc tả nghiệm thu, đội agent, bàn giao và workspace"),
            ("6", "B11. L4 — Review kế hoạch và giao đội agent thực hiện đặc tả", "B12. L4 — Kiểm tra độc lập, so sánh với single agent"),
            ("7", "B13. L5 — Software factory: nhận spec, tạo/sửa tiện ích, tự kiểm tra, đóng gói", "B14. L5 — Chạy end-to-end với yêu cầu mới, giới hạn quyền, ngân sách và lỗi"),
            ("8", "B15. L5 — Productivity audit: tự chủ, thời gian kiểm tra, chất lượng, chi phí", "B16. Capstone không chỉ đạo từng bước, bảo vệ bằng chứng, chọn mức áp dụng"),
        ],
        "levels": [
            ("L0 Baseline", "Hiểu việc hiện tại và chọn vấn đề phù hợp"),
            ("L1 AI Assistance", "Dùng AI hỗ trợ phần việc nhỏ và tự kiểm tra đầu ra"),
            ("L2 AI Collaboration", "Cung cấp context, trao đổi và chỉnh kết quả qua checkpoint"),
            ("L3 Task Delegation", "Giao nhiệm vụ trọn gói, nhận artifact và nghiệm thu"),
            ("L4 Spec-Driven AI Team", "Viết đặc tả nghiệm thu, cấu hình vai trò, bàn giao và review"),
            ("L5 Software Factory", "Cấu hình quy trình tự triển khai, kiểm thử, đóng gói và xử lý ngoại lệ"),
        ],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae02",
        "code": "AE02",
        "months": "Tháng 3–4",
        "intake": {
            "start": "23/12/2026",
            "slots": [
                "Tối Thứ Năm 20:30–22:30 GMT+7",
                "Tối Chủ Nhật 20:30–22:30 GMT+7",
            ],
            "hours": "2 giờ / buổi",
        },
        "title": "Math for ML & DL",
        "tagline": "Understand the math. Unlock the models.",
        "audience": "Người chuẩn bị học ML/DL, đọc nghiên cứu hoặc củng cố toán cho kỹ thuật AI.",
        "capability": "Biểu diễn và suy luận bằng toán cho machine learning và deep learning.",
        "prereq": "Đại số phổ thông, hàm số và Python cơ bản.",
        "goal": "Xây nền tảng toán theo tiến trình trực giác → công thức → tính tay → NumPy. Hiểu biểu diễn dữ liệu, phép tính vector, tối ưu và bất định.",
        "outcome": "Notebook tính similarity, projection, tối ưu một hàm đơn giản và ước lượng xác suất. Kiểm tra gradient bằng sai phân hữu hạn.",
        "tools": "Notebook workspace trên CPU, lab toán tương tác và phiên chữa bài.",
        "proof": "Notebook toán có lời giải và kiểm tra tính đúng.",
        "weeks": [
            ("1", "B1. Scalar, vector, matrix, tensor, shape và biểu diễn dữ liệu", "B2. Dot product, norm, khoảng cách và cosine similarity"),
            ("2", "B3. Nhân ma trận, biến đổi tuyến tính và hệ phương trình", "B4. Rank, basis, projection và hình học least squares"),
            ("3", "B5. Eigenvalue, eigenvector và diễn giải hình học", "B6. SVD và xấp xỉ hạng thấp"),
            ("4", "B7. Đạo hàm riêng, gradient và đạo hàm theo hướng", "B8. Chain rule, Jacobian và vi phân hàm nhiều biến"),
            ("5", "B9. Gradient descent và ảnh hưởng của bước cập nhật", "B10. Convexity, curvature, tối ưu có ràng buộc và regularization"),
            ("6", "B11. Xác suất có điều kiện, độc lập và định lý Bayes", "B12. Biến ngẫu nhiên, phân phối, kỳ vọng, phương sai, covariance"),
            ("7", "B13. Sampling, LLN, CLT, sai số ước lượng và khoảng tin cậy", "B14. Likelihood, MLE, MAP và liên hệ với hàm mục tiêu"),
            ("8", "B15. Entropy, cross-entropy và KL divergence", "B16. Math lab tổng hợp và bảo vệ notebook"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae03",
        "code": "AE03",
        "months": "Tháng 5–6",
        "title": "Machine Learning Foundations",
        "tagline": "Turn data into reliable predictions.",
        "audience": "Software engineer chuyển sang ML và analyst muốn xây mô hình dự đoán.",
        "capability": "Xây dựng và đánh giá mô hình machine learning đáng tin cậy.",
        "prereq": "Đạt chuẩn AE02; Python, NumPy và pandas cơ bản.",
        "goal": "Xây baseline đáng tin, biểu diễn dữ liệu, huấn luyện mô hình và đánh giá offline đúng cách. Bài toán có thể dùng dữ liệu bảng, phân loại văn bản hoặc tìm kiếm đơn giản.",
        "outcome": "Pipeline offline chạy lại được, benchmark, báo cáo sai số và model artifact. Giải thích được dữ liệu dùng để fit, tune và test.",
        "tools": "Môi trường ML cài sẵn, dataset, experiment tracking và danh sách contribution phù hợp.",
        "proof": "Benchmark và gói đóng góp open source đầu tiên.",
        "weeks": [
            ("1", "B1. Chuyển câu hỏi thành bài toán supervised/unsupervised, target và baseline", "B2. Train / validation / test, split theo thời gian hoặc nhóm, data leakage"),
            ("2", "B3. Linear regression, fitting, residual và dự đoán", "B4. GD, SGD, feature scaling và regularization trong regression"),
            ("3", "B5. Logistic regression và xác suất dự đoán", "B6. Metric hồi quy, phân loại, threshold và dữ liệu mất cân bằng"),
            ("4", "B7. Decision tree, chia nhánh, impurity và overfitting", "B8. Random forest, bagging và bias-variance"),
            ("5", "B9. Gradient boosting và baseline cho dữ liệu bảng", "B10. Cross-validation, hyperparameter search và ghi nhận thí nghiệm"),
            ("6", "B11. Feature transformation, dữ liệu thiếu và preprocessing pipeline", "B12. PCA, chọn số chiều và đánh giá thông tin bị mất"),
            ("7", "B13. K-means và nearest neighbors", "B14. TF-IDF, retrieval baseline và metric tìm kiếm"),
            ("8", "B15. Error analysis, calibration và sai số theo nhóm dữ liệu", "B16. Bảo vệ pipeline ML và quyết định chọn mô hình"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae04",
        "code": "AE04",
        "months": "Tháng 7–8",
        "title": "Deep Learning Foundations",
        "tagline": "Build, train, and adapt neural models.",
        "audience": "Người đã biết ML, muốn học DL, NLP và foundation models.",
        "capability": "Huấn luyện và thích nghi neural network.",
        "prereq": "Đạt chuẩn AE03; hiểu gradient, overfitting và đánh giá offline.",
        "goal": "Hiểu cơ chế neural network, tự xây training loop, debug quá trình học và thích nghi mô hình pretrained. Tập trung text và representation learning; CNN là kiến trúc bổ sung.",
        "outcome": "Checkpoint mini language model huấn luyện từ đầu, adapter hoặc mô hình đã SFT, training log, model card và benchmark offline. Lab tuần 6–8 chạy trên GPU.",
        "tools": "GPU quota cá nhân, nơi lưu checkpoint, training recipe và hỗ trợ debug.",
        "proof": "Checkpoint, adapter, training log và model card.",
        "weeks": [
            ("1", "B1. PyTorch, tensor, broadcasting, device và autograd", "B2. MLP, layer, activation, forward pass và loss"),
            ("2", "B3. Backpropagation và chain rule cho neural network", "B4. Training loop, data loader, batching và checkpoint"),
            ("3", "B5. Momentum, Adam và learning-rate schedule", "B6. Initialization, normalization, dropout và regularization"),
            ("4", "B7. Debug training qua gradient, learning curve và overfit một batch", "B8. CNN và transfer learning với bài tập ảnh nhỏ"),
            ("5", "B9. Tokenization, embedding và biểu diễn chuỗi", "B10. Attention: query, key, value và masking"),
            ("6", "B11. Transformer, encoder, decoder và vị trí token", "B12. Language modeling, pretraining, sinh token — bắt đầu mini LM"),
            ("7", "B13. Supervised fine-tuning và PEFT/LoRA với mô hình nhỏ", "B14. Contrastive learning và huấn luyện embedding"),
            ("8", "B15. Ablation, profiling bộ nhớ/tính toán và so sánh baseline", "B16. Demo, error analysis và bảo vệ model card"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae05",
        "code": "AE05",
        "months": "Tháng 9–10",
        "title": "ML & GenAI System Design",
        "tagline": "Design for production. Defend every trade-off.",
        "audience": "SWE, AI/ML Engineer chuẩn bị phỏng vấn system design hoặc xây hệ thống AI.",
        "capability": "Thiết kế hệ thống ML/GenAI theo ràng buộc sản phẩm.",
        "prereq": "Đạt chuẩn AE03–AE04; biết API, HTTP, SQL và Git. Prework kiểm tra container, queue và hệ thống phân tán cơ bản.",
        "goal": "Thiết kế, trình bày và kiểm chứng kiến trúc ML/GenAI dưới ràng buộc sản phẩm. Phục vụ cả công việc thực tế và phỏng vấn ML/AI System Design.",
        "outcome": "Demo có giới hạn thời gian, design document và báo cáo vận hành. Bảo vệ được sơ đồ, ước lượng và trade-off.",
        "tools": "Deployment sandbox, API budget, công cụ load test và monitoring.",
        "proof": "Demo, design document và báo cáo vận hành.",
        "weeks": [],
        "sessions": [
            ("B1", "Xác định bài toán và ràng buộc sản phẩm", "Chốt người dùng, luồng, quy mô, ngân sách; ghi giả định; cân nhắc có cần ML hay không"),
            ("B2", "Kết nối chất lượng mô hình với kết quả sản phẩm", "Cây mục tiêu: chỉ số kinh doanh, metric offline, giới hạn vận hành"),
            ("B3", "Phác thảo kiến trúc tối thiểu", "Request flow và training flow; interface; thành phần thay thế độc lập"),
            ("B4", "Thiết kế nguồn và dòng dữ liệu", "Data contract, nhãn, lưu trữ, lineage; dữ liệu đến muộn và đổi schema"),
            ("B5", "Tổ chức feature trong hệ thống", "Nơi và thời điểm tính feature, version, point-in-time, nhất quán khi serving"),
            ("B6", "Phát triển và chấp nhận mô hình", "Chọn model từ benchmark AE03–AE04; training job, registry, tái lập, điều kiện release"),
            ("B7", "Thiết kế dịch vụ dự đoán", "API contract, latency budget, serving đồng bộ hoặc bất đồng bộ"),
            ("B8", "Kiểm chứng online và phát hành", "Nhóm thử nghiệm, guardrail, tiêu chí dừng và rollback"),
            ("B9", "Mở rộng và duy trì hệ thống", "Capacity, cảnh báo, sự cố, quy tắc cập nhật dữ liệu/model"),
            ("B10", "GenAI — Chiến lược mô hình và tri thức", "Decision record: retrieval, long context, adaptation, tool use; API hay self-host"),
            ("B11", "GenAI — RAG có thể kiểm chứng", "Index, hybrid search, rerank, citation; tài liệu hết hạn và quyền truy cập"),
            ("B12", "GenAI — Ngân sách inference", "Caching, batching, routing, precision; TTFT và thời gian hoàn tất"),
            ("B13", "GenAI — Đánh giá chất lượng", "Eval set, hiệu chỉnh judge bằng nhãn người, chặn regression trước release"),
            ("B14", "GenAI — Vận hành và ranh giới thực thi", "Failure budget, dữ liệu nhạy cảm, retry, idempotency, trace, tool contract"),
            ("B15", "Case study ML — Recommendation hoặc ranking", "Vận dụng 9 bước, bảo vệ sơ đồ và ước lượng, thử tải một phần hệ thống"),
            ("B16", "Case study GenAI — Mock interview", "Trình bày hệ thống LLM/RAG khi yêu cầu đổi; tác động chất lượng, latency, chi phí, vận hành"),
        ],
        "levels": [],
        "schedule_kind": "sessions",
    },
    {
        "slug": "ae06",
        "code": "AE06",
        "months": "Tháng 11–12",
        "title": "Frontier AI Lab",
        "tagline": "Explore the frontier. Learn to research.",
        "audience": "AI engineer, technical lead và builder đã có nền tảng AI/ML.",
        "capability": "Nghiên cứu ứng dụng theo các hướng AI mới của từng năm.",
        "prereq": "Hoàn thành AE03–AE04; AE05 là lợi thế khi mang hệ thống vào thí nghiệm.",
        "goal": "Kỹ năng nghiên cứu là kỹ năng kỹ sư — kể cả khi không nhằm công bố paper. Một nửa thời lượng là seminar về chủ đề AI mới. Nửa còn lại: thiết kế thí nghiệm, thực hành và trình bày.",
        "outcome": "Research report, prototype; tùy chọn manuscript hoặc gói đóng góp open source.",
        "tools": "Research sandbox, API budget, GPU khi cần, research clinic và mentor review.",
        "proof": "Research report, prototype và tùy chọn paper/contribution package.",
        "weeks": [
            ("1–2", "Seminar hướng frontier của năm: đọc paper, tóm claim, đặt câu hỏi", "Research skills: câu hỏi nghiên cứu, giả thuyết, phạm vi thí nghiệm"),
            ("3–4", "Thiết kế thí nghiệm, chọn baseline, metric và tiêu chí thành công", "Tái lập hoặc kiểm tra một claim; ghi log và hạn chế"),
            ("5–6", "Prototype / ablation trên sandbox và GPU được cấp", "Research clinic: mentor review hướng đi và bằng chứng"),
            ("7–8", "Viết research report, trình bày kết quả", "Bảo vệ: giải thích, sửa trực tiếp, quyết định bước tiếp theo"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
        "week_headers": ("Giai đoạn", "Trọng tâm A", "Trọng tâm B"),
    },
]


def logo_strip(prefix: str) -> str:
    items = "".join(
        f'<li><img src="{prefix}assets/img/companies/{fn}" alt=""><span>{name}</span></li>'
        for fn, name in COMPANIES
    )
    return f"""<div class="logo-strip reveal">
  <p>Giảng viên và cố vấn: NVIDIA · TikTok · Amazon · Grab</p>
  <ul>{items}</ul>
</div>"""


def diagram_figure(filename: str, alt: str, prefix: str) -> str:
    return f'<figure class="diagram reveal"><img src="{prefix}assets/img/diagrams/{filename}" alt="{alt}"></figure>'


def nav(prefix: str, active: str) -> str:
    def item(key: str, href: str, label: str, hot: bool = False) -> str:
        cls = []
        if active == key:
            cls.append("is-active")
        if hot:
            cls.append("nav-hot")
        attr = f' class="{" ".join(cls)}"' if cls else ""
        return f'<a href="{href}"{attr}>{label}</a>'

    return f"""<header class="header" data-header>
  <div class="header-inner">
    <a class="brand" href="{prefix}index.html">
      <img src="{prefix}assets/img/logo-mark.svg" alt="">
      <span><b>ENGINEERPRO</b><small>AI / ML Accelerator</small></span>
    </a>
    <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav" aria-label="Mở menu">
      <span></span>
    </button>
    <nav class="nav" id="site-nav" data-nav-panel>
      {item("home", prefix + "index.html", "Trang chủ")}
      {item("courses", prefix + "khoa-hoc/", "Khoá học")}
      {item("schedule", prefix + "lich-khai-giang/", "Lịch khai giảng", hot=True)}
      {item("instructors", prefix + "giang-vien/", "Giảng viên")}
      <a class="btn btn-primary" href="{MSG}" target="_blank" rel="noopener">Tư vấn Messenger</a>
    </nav>
  </div>
</header>"""


def footer(prefix: str) -> str:
    links = "".join(
        f'<li><a href="{prefix}khoa-hoc/{c["slug"]}/">{c["code"]} · {c["title"]}</a></li>'
        for c in COURSES
    )
    return f"""<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand" href="{prefix}index.html">
        <img src="{prefix}assets/img/logo-mark.svg" alt="">
        <span><b>ENGINEERPRO</b><small>AI / ML Accelerator</small></span>
      </a>
      <p style="margin-top:1rem">Một năm học AI Engineering với công cụ trả phí, GPU, lab huấn luyện mô hình và lộ trình đóng góp open source có mentor review.</p>
    </div>
    <div>
      <h3>Sáu học phần</h3>
      <ul>{links}</ul>
    </div>
    <div>
      <h3>Liên hệ</h3>
      <ul>
        <li><a href="{MSG}" target="_blank" rel="noopener">Nhắn Messenger</a></li>
        <li><a href="{FB}" target="_blank" rel="noopener">Facebook EngineerPro AI</a></li>
        <li><a href="{prefix}lich-khai-giang/">Lịch khai giảng</a></li>
        <li><a href="{prefix}giang-vien/">Giảng viên Big Tech</a></li>
        <li><a href="{prefix}khoa-hoc/">Lộ trình 6 khoá</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal">
    <span>© <span data-year></span> EngineerPro AI</span>
    <span>Learn with the tools. Train on GPUs. Contribute to real projects.</span>
  </div>
</footer>"""


def messenger_fab() -> str:
    return f"""<a class="msg-fab" href="{MSG}" target="_blank" rel="noopener" aria-label="Nhắn tin tư vấn qua Messenger">
  <svg viewBox="0 0 24 24" aria-hidden="true">
    <path fill="currentColor" d="M.001 11.639C.001 4.949 5.241 0 12.001 0 18.762 0 24 4.95 24 11.639c0 6.689-5.238 11.638-11.999 11.638-1.21 0-2.38-.16-3.47-.46a.96.96 0 00-.64.05l-2.39 1.05a.96.96 0 01-1.35-.85l-.07-2.14a.97.97 0 00-.32-.68A11.39 11.39 0 010 11.639zm8.32-2.19l-3.52 5.6c-.35.53.32 1.139.82.75l3.79-2.87a.724.724 0 01.87 0l2.8 2.1c.84.63 2.04.41 2.6-.48l3.52-5.6c.35-.53-.32-1.13-.82-.75l-3.79 2.87a.724.724 0 01-.87 0l-2.8-2.1a1.8 1.8 0 00-2.6.48z"/>
  </svg>
</a>"""


def page(title: str, description: str, path: str, prefix: str, active: str, body: str, extra_head: str = "") -> str:
    canonical = f"{SITE}/{path}" if path else f"{SITE}/"
    og = f"{SITE}/assets/img/og-share.png"
    return f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/img/favicon-32.png">
  <link rel="icon" type="image/png" href="{prefix}assets/img/favicon.png">
  <link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="EngineerPro AI">
  <meta property="og:locale" content="vi_VN">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/css/style.css">
  {extra_head}
</head>
<body>
  <a class="skip-link" href="#main">Bỏ qua điều hướng</a>
  {nav(prefix, active)}
  <main id="main">{body}</main>
  {footer(prefix)}
  {messenger_fab()}
  <script src="{prefix}assets/js/main.js"></script>
</body>
</html>
"""


def json_ld_home() -> str:
    courses = [
        {
            "@type": "Course",
            "name": f'{c["code"]} — {c["title"]}',
            "description": c["tagline"],
            "url": f'{SITE}/khoa-hoc/{c["slug"]}/',
            "provider": {"@id": f"{SITE}/#org"},
        }
        for c in COURSES
    ]
    import json

    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "EducationalOrganization"],
                "@id": f"{SITE}/#org",
                "name": "EngineerPro AI",
                "url": f"{SITE}/",
                "logo": f"{SITE}/assets/img/logo-mark.png",
                "sameAs": [FB, MSG],
            },
            {
                "@type": "EducationalOccupationalProgram",
                "name": "AI/ML Engineering Accelerator",
                "description": "Lộ trình 12 tháng, 6 khoá AI/ML Engineering với giảng viên Big Tech.",
                "url": f"{SITE}/",
                "provider": {"@id": f"{SITE}/#org"},
                "timeToComplete": "P12M",
                "hasCourse": courses,
            },
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def course_when(c: dict) -> str:
    intake = c.get("intake")
    if intake:
        return f"Khai giảng {intake['start']}"
    return c["months"]


def home() -> str:
    cards = "\n".join(
        f"""<a class="course-card reveal" href="khoa-hoc/{c['slug']}/">
  <div class="hex">{c['code']}</div>
  <div>
    <div class="meta">{course_when(c)}</div>
    <h3>{c['title']}</h3>
    <p>{c['tagline']}</p>
  </div>
  <span class="go" aria-hidden="true">→</span>
</a>"""
        for c in COURSES
    )
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="eyebrow">Mentor từ NVIDIA, TikTok, Amazon, Grab</div>
      <h1>Sáu khoá AI Engineering — học với giảng viên đang làm tại Big Tech.</h1>
      <p class="lede">Lộ trình 12 tháng cho người đã biết lập trình. Công cụ trả phí, GPU lab, contribution có mentor review. Giảng viên NVIDIA; cố vấn từ TikTok, Grab và Amazon.</p>
      <p class="tagline">Learn with the tools. Train on GPUs. Contribute to real projects.</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-lg" href="{MSG}" target="_blank" rel="noopener">Tư vấn qua Messenger</a>
        <a class="btn btn-ghost btn-lg" href="#lo-trinh">Xem 6 học phần</a>
        <a class="btn btn-ghost btn-lg" href="lich-khai-giang/">Lịch khai giảng</a>
      </div>
      <p class="intake-line">Đợt tới: AE01 khai giảng <strong>25/11/2026</strong> · AE02 khai giảng <strong>23/12/2026</strong></p>
    </div>
    <div class="hero-visual">
      <img src="assets/img/logo-mark.svg" alt="Logo EngineerPro AI">
    </div>
  </div>
  <div class="wrap">{logo_strip("")}</div>
  <div class="wrap stats">
    <div class="stat"><b>12 tháng</b><span>6 học phần × 2 tháng</span></div>
    <div class="stat"><b>96 buổi</b><span>2,5 giờ / buổi, 2 buổi / tuần</span></div>
    <div class="stat"><b>528 giờ</b><span>240 giờ lớp + ~288 giờ tự học</span></div>
    <div class="stat"><b>Big Tech</b><span>NVIDIA · TikTok · Amazon · Grab</span></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Đối tượng</div>
      <h2>Cho người muốn làm AI/ML Engineering, không chỉ “biết dùng ChatGPT”.</h2>
    </div>
    <div class="grid-4">
      <article class="card reveal"><div class="icon-pill">01</div><h3>Mới vào AI/ML</h3><p>Cần lộ trình có thứ tự, lab sẵn và tiêu chí đầu ra rõ.</p></article>
      <article class="card reveal"><div class="icon-pill">02</div><h3>Kiến thức còn rời</h3><p>Đã học vài khoá lẻ, muốn nối thành năng lực bảo vệ được quyết định kỹ thuật.</p></article>
      <article class="card reveal"><div class="icon-pill">03</div><h3>SWE chuyển AI</h3><p>Biết code, muốn train model, thiết kế hệ thống và đưa lên production.</p></article>
      <article class="card reveal"><div class="icon-pill">04</div><h3>Sinh viên kỹ thuật</h3><p>Có nền lập trình, muốn portfolio GPU, demo và contribution.</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">USP</div>
      <h2>Môi trường thực hành của kỹ sư, chuẩn bị sẵn.</h2>
      <p>Access. Practice. Proof. Ba lớp giá trị hỗ trợ nhau suốt 12 tháng — mentor Big Tech review từng checkpoint.</p>
    </div>
    <div class="grid-3">
      <article class="card reveal"><div class="icon-pill">A</div><h3>Access</h3><p>Công cụ AI trả phí, GPU, sandbox triển khai — có ngay khi học phần bắt đầu, không tự mò setup một mình.</p></article>
      <article class="card reveal"><div class="icon-pill">P</div><h3>Practice</h3><p>Lab, dữ liệu, quota, và hỗ trợ xử lý lỗi. 16 buổi mỗi học phần: lý thuyết, worked example, thực hành có hướng dẫn.</p></article>
      <article class="card reveal"><div class="icon-pill">✓</div><h3>Proof</h3><p>Workflow, checkpoint, benchmark, demo và contribution — thứ bạn giữ lại trên CV, không chỉ chứng chỉ.</p></article>
    </div>
  </div>
</section>

<section id="lo-trinh">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Lộ trình 12 tháng</div>
      <h2>Sáu khoá, mỗi khoá 8 tuần — 4 tuần dự phòng cho lễ, học bù và portfolio.</h2>
    </div>
    {diagram_figure("roadmap-12.svg", "Lộ trình 12 tháng sáu học phần AE01 đến AE06", "")}
    <div class="path">{cards}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Đánh giá</div>
      <h2>Đạt khi bạn giải thích và sửa được — không phải copy output của AI.</h2>
    </div>
    <div class="grid-4">
      <article class="card reveal"><h3>20%</h3><p>Kiểm tra hiểu biết cá nhân</p></article>
      <article class="card reveal"><h3>30%</h3><p>Lab và bài tập</p></article>
      <article class="card reveal"><h3>35%</h3><p>Bài tập lớn học phần</p></article>
      <article class="card reveal"><h3>15%</h3><p>Bảo vệ: giải thích và sửa trực tiếp</p></article>
    </div>
    <p class="reveal" style="margin-top:1.2rem;color:var(--muted)">Ngưỡng đạt đề xuất 70/100, hoàn thành yêu cầu bắt buộc. Được dùng AI nhưng phải ghi phần AI hỗ trợ và cách kiểm chứng.</p>
  </div>
</section>

<section>
  <div class="wrap callout reveal">
    <h2>Giảng viên NVIDIA. Cố vấn TikTok, Grab và Amazon.</h2>
    <p>Anh Đạt giảng dạy. Cố vấn: anh Lâm (ex-Senior SWE TikTok, Grab) và anh Hoà (SWE @ Amazon, ex-Tech Lead TikTok).</p>
    <div class="hero-actions">
      <a class="btn btn-ghost" href="giang-vien/">Xem giảng viên</a>
      <a class="btn btn-primary" href="lich-khai-giang/">Lịch khai giảng</a>
    </div>
  </div>
</section>
"""
    return page(
        "EngineerPro AI — 6 khoá AI Engineering với giảng viên Big Tech",
        "Lộ trình 12 tháng, 6 khoá: AI productivity, toán ML, machine learning, deep learning, system design và frontier lab. Giảng viên NVIDIA; cố vấn TikTok, Grab và Amazon. GPU, công cụ trả phí, mentor review.",
        "",
        "",
        "home",
        body,
        json_ld_home(),
    )


def schedule_table(course: dict) -> str:
    if course["schedule_kind"] == "sessions":
        rows = "".join(
            f"<tr><th>{a}</th><td><strong>{b}</strong></td><td>{c}</td></tr>"
            for a, b, c in course["sessions"]
        )
        return f"""<div class="table-wrap"><table>
          <thead><tr><th>Buổi</th><th>Trọng tâm</th><th>Bài tập / đầu ra</th></tr></thead>
          <tbody>{rows}</tbody>
        </table></div>"""
    h1, h2, h3 = course.get("week_headers", ("Tuần", "Buổi 1", "Buổi 2"))
    rows = "".join(
        f"<tr><th>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in course["weeks"]
    )
    return f"""<div class="table-wrap"><table>
      <thead><tr><th>{h1}</th><th>{h2}</th><th>{h3}</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>"""


def course_page(i: int) -> str:
    c = COURSES[i]
    prev_c = COURSES[i - 1] if i > 0 else None
    next_c = COURSES[i + 1] if i < len(COURSES) - 1 else None
    levels = ""
    if c["levels"]:
        rows = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in c["levels"])
        levels = f"""<div class="table-wrap" style="margin-bottom:1.4rem"><table>
          <thead><tr><th>Cấp độ</th><th>Năng lực</th></tr></thead><tbody>{rows}</tbody></table></div>"""
    pager = '<div class="pager">'
    if prev_c:
        pager += f'<a href="../{prev_c["slug"]}/"><small>Học phần trước</small><strong>{prev_c["code"]} · {prev_c["title"]}</strong></a>'
    else:
        pager += "<span></span>"
    if next_c:
        pager += f'<a href="../{next_c["slug"]}/" style="text-align:right"><small>Học phần sau</small><strong>{next_c["code"]} · {next_c["title"]}</strong></a>'
    pager += "</div>"
    chips = "".join(
        f'<span class="chip">{x}</span>'
        for x in (c["code"], course_when(c), "16 buổi · 8 tuần", "Mentor Big Tech")
    )
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../../index.html">Trang chủ</a> / <a href="../">Khoá học</a> / {c["code"]}</p>
    <div class="chips">{chips}</div>
    <p class="tagline-en" style="margin-top:1rem">{c["tagline"]}</p>
    <h1>{c["code"]} — {c["title"]}</h1>
    <p class="lede">{c["goal"]}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{MSG}" target="_blank" rel="noopener">Tư vấn học phần này</a>
      <a class="btn btn-ghost" href="../../lich-khai-giang/">Lịch khai giảng</a>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    {diagram_figure(*DIAGRAMS[c["slug"]], "../../")}
  </div>
</section>
<section>
  <div class="wrap split">
    <article class="card"><h3>Đầu vào</h3><p>{c["prereq"]}</p></article>
    <article class="card"><h3>Đầu ra</h3><p>{c["outcome"]}</p></article>
    <article class="card"><h3>Phù hợp với</h3><p>{c["audience"]}</p></article>
    <article class="card"><h3>Năng lực cốt lõi</h3><p>{c["capability"]}</p></article>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head"><div class="kicker">Syllabus</div><h2>16 buổi trong 8 tuần.</h2></div>
    {levels}
    {schedule_table(c)}
  </div>
</section>
<section>
  <div class="wrap split">
    <article class="card"><div class="icon-pill">Lab</div><h3>Công cụ & quyền lợi</h3><p>{c["tools"]}</p></article>
    <article class="card"><div class="icon-pill">CV</div><h3>Minh chứng giữ lại</h3><p>{c["proof"]}</p></article>
  </div>
  {pager}
</section>
"""
    return page(
        f'{c["code"]} — {c["title"]} | EngineerPro AI',
        f'{c["tagline"]} {c["goal"][:140]}',
        f'khoa-hoc/{c["slug"]}/',
        "../../",
        "courses",
        body,
    )


def courses_index() -> str:
    cards = "\n".join(
        f"""<a class="course-card reveal" href="{c['slug']}/">
  <div class="hex">{c['code']}</div>
  <div>
    <div class="meta">{course_when(c)} · {c['capability']}</div>
    <h3>{c['title']}</h3>
    <p>{c['tagline']}</p>
  </div>
  <span class="go" aria-hidden="true">→</span>
</a>"""
        for c in COURSES
    )
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Trang chủ</a> / Khoá học</p>
    <h1>Sáu khoá, một lộ trình.</h1>
    <p class="lede">Mỗi khoá 16 buổi, mentor Big Tech review. AE01 khai giảng 25/11/2026; AE02 khai giảng 23/12/2026. Học lần lượt 12 tháng, hoặc vào đúng học phần khi đã đủ đầu vào.</p>
  </div>
</section>
<section>
  <div class="wrap">
    {diagram_figure("roadmap-12.svg", "Lộ trình 12 tháng sáu học phần AE01 đến AE06", "../")}
    <div class="path">{cards}</div>
  </div>
</section>
"""
    return page(
        "Khoá học | EngineerPro AI",
        "Lộ trình 6 học phần AI/ML Engineering Accelerator: AE01 đến AE06.",
        "khoa-hoc/",
        "../",
        "courses",
        body,
    )


def instructors() -> str:
    cards = []
    for p in PEOPLE:
        tags = "".join(
            f'<div class="company-tag"><img src="../assets/img/companies/{fn}" alt="">{name}</div>'
            for fn, name in p["tags"]
        )
        cards.append(
            f"""<article class="card person">
  <div class="avatar"><img src="../assets/img/mentors/{p["photo"]}" alt="{p["name"]}"></div>
  <span class="soon">{p["badge"]}</span>
  <h3>{p["name"]}</h3>
  <p class="person-role">{p["role"]} @ {p["company"]}</p>
  <div class="person-tags">{tags}</div>
  <p>{p["track"]}</p>
  <a class="btn btn-ghost" href="{p["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>
</article>"""
        )
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Trang chủ</a> / Giảng viên</p>
    <h1>Giảng viên và cố vấn Big Tech.</h1>
    <p class="lede">Giảng viên: anh Đạt (NVIDIA). Cố vấn: anh Lâm (ex-Senior SWE TikTok, Grab) và anh Hoà (SWE @ Amazon, ex-Tech Lead TikTok). Team từ NVIDIA, TikTok, Amazon, Grab.</p>
    {logo_strip("../")}
  </div>
</section>
<section class="instructors">
  <div class="wrap grid-3">{"".join(cards)}</div>
</section>
<section>
  <div class="wrap callout">
    <h2>Muốn hỏi lộ trình với mentor?</h2>
    <p>Nhắn Messenger EngineerPro AI. AE01 khai giảng 25/11/2026; AE02 khai giảng 23/12/2026.</p>
    <a class="btn btn-ghost" href="{MSG}" target="_blank" rel="noopener">Nhắn Messenger</a>
  </div>
</section>
"""
    return page(
        "Giảng viên | EngineerPro AI",
        "Giảng viên Đạt Phạm (NVIDIA). Cố vấn Lâm Phạm (ex-Senior SWE TikTok, Grab) và Harry Lê Quang Hoà (SWE @ Amazon, ex-Tech Lead TikTok).",
        "giang-vien/",
        "../",
        "instructors",
        body,
    )


def schedule() -> str:
    cards = []
    for c in COURSES:
        intake = c.get("intake")
        if intake:
            slots = "".join(f"<li>{s}</li>" for s in intake["slots"])
            cards.append(
                f"""<article class="sched-card is-open reveal">
  <div class="when">Khai giảng {intake["start"]}</div>
  <span class="soon">Đang mở đăng ký</span>
  <h3>{c["code"]} · {c["title"]}</h3>
  <p>{c["tagline"]}</p>
  <ul class="slots">{slots}</ul>
  <p>16 buổi · 8 tuần · {intake["hours"]}</p>
  <div class="open"><a class="btn btn-primary" href="{MSG}" target="_blank" rel="noopener">Đăng ký qua Messenger</a></div>
</article>"""
            )
        else:
            cards.append(
                f"""<article class="sched-card reveal">
  <div class="when">{c["months"]} · Sắp công bố</div>
  <h3>{c["code"]} · {c["title"]}</h3>
  <p>{c["tagline"]}</p>
  <p>16 buổi · 8 tuần · GMT+7</p>
  <p>Ngày và khung giờ xác nhận qua fanpage.</p>
  <div class="open"><a class="btn btn-ghost" href="{MSG}" target="_blank" rel="noopener">Nhận lịch khai giảng</a></div>
</article>"""
            )
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Trang chủ</a> / Lịch khai giảng</p>
    <h1>Lịch khai giảng 6 khoá.</h1>
    <p class="lede">AE01 khai giảng 25/11/2026: tối Thứ Tư 20:30–22:30 và chiều Chủ Nhật 14:00–16:00 (GMT+7), 16 buổi. AE02 khai giảng 23/12/2026: tối Thứ Năm 20:30–22:30 và tối Chủ Nhật 20:30–22:30 (GMT+7), 16 buổi. AE03–AE06 công bố sau.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{MSG}" target="_blank" rel="noopener">Đăng ký qua Messenger</a>
      <a class="btn btn-ghost" href="../khoa-hoc/">Xem syllabus 6 khoá</a>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    {diagram_figure("year-calendar.svg", "Lịch khai giảng AE01 25/11/2026 và AE02 23/12/2026", "../")}
    <div class="sched-grid">{"".join(cards)}</div>
  </div>
</section>
<section>
  <div class="wrap callout">
    <h2>Đang nhận đăng ký AE01 và AE02.</h2>
    <p>AE01 bắt đầu 25/11/2026. AE02 bắt đầu 23/12/2026. Nhắn Messenger để giữ chỗ.</p>
    <a class="btn btn-ghost" href="{MSG}" target="_blank" rel="noopener">Nhắn Messenger</a>
  </div>
</section>
"""
    return page(
        "Lịch khai giảng | EngineerPro AI",
        "AE01 khai giảng 25/11/2026 (T4 20:30–22:30, CN 14:00–16:00 GMT+7). AE02 khai giảng 23/12/2026 (T5 và CN 20:30–22:30 GMT+7). 16 buổi mỗi module.",
        "lich-khai-giang/",
        "../",
        "schedule",
        body,
    )


def not_found() -> str:
    # Root-absolute prefix so GitHub Pages can serve this file at any missing nested URL.
    prefix = "/engineerproai/"
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Không tìm thấy trang.</h1>
    <p class="lede">Link có thể đã đổi. Về trang chủ hoặc xem 6 học phần.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{prefix}">Về trang chủ</a>
      <a class="btn btn-ghost" href="{prefix}khoa-hoc/">Khoá học</a>
    </div>
  </div>
</section>
"""
    return page("Không tìm thấy | EngineerPro AI", "Trang không tồn tại.", "404.html", prefix, "home", body)


def sitemap() -> str:
    urls = ["", "khoa-hoc/", "lich-khai-giang/", "giang-vien/"] + [
        f"khoa-hoc/{c['slug']}/" for c in COURSES
    ]
    items = "\n".join(
        f"  <url><loc>{SITE}/{u}</loc><changefreq>weekly</changefreq></url>" if u else f"  <url><loc>{SITE}/</loc><changefreq>weekly</changefreq></url>"
        for u in urls
    )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + items + "\n</urlset>\n"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main() -> None:
    write(DOCS / "index.html", home())
    write(DOCS / "khoa-hoc" / "index.html", courses_index())
    write(DOCS / "lich-khai-giang" / "index.html", schedule())
    write(DOCS / "giang-vien" / "index.html", instructors())
    write(DOCS / "404.html", not_found())
    for i, c in enumerate(COURSES):
        write(DOCS / "khoa-hoc" / c["slug"] / "index.html", course_page(i))
    write(DOCS / "sitemap.xml", sitemap())
    write(
        DOCS / "robots.txt",
        f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n",
    )
    write(DOCS / ".nojekyll", "")


if __name__ == "__main__":
    main()
