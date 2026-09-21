#!/usr/bin/env python3
"""Build static HTML into docs/ for GitHub Pages."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = "https://engineerpro-team.github.io/engineerproai"
FB = "https://www.facebook.com/EngineerProAI"
MSG = "https://m.me/EngineerProAI"
GA_ID = "G-5TH79627Q6"
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
    "ae01": ("ae01-levels.svg", "AE01 capability ladder from L0 to L5"),
    "ae02": ("ae02-math.svg", "Four math pillars of AE02"),
    "ae03": ("ae03-pipeline.svg", "AE03 machine learning pipeline"),
    "ae04": ("ae04-dl.svg", "AE04 deep learning path"),
    "ae05": ("ae05-system.svg", "AE05 ML and GenAI system design"),
    "ae06": ("ae06-research.svg", "AE06 applied research loop"),
}

COURSES = [
    {
        "slug": "ae01",
        "code": "AE01",
        "months": "Months 1–2",
        "intake": {
            "start": "25/11/2026",
            "slots": [
                "Wed 20:30–22:30 GMT+7",
                "Sun 14:00–16:00 GMT+7",
            ],
            "hours": "2 hours / session",
        },
        "title": "AI Productivity & Harnesses",
        "tagline": "Work with AI like an engineer at Big Tech.",
        "audience": "Technical and non-technical professionals: PMs, BAs, operations, marketers, knowledge workers, and developers.",
        "capability": "Progress from L0 to L5 through personal assistance, collaboration, delegation, orchestration, and AI workflow operations.",
        "prereq": "Basic use of computers, files, and office applications. The non-technical track does not require programming. The technical track is for learners who can read and edit code.",
        "goal": "Use AI to complete work and achieve measurable productivity gains. Practice with documents, tabular data, workplace information, and AI coding tools to create useful applications.",
        "outcome": "Identify tasks suitable for AI, collaborate and delegate at different autonomy levels, build utilities with AI coding, configure an agent team, run goal-driven workflows, and select a useful autonomy level for each task.",
        "tools": "A paid AI seat for two months, a workspace for running utilities, templates, API quota, and setup support.",
        "proof": "Utilities, harnesses, orchestration logs, an L0–L5 record, and a productivity report.",
        "weeks": [
            ("1", "S1, L0: Select a work task, record a baseline, and define completion criteria", "S2, L1: Activate accounts, use AI for small tasks, and check for errors"),
            ("2", "S3, L2: Provide requirements, context, and examples; build a checkpoint-based collaboration workflow", "S4, L2: Use AI coding to build a small document or data utility"),
            ("3", "S5, L2: Debug with AI, run business tests, and save versions", "S6, L3: Turn requirements into a delegable task with artifacts and acceptance criteria"),
            ("4", "S7, L3: Build a custom harness with instructions, context, skills, templates, tools, and tests", "S8, L3: Let an agent complete an independent task in an isolated workspace"),
            ("5", "S9, L3: Review the result, test missing-data cases, and revise the configuration", "S10, L4: Write acceptance criteria and configure an agent team, handoff contracts, and workspaces"),
            ("6", "S11, L4: Review the plan and ask the agent team to implement the specification", "S12, L4: Verify independently and compare with a single agent"),
            ("7", "S13, L5: Configure a software factory to accept specs, build or update utilities, test, and package", "S14, L5: Run a new requirement end to end with permission, budget, and failure limits"),
            ("8", "S15, L5: Audit autonomy, review time, quality, cost, and productivity trade-offs", "S16, L5: Unguided capstone, defend the evidence, and select a practical adoption level"),
        ],
        "levels": [
            ("L0 Baseline", "Understand the current workflow and select a suitable problem"),
            ("L1 AI Assistance", "Use AI for small tasks and verify every output"),
            ("L2 AI Collaboration", "Provide context, discuss requirements, and refine results through checkpoints"),
            ("L3 Task Delegation", "Delegate a complete task and evaluate the resulting artifact"),
            ("L4 Spec-Driven AI Team", "Write acceptance criteria, configure roles and handoffs, and review plans and results"),
            ("L5 Software Factory", "Configure a workflow that implements, tests, packages, and handles exceptions"),
        ],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae02",
        "code": "AE02",
        "months": "Months 3–4",
        "intake": {
            "start": "23/12/2026",
            "slots": [
                "Thu 20:30–22:30 GMT+7",
                "Sun 20:30–22:30 GMT+7",
            ],
            "hours": "2 hours / session",
        },
        "title": "Math for ML & DL",
        "tagline": "Understand the math. Unlock the models.",
        "audience": "Learners preparing for ML, DL, research reading, or stronger mathematical foundations.",
        "capability": "Represent and reason about ML and DL concepts mathematically.",
        "prereq": "High school algebra, functions, and basic Python.",
        "goal": "Build mathematical foundations through intuition, formulas, manual calculations, and NumPy. Understand data representation, vector operations, optimization, and uncertainty.",
        "outcome": "A notebook that computes similarity and projections, optimizes a simple function, estimates probabilities, and checks gradients with finite differences.",
        "tools": "CPU notebook workspace, interactive math labs, and solution sessions.",
        "proof": "Mathematics notebook with solutions and correctness checks.",
        "weeks": [
            ("1", "S1: Scalars, vectors, matrices, tensors, shapes, and data representation", "S2: Dot products, norms, distance, and cosine similarity"),
            ("2", "S3: Matrix multiplication, linear transformations, and systems of equations", "S4: Rank, basis, projection, and least-squares geometry"),
            ("3", "S5: Eigenvalues, eigenvectors, and geometric interpretation", "S6: SVD and low-rank approximation"),
            ("4", "S7: Partial derivatives, gradients, and directional derivatives", "S8: The chain rule, Jacobians, and multivariable differentiation"),
            ("5", "S9: Gradient descent and the effect of step size", "S10: Convexity, curvature, constrained optimization, and regularization"),
            ("6", "S11: Conditional probability, independence, and Bayes' theorem", "S12: Random variables, distributions, expectation, variance, and covariance"),
            ("7", "S13: Sampling, LLN, CLT, estimation error, and confidence intervals", "S14: Likelihood, MLE, MAP, and their connection to objective functions"),
            ("8", "S15: Entropy, cross-entropy, and KL divergence", "S16: Integrated mathematics lab and notebook defense"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae03",
        "code": "AE03",
        "months": "Months 5–6",
        "title": "Machine Learning Foundations",
        "tagline": "Turn data into reliable predictions.",
        "audience": "Software engineers moving into ML and analysts building predictive models.",
        "capability": "Build and evaluate ML models.",
        "prereq": "AE02 competency and basic Python, NumPy, and pandas.",
        "goal": "Build reliable baselines, select data representations, train models, and evaluate them correctly offline. Projects may use tabular data, text classification, or simple retrieval.",
        "outcome": "A reproducible offline pipeline, benchmark, error report, and model artifact. Explain which data was used for fitting, tuning, and testing.",
        "tools": "Prepared ML environment, datasets, experiment tracking, and a list of suitable contributions.",
        "proof": "Benchmark and first contribution package.",
        "weeks": [
            ("1", "S1: Turn questions into supervised or unsupervised problems, then define targets and baselines", "S2: Train / validation / test splits, including time-based and group-based splits and data leakage"),
            ("2", "S3: Linear regression, fitting, residuals, and prediction", "S4: GD, SGD, feature scaling, and regularization for regression"),
            ("3", "S5: Logistic regression and predictive probabilities", "S6: Regression and classification metrics, thresholds, and imbalanced data"),
            ("4", "S7: Decision trees, splitting, impurity, and overfitting", "S8: Random forests, bagging, and the bias-variance trade-off"),
            ("5", "S9: Gradient boosting and tabular-data baselines", "S10: Cross-validation, hyperparameter search, and experiment tracking"),
            ("6", "S11: Feature transformation, missing data, and preprocessing pipelines", "S12: PCA, dimension selection, and information-loss evaluation"),
            ("7", "S13: K-means and nearest neighbors", "S14: TF-IDF, retrieval baselines, and search evaluation metrics"),
            ("8", "S15: Error analysis, calibration, and errors across data groups", "S16: Defend the ML pipeline and model selection decisions"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae04",
        "code": "AE04",
        "months": "Months 7–8",
        "title": "Deep Learning Foundations",
        "tagline": "Build, train, and adapt neural models.",
        "audience": "Learners with ML knowledge who want to study DL, NLP, and foundation models.",
        "capability": "Train and adapt neural networks.",
        "prereq": "AE03 competency and an understanding of gradients, overfitting, and offline evaluation.",
        "goal": "Understand neural networks, build training loops, debug training, and adapt pretrained models. Practice focuses on text and representation learning; CNNs broaden intuition.",
        "outcome": "A mini language-model checkpoint trained from scratch, an SFT model or adapter, training logs, a model card, and an offline benchmark. Weeks 6–8 GPU labs.",
        "tools": "Individual GPU quota, checkpoint storage, training recipes, and debugging support.",
        "proof": "Checkpoint, adapter, training logs, and model card.",
        "weeks": [
            ("1", "S1: PyTorch tensor operations, broadcasting, devices, and autograd", "S2: MLP layers, activations, forward passes, and loss"),
            ("2", "S3: Backpropagation and the chain rule in neural networks", "S4: Training loops, data loaders, batching, and checkpoints"),
            ("3", "S5: Momentum, Adam, and learning-rate schedules", "S6: Initialization, normalization, dropout, and regularization"),
            ("4", "S7: Debugging gradients and learning curves, then overfitting one batch", "S8: CNNs and transfer learning through a small image task"),
            ("5", "S9: Tokenization, embeddings, and sequence representation", "S10: Attention: queries, keys, values, and masking"),
            ("6", "S11: Transformer encoders, decoders, and token positions", "S12: Language modeling, pretraining, token generation — launch mini LM lab"),
            ("7", "S13: Supervised fine-tuning and PEFT / LoRA with a small model", "S14: Contrastive learning and embedding training"),
            ("8", "S15: Model ablation, memory and compute profiling, and baseline comparison", "S16: Demo, error analysis, and model card defense"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
    },
    {
        "slug": "ae05",
        "code": "AE05",
        "months": "Months 9–10",
        "title": "ML & GenAI System Design",
        "tagline": "Design for production. Defend every trade-off.",
        "audience": "Software, AI, and ML engineers preparing for system design interviews or production AI work.",
        "capability": "Design ML and GenAI systems under product constraints.",
        "prereq": "AE03 and AE04 competency, plus API, HTTP, SQL, and Git. A pre-module assignment checks containers, queues, and basic distributed systems.",
        "goal": "Design, present, and validate an ML or GenAI architecture under product constraints. Supports both production work and ML / AI system design interviews.",
        "outcome": "Time-limited lab demo, design document, and operations report. Defend diagrams, estimates, and trade-offs.",
        "tools": "Deployment sandbox, API budget, load-testing tools, and monitoring tools.",
        "proof": "Demo, design document, and operations report.",
        "weeks": [],
        "sessions": [
            ("S1", "Define the problem and product constraints", "Define users, workflows, scale, and budget. Record assumptions and assess whether ML is necessary"),
            ("S2", "Connect model quality to product outcomes", "Build an objective tree with business goals, offline metrics, and operational limits"),
            ("S3", "Draft the minimum architecture", "Draw request and training flows. Define interfaces and independently replaceable components"),
            ("S4", "Design data sources and flows", "Data contracts, labeling, storage, and lineage. Handle late data and schema changes"),
            ("S5", "Organize features in the system", "Where and when features are computed and versioned. Point-in-time correctness and serving consistency"),
            ("S6", "Model development and acceptance", "Use AE03–AE04 benchmarks to select a model. Training jobs, registry, reproducibility, release criteria"),
            ("S7", "Design the prediction service", "API contract and latency budget. Synchronous or asynchronous serving"),
            ("S8", "Validate online and release", "Experiment groups, guardrail metrics, stopping criteria, and rollback paths"),
            ("S9", "Scale and maintain the system", "Capacity plan, alerts, incident responsibilities, and update rules"),
            ("S10", "GenAI: model and knowledge strategy", "Decision record: retrieval, long context, adaptation, tool use; API vs self-hosting"),
            ("S11", "GenAI: verifiable RAG", "Index updates, hybrid retrieval, reranking, citations; expired documents and permissions"),
            ("S12", "GenAI: budget for inference", "Caching, batching, routing, precision. Time to first token vs total completion time"),
            ("S13", "GenAI: quality evaluation", "Eval set, calibrate judges with human labels, block regressions before release"),
            ("S14", "GenAI: operations and execution boundaries", "Failure budgets, sensitive data, retries, idempotency, traces, tool contracts"),
            ("S15", "ML case study: recommendation or ranking", "Apply all nine steps, defend diagrams and estimates, load-test a deployed slice"),
            ("S16", "GenAI case study: mock interview", "Present an LLM/RAG system under changing requirements; quality, latency, cost, operations"),
        ],
        "levels": [],
        "schedule_kind": "sessions",
    },
    {
        "slug": "ae06",
        "code": "AE06",
        "months": "Months 11–12",
        "title": "Frontier AI Lab",
        "tagline": "Explore the frontier. Learn to research.",
        "audience": "AI engineers, technical leads, and builders who want research skills, with an optional paper track.",
        "capability": "Conduct applied research on emerging AI topics selected each year.",
        "prereq": "AE03 and AE04 completed. AE05 helps if you bring a system into the experiments.",
        "goal": "Research is an engineering skill even if you do not plan to publish. Half the module is seminars on emerging AI topics. The other half: experiment design, practical work, and presentations.",
        "outcome": "Research report and prototype, with an optional manuscript or contribution package.",
        "tools": "Research sandbox, API budget, GPUs when needed, research clinics, and mentor review.",
        "proof": "Research report, prototype, and optional paper or contribution package.",
        "weeks": [
            ("1–2", "Seminars on this year's frontier: read papers, extract claims, ask questions", "Research skills: question, hypothesis, and experiment scope"),
            ("3–4", "Design experiments: baseline, metrics, and success criteria", "Reproduce or test a claim; log results and limitations"),
            ("5–6", "Prototype / ablation on the sandbox and allocated GPUs", "Research clinic: mentor review of direction and evidence"),
            ("7–8", "Write the research report and present results", "Defense: explain, revise live, and decide the next step"),
        ],
        "levels": [],
        "schedule_kind": "weeks",
        "week_headers": ("Weeks", "Focus A", "Focus B"),
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
      <a class="btn btn-msg" href="{MSG}" target="_blank" rel="noopener">{messenger_icon()} Tư vấn</a>
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


def messenger_icon() -> str:
    return """<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M.001 11.639C.001 4.949 5.241 0 12.001 0 18.762 0 24 4.95 24 11.639c0 6.689-5.238 11.638-11.999 11.638-1.21 0-2.38-.16-3.47-.46a.96.96 0 00-.64.05l-2.39 1.05a.96.96 0 01-1.35-.85l-.07-2.14a.97.97 0 00-.32-.68A11.39 11.39 0 010 11.639zm8.32-2.19l-3.52 5.6c-.35.53.32 1.139.82.75l3.79-2.87a.724.724 0 01.87 0l2.8 2.1c.84.63 2.04.41 2.6-.48l3.52-5.6c.35-.53-.32-1.13-.82-.75l-3.79 2.87a.724.724 0 01-.87 0l-2.8-2.1a1.8 1.8 0 00-2.6.48z"/></svg>"""


def messenger_fab() -> str:
    return f"""<a class="msg-fab" href="{MSG}" target="_blank" rel="noopener" aria-label="Nhắn tin tư vấn qua Messenger">
  {messenger_icon()}
</a>"""


def gtag_snippet() -> str:
    return f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>"""


def page(title: str, description: str, path: str, prefix: str, active: str, body: str, extra_head: str = "") -> str:
    canonical = f"{SITE}/{path}" if path else f"{SITE}/"
    og = f"{SITE}/assets/img/og-share.png"
    return f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  {gtag_snippet()}
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
    {diagram_figure("roadmap-12.svg", "12-month path, six modules AE01 to AE06", "")}
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
          <thead><tr><th>Session</th><th>Focus</th><th>Exercise / deliverable</th></tr></thead>
          <tbody>{rows}</tbody>
        </table></div>"""
    h1, h2, h3 = course.get("week_headers", ("Week", "Session 1", "Session 2"))
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
          <thead><tr><th>Level</th><th>Capability</th></tr></thead><tbody>{rows}</tbody></table></div>"""
    pager = '<div class="pager">'
    if prev_c:
        pager += f'<a href="../{prev_c["slug"]}/"><small>Previous</small><strong>{prev_c["code"]} · {prev_c["title"]}</strong></a>'
    else:
        pager += "<span></span>"
    if next_c:
        pager += f'<a href="../{next_c["slug"]}/" style="text-align:right"><small>Next</small><strong>{next_c["code"]} · {next_c["title"]}</strong></a>'
    pager += "</div>"
    chips = "".join(
        f'<span class="chip">{x}</span>'
        for x in (c["code"], course_when(c), "16 sessions · 8 weeks", "Mentor Big Tech")
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
    <article class="card"><h3>Prerequisites</h3><p>{c["prereq"]}</p></article>
    <article class="card"><h3>Outcomes</h3><p>{c["outcome"]}</p></article>
    <article class="card"><h3>Audience</h3><p>{c["audience"]}</p></article>
    <article class="card"><h3>Core capability</h3><p>{c["capability"]}</p></article>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head"><div class="kicker">Syllabus</div><h2>16 sessions in 8 weeks.</h2></div>
    {levels}
    {schedule_table(c)}
  </div>
</section>
<section>
  <div class="wrap split">
    <article class="card"><div class="icon-pill">Lab</div><h3>Tools &amp; access</h3><p>{c["tools"]}</p></article>
    <article class="card"><div class="icon-pill">CV</div><h3>Evidence you keep</h3><p>{c["proof"]}</p></article>
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
    {diagram_figure("roadmap-12.svg", "12-month path, six modules AE01 to AE06", "../")}
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
  <a class="sched-main" href="../khoa-hoc/{c["slug"]}/">
    <div class="when">Khai giảng {intake["start"]}</div>
    <span class="soon">Đang mở đăng ký</span>
    <h3>{c["code"]} · {c["title"]}</h3>
    <p>{c["tagline"]}</p>
    <ul class="slots">{slots}</ul>
    <p>16 sessions · 8 weeks · {intake["hours"]}</p>
    <p class="sched-go">Xem syllabus →</p>
  </a>
  <div class="open"><a class="btn btn-primary" href="{MSG}" target="_blank" rel="noopener">Đăng ký qua Messenger</a></div>
</article>"""
            )
        else:
            cards.append(
                f"""<article class="sched-card reveal">
  <a class="sched-main" href="../khoa-hoc/{c["slug"]}/">
    <div class="when">{c["months"]} · Sắp công bố</div>
    <h3>{c["code"]} · {c["title"]}</h3>
    <p>{c["tagline"]}</p>
    <p>16 sessions · 8 weeks · GMT+7</p>
    <p class="sched-go">Xem syllabus →</p>
  </a>
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
