"""
DevFahad — Personal Portfolio (Upgraded)
A single-page, mobile-first, dark-mode portfolio built with Streamlit.

Features
--------
• Instant-loading CDN favicon
• Animated coding/AI Lottie in the hero (streamlit-lottie)
• Sticky nav with italic tagline
• Fluid, relative column ratios (mobile → desktop)
• Rich hover animations on every CTA button
• Custom CSS media queries for perfect mobile stacking

Run
---
    pip install -r requirements.txt
    streamlit run app.py
"""

from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# ---------- Page Config (favicon + title) ----------
FAVICON_URL = "https://cdn-icons-png.flaticon.com/512/3242/3242257.png"

st.set_page_config(
    page_title="DevFahad — AI-Augmented Engineer",
    page_icon=FAVICON_URL,          # instant-load CDN favicon
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Lottie loader (with graceful fallback) ----------
@st.cache_data(show_spinner=False, ttl=3600)
def load_lottie(url: str) -> dict | None:
    """Fetch a Lottie JSON. Returns None on any failure."""
    try:
        r = requests.get(url, timeout=8)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


# Primary (user-requested) URL first; fallbacks if the CDN 403s.
LOTTIE_CANDIDATES = [
    "https://assets5.lottiefiles.com/packages/lf20_fcfwnr0q.json",  # requested
    "https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json",  # coder at laptop
    "https://assets9.lottiefiles.com/packages/lf20_iv4dsx3q.json",  # developer animation
    "https://assets1.lottiefiles.com/packages/lf20_M9p23l.json",    # dev workflow
]

lottie_animation = None
for _url in LOTTIE_CANDIDATES:
    lottie_animation = load_lottie(_url)
    if lottie_animation:
        break


# ---------- Global Styles (Dark Mode + Responsive) ----------
CUSTOM_CSS = """
<style>
/* ---- Fonts ---- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

/* ---- Base ---- */
html, body, [class*="css"], .stApp {
    background: radial-gradient(1200px 600px at 20% -10%, rgba(99, 102, 241, 0.15), transparent 60%),
                radial-gradient(900px 500px at 100% 10%, rgba(16, 185, 129, 0.10), transparent 60%),
                #0b0f19 !important;
    color: #e5e7eb !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    overflow-x: hidden;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 3rem !important;
    max-width: 1180px !important;
}

/* ---- Navigation ---- */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    padding: 12px 22px;
    margin-bottom: 20px;
    background: rgba(17, 24, 39, 0.55);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    position: sticky;
    top: 8px;
    z-index: 999;
    flex-wrap: wrap;
}
.nav-left { display: flex; align-items: center; gap: 14px; flex: 1 1 auto; min-width: 0; }
.nav-brand {
    font-weight: 800; font-size: 1.05rem; color: #fff;
    letter-spacing: 0.3px; white-space: nowrap;
}
.nav-brand span { color: #6366f1; }
.nav-divider {
    width: 1px; height: 20px;
    background: rgba(255,255,255,0.12);
}
.nav-tagline {
    font-style: italic;
    font-weight: 400;
    font-size: 0.85rem;
    color: #94a3b8;
    letter-spacing: 0.2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.nav-links { display: flex; align-items: center; }
.nav-links a {
    color: #cbd5e1 !important; text-decoration: none !important;
    margin-left: 18px; font-size: 0.9rem; font-weight: 500;
    transition: color 0.2s ease;
}
.nav-links a:hover { color: #a5b4fc !important; }

/* ---- Hero Wrapper ---- */
.hero-wrap {
    padding: 40px 32px;
    border-radius: 22px;
    background: linear-gradient(145deg, rgba(30,41,59,0.7), rgba(17,24,39,0.4));
    border: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}
.hero-wrap::before {
    content: ""; position: absolute; inset: 0;
    background: radial-gradient(600px 300px at 20% 0%, rgba(99,102,241,0.18), transparent 60%);
    pointer-events: none;
}

/* Style the actual st.image() portrait */
[data-testid="stImage"] img {
    border-radius: 20px !important;
    border: 3px solid transparent;
    background:
        linear-gradient(#0b0f19, #0b0f19) padding-box,
        linear-gradient(135deg, #6366f1, #10b981) border-box;
    box-shadow:
        0 20px 45px rgba(0,0,0,0.5),
        0 0 0 6px rgba(99,102,241,0.08);
    transition: all 0.35s ease;
    max-width: 100% !important;
    height: auto !important;
}
[data-testid="stImage"] img:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow:
        0 25px 55px rgba(99,102,241,0.35),
        0 0 0 6px rgba(99,102,241,0.15);
}

.hero-content { padding-left: 6px; }
.hero-badge {
    display: inline-block; padding: 6px 14px; border-radius: 999px;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #a5b4fc; font-size: 0.78rem; font-weight: 500;
    margin-bottom: 16px; letter-spacing: 0.4px;
}
.hero-content h1 {
    font-size: clamp(2rem, 5vw, 3.4rem);
    font-weight: 800; letter-spacing: -1.5px;
    margin: 0 0 14px 0; line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 55%, #34d399 100%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-content p.tagline {
    font-size: clamp(0.95rem, 1.6vw, 1.1rem);
    color: #cbd5e1; margin: 0 0 20px 0;
    line-height: 1.65; font-weight: 400;
}
.hero-content p.tagline b { color: #a5b4fc; }
.hero-content .location {
    display: inline-flex; align-items: center; gap: 6px;
    color: #94a3b8; font-size: 0.9rem; font-weight: 500;
    padding: 6px 12px; border-radius: 999px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
}
.hero-content .location svg { width: 14px; height: 14px; }

/* Lottie container */
.lottie-wrap {
    display: flex; justify-content: center; align-items: center;
    padding: 6px;
}

/* ---- Section headings ---- */
.section { margin-top: 56px; scroll-margin-top: 90px; }
.section-title {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 2px;
    color: #6366f1; text-transform: uppercase; margin-bottom: 8px;
    font-family: 'JetBrains Mono', monospace;
}
.section-heading {
    font-size: clamp(1.6rem, 3.5vw, 2.2rem);
    font-weight: 700; color: #f1f5f9; margin: 0 0 24px 0;
    letter-spacing: -0.5px;
}

/* ---- About ---- */
.about-card {
    padding: 32px; border-radius: 16px;
    background: rgba(30, 41, 59, 0.45);
    border: 1px solid rgba(255,255,255,0.06);
    font-size: 1.02rem; line-height: 1.75; color: #cbd5e1;
    transition: all 0.3s ease;
}
.about-card:hover {
    border-color: rgba(99,102,241,0.35);
    transform: translateY(-3px);
}
.about-card b { color: #f1f5f9; font-weight: 600; }
.about-card .accent { color: #a5b4fc; font-weight: 600; }

/* ---- Skills grid ---- */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 18px;
}
.skill-card {
    padding: 24px; border-radius: 14px;
    background: rgba(30, 41, 59, 0.45);
    border: 1px solid rgba(255,255,255,0.06);
    transition: all 0.3s ease;
}
.skill-card:hover {
    transform: translateY(-5px);
    border-color: rgba(99, 102, 241, 0.5);
    background: rgba(30, 41, 59, 0.75);
    box-shadow: 0 12px 30px rgba(99,102,241,0.15);
}
.skill-icon {
    width: 44px; height: 44px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(16,185,129,0.15));
    color: #a5b4fc; font-size: 1.3rem; margin-bottom: 14px;
    border: 1px solid rgba(99,102,241,0.25);
}
.skill-card h3 { color: #f1f5f9; font-size: 1.05rem; font-weight: 600; margin: 0 0 6px 0; }
.skill-card p { color: #94a3b8; font-size: 0.88rem; line-height: 1.55; margin: 0; }
.skill-tag {
    display: inline-block; margin-top: 10px; padding: 3px 10px;
    background: rgba(16, 185, 129, 0.12); color: #6ee7b7;
    border-radius: 999px; font-size: 0.72rem; font-weight: 500;
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid rgba(16,185,129,0.25);
}

/* ---- Projects ---- */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 22px;
}
.project-card {
    padding: 28px; border-radius: 16px;
    background: linear-gradient(160deg, rgba(30,41,59,0.7), rgba(17,24,39,0.55));
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.3s ease;
    display: flex; flex-direction: column; height: 100%;
}
.project-card:hover {
    transform: translateY(-6px);
    border-color: rgba(99,102,241,0.5);
    box-shadow: 0 15px 35px rgba(0,0,0,0.35);
}
.project-header {
    display: flex; justify-content: space-between; align-items: flex-start;
    margin-bottom: 6px; gap: 12px; flex-wrap: wrap;
}
.project-title {
    font-size: 1.25rem; font-weight: 700; color: #f1f5f9; margin: 0;
    font-family: 'JetBrains Mono', monospace; letter-spacing: -0.3px;
}
.project-role {
    display: inline-block; padding: 4px 10px; border-radius: 6px;
    background: rgba(99,102,241,0.15); color: #a5b4fc;
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.3px;
    border: 1px solid rgba(99,102,241,0.3);
    white-space: nowrap;
}
.project-url {
    color: #6ee7b7 !important; text-decoration: none !important;
    font-size: 0.88rem; margin-bottom: 18px;
    font-family: 'JetBrains Mono', monospace;
    display: inline-flex; align-items: center; gap: 4px;
    transition: all 0.3s ease;
}
.project-url:hover { color: #34d399 !important; text-decoration: underline !important; transform: translateX(3px); }
.project-block { margin-top: 14px; }
.project-block h4 {
    font-size: 0.75rem; font-weight: 700; letter-spacing: 1.5px;
    text-transform: uppercase; color: #6366f1;
    margin: 0 0 6px 0; font-family: 'JetBrains Mono', monospace;
}
.project-block p { color: #cbd5e1; font-size: 0.92rem; line-height: 1.65; margin: 0; }

/* ---- Contact / Footer ---- */
.contact-card {
    padding: 40px 32px; border-radius: 20px;
    background: linear-gradient(145deg, rgba(30,41,59,0.7), rgba(17,24,39,0.5));
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
    margin-top: 40px;
}
.contact-card h2 {
    font-size: clamp(1.6rem, 3.5vw, 2rem); font-weight: 700;
    color: #f1f5f9; margin: 0 0 10px 0; letter-spacing: -0.5px;
}
.contact-card p { color: #94a3b8; font-size: 1rem; margin: 0 0 24px 0; }

.contact-buttons {
    display: flex; justify-content: center; gap: 12px;
    flex-wrap: wrap; margin-bottom: 10px;
}

/* ---- Universal Button (with rich hover) ---- */
.btn {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 12px 22px; border-radius: 10px;
    font-size: 0.93rem; font-weight: 600;
    text-decoration: none !important;
    border: 1px solid transparent;
    transition: all 0.3s ease;   /* smooth for every property */
    will-change: transform;
}
.btn:hover {
    transform: translateY(-5px);  /* requested lift */
}
.btn svg { width: 16px; height: 16px; }

.btn-primary {
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: #fff !important;
    box-shadow: 0 4px 14px rgba(99,102,241,0.35);
}
.btn-primary:hover {
    box-shadow: 0 12px 28px rgba(99,102,241,0.55);
    filter: brightness(1.05);
}
.btn-secondary {
    background: rgba(255,255,255,0.05);
    color: #e5e7eb !important;
    border-color: rgba(255,255,255,0.12);
}
.btn-secondary:hover {
    background: rgba(255,255,255,0.12);
    border-color: rgba(255,255,255,0.28);
    box-shadow: 0 10px 24px rgba(0,0,0,0.35);
}
.whatsapp-btn {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 12px 22px; border-radius: 10px;
    background: linear-gradient(135deg, #25d366, #128c7e);
    border: 1px solid rgba(37, 211, 102, 0.4);
    color: #ffffff !important;
    font-size: 0.93rem; font-weight: 600;
    text-decoration: none !important;
    box-shadow: 0 4px 14px rgba(37, 211, 102, 0.25);
    transition: all 0.3s ease;
    will-change: transform;
}
.whatsapp-btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 28px rgba(37, 211, 102, 0.5);
    filter: brightness(1.05);
}

.footer-credit {
    text-align: center; margin-top: 32px;
    color: #64748b; font-size: 0.82rem;
    padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.05);
}
.footer-credit span { color: #a5b4fc; }

/* ==========================================================
   RESPONSIVE MEDIA QUERIES
   ========================================================== */

/* Tablet */
@media (max-width: 900px) {
    .nav-tagline { font-size: 0.8rem; }
    .hero-wrap { padding: 34px 24px; }
}

/* Small tablet — hide nav tagline to avoid clutter */
@media (max-width: 780px) {
    .nav-tagline, .nav-divider { display: none; }
}

/* Mobile */
@media (max-width: 640px) {
    .block-container { padding-left: 0.8rem !important; padding-right: 0.8rem !important; }
    .hero-wrap { padding: 30px 18px; text-align: center; }
    .hero-content { padding-left: 0; text-align: center; }
    .about-card, .project-card, .skill-card { padding: 22px; }
    .contact-card { padding: 32px 20px; }
    .nav-links { display: none; }
    .nav-bar { padding: 10px 16px; }
    .btn, .whatsapp-btn { padding: 12px 18px; font-size: 0.9rem; width: 100%; justify-content: center; }
    .contact-buttons { flex-direction: column; align-items: stretch; }
    [data-testid="stImage"] { display: flex; justify-content: center; }
    /* Streamlit columns stack automatically at <640px; make sure Lottie stays centered */
    .lottie-wrap { max-width: 320px; margin: 0 auto; }
}

/* Very small phones */
@media (max-width: 380px) {
    .hero-content h1 { font-size: 1.9rem; }
    .section-heading { font-size: 1.5rem; }
    .contact-card h2 { font-size: 1.4rem; }
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------- Navigation (with italic tagline) ----------
st.markdown("""
<div class="nav-bar">
    <div class="nav-left">
        <div class="nav-brand">Dev<span>Fahad</span></div>
        <div class="nav-divider"></div>
        <div class="nav-tagline">Turning complex ideas into seamless digital realities.</div>
    </div>
    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- HERO (Photo + Text + Lottie) ----------
st.markdown('<div class="hero-wrap" id="home">', unsafe_allow_html=True)

# Fluid, relative ratios → scales perfectly across screens
col_photo, col_text, col_anim = st.columns([1, 1.6, 1.2], gap="large", vertical_alignment="center")

with col_photo:
    IMAGE_PATH = Path(__file__).parent / "image_3.webp"
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width=300)
    else:
        st.warning("⚠️ `image_3.webp` not found next to `app.py`.")

with col_text:
    st.markdown("""
    <div class="hero-content">
        <div class="hero-badge">👋 AVAILABLE FOR PROJECTS</div>
        <h1>DevFahad</h1>
        <p class="tagline">
            Building Scalable Digital Ecosystems &amp; Interactive Experiences
            through <b>AI-Augmented Engineering</b>.
        </p>
        <div class="location">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Peshawar, Pakistan
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_anim:
    st.markdown('<div class="lottie-wrap">', unsafe_allow_html=True)
    if lottie_animation:
        st_lottie(
            lottie_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=260,
            key="hero-lottie",
        )
    else:
        # Elegant graphical fallback (pure SVG) if Lottie CDN is unreachable
        st.markdown("""
        <svg viewBox="0 0 260 260" width="220" height="220" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#6366f1"/>
              <stop offset="100%" stop-color="#10b981"/>
            </linearGradient>
          </defs>
          <circle cx="130" cy="130" r="100" fill="none" stroke="url(#g)" stroke-width="2" opacity="0.4">
            <animate attributeName="r" values="90;105;90" dur="4s" repeatCount="indefinite"/>
          </circle>
          <g fill="none" stroke="url(#g)" stroke-width="3" stroke-linecap="round">
            <path d="M95 110 L70 130 L95 150"/>
            <path d="M165 110 L190 130 L165 150"/>
            <path d="M145 100 L115 160"/>
          </g>
        </svg>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------- ABOUT ----------
st.markdown("""
<div class="section" id="about">
    <div class="section-title">// 01 — About</div>
    <h2 class="section-heading">Who I Am</h2>
    <div class="about-card">
        I'm a <b>developer</b> who leverages <span class="accent">AI and modern tools</span>
        to design and ship end-to-end digital products. My focus spans
        <b>UI/UX design</b>, <b>web applications</b>, <b>eCommerce platforms</b>,
        and <b>interactive games</b>. I believe the best products come from combining
        strong engineering fundamentals with thoughtful design — accelerated by an
        AI-first workflow that turns ideas into shipped software, fast.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- SKILLS ----------
st.markdown("""
<div class="section" id="skills">
    <div class="section-title">// 02 — Skills</div>
    <h2 class="section-heading">What I Do</h2>
    <div class="skills-grid">
        <div class="skill-card">
            <div class="skill-icon">🎨</div>
            <h3>UI/UX Design</h3>
            <p>Crafting clean, intuitive interfaces with a focus on hierarchy, accessibility, and delightful micro-interactions.</p>
            <div class="skill-tag">Figma · Design Systems</div>
        </div>
        <div class="skill-card">
            <div class="skill-icon">💻</div>
            <h3>Web Development</h3>
            <p>Building responsive, performant web applications end-to-end — from static sites to full-stack platforms.</p>
            <div class="skill-tag">React · Next.js · Streamlit</div>
        </div>
        <div class="skill-card">
            <div class="skill-icon">🛒</div>
            <h3>eCommerce</h3>
            <p>Designing and deploying storefronts optimized for conversion, speed, and a seamless checkout experience.</p>
            <div class="skill-tag">Shopify · Custom Stacks</div>
        </div>
        <div class="skill-card">
            <div class="skill-icon">🎮</div>
            <h3>Game Development</h3>
            <p>Prototyping and shipping interactive game experiences with AI-augmented tooling for rapid iteration.</p>
            <div class="skill-tag">CodeWisp · Arena AI</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- PROJECTS ----------
st.markdown("""
<div class="section" id="projects">
    <div class="section-title">// 03 — Projects</div>
    <h2 class="section-heading">Selected Work</h2>
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-header">
                <h3 class="project-title">ToolboxTools</h3>
                <span class="project-role">Sole Developer</span>
            </div>
            <a class="project-url" href="https://toolboxtools.netlify.app" target="_blank" rel="noopener">
                ↗ toolboxtools.netlify.app
            </a>
            <div class="project-block">
                <h4>Goal</h4>
                <p>Build an all-in-one, browser-based toolbox that consolidates dozens of
                everyday utilities — converters, generators, and calculators — into a single
                fast, ad-free interface.</p>
            </div>
            <div class="project-block">
                <h4>Impact</h4>
                <p>Replaces the need to juggle multiple single-purpose sites, delivering a
                unified, distraction-free experience that saves users time on repetitive
                digital tasks.</p>
            </div>
        </div>
        <div class="project-card">
            <div class="project-header">
                <h3 class="project-title">FinCalcHub</h3>
                <span class="project-role">Sole Developer</span>
            </div>
            <a class="project-url" href="https://fincalchub.xyz" target="_blank" rel="noopener">
                ↗ fincalchub.xyz
            </a>
            <div class="project-block">
                <h4>Goal</h4>
                <p>Create a comprehensive financial-calculator hub covering loans, mortgages,
                investments, and taxes — designed to make complex financial planning
                accessible to everyone.</p>
            </div>
            <div class="project-block">
                <h4>Impact</h4>
                <p>Empowers users to make informed money decisions with clear, transparent
                calculations and a mobile-friendly UX built for real-world financial planning.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- CONTACT ----------
st.markdown("""
<div class="section" id="contact">
    <div class="section-title">// 04 — Contact</div>
    <h2 class="section-heading">Let's Build Something</h2>
    <div class="contact-card">
        <h2>Have a project in mind?</h2>
        <p>I'm open to freelance work, collaborations, and interesting conversations.</p>
        <div class="contact-buttons">
            <a class="btn btn-primary" href="mailto:believerbk4@gmail.com">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
                Email Me
            </a>
            <a class="btn btn-secondary" href="https://github.com/Fahadkhan590" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.1.79-.25.79-.56 0-.28-.01-1.02-.02-2-3.2.7-3.87-1.54-3.87-1.54-.52-1.33-1.28-1.68-1.28-1.68-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.25.45-2.28 1.18-3.09-.12-.29-.51-1.46.11-3.04 0 0 .97-.31 3.18 1.18a11.03 11.03 0 0 1 5.79 0c2.21-1.49 3.18-1.18 3.18-1.18.62 1.58.23 2.75.11 3.04.73.81 1.18 1.84 1.18 3.09 0 4.41-2.69 5.38-5.25 5.67.41.35.78 1.05.78 2.12 0 1.53-.01 2.76-.01 3.14 0 .31.21.67.8.55C20.22 21.39 23.5 17.08 23.5 12 23.5 5.65 18.35.5 12 .5z"/>
                </svg>
                GitHub
            </a>
            <a class="btn btn-secondary" href="https://www.youtube.com/channel/UCPbvK3VQ_dtFCUlC403AxEg" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31.3 31.3 0 0 0 0 12a31.3 31.3 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1c.4-1.9.5-3.9.5-5.8s-.1-3.9-.5-5.8zM9.6 15.6V8.4l6.3 3.6-6.3 3.6z"/>
                </svg>
                YouTube
            </a>
            <a class="whatsapp-btn" href="https://wa.me/923145265503" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                    <path d="M20.5 3.5A11.9 11.9 0 0 0 12 0C5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6c1.7.9 3.7 1.4 5.7 1.4h.1c6.6 0 12-5.4 12-12 0-3.2-1.3-6.2-3.5-8.3zM12 21.8h-.1c-1.8 0-3.6-.5-5.1-1.4l-.4-.2-3.7 1 1-3.6-.2-.4c-1-1.6-1.5-3.4-1.5-5.2 0-5.5 4.5-10 10-10 2.7 0 5.2 1 7.1 2.9 1.9 1.9 2.9 4.4 2.9 7.1 0 5.5-4.5 9.8-10 9.8zm5.5-7.3c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.2s-.8 1-1 1.2c-.2.2-.4.2-.7 0-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.7l.5-.6c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5s-.7-1.7-1-2.3c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.3 5.2 4.6 3.1 1.3 3.1.9 3.7.8.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/>
                </svg>
                WhatsApp: +92 314 5265503
            </a>
        </div>
    </div>
    <div class="footer-credit">
        © 2026 <span>DevFahad</span> · Crafted with Streamlit &amp; AI-Augmented Engineering
    </div>
</div>
""", unsafe_allow_html=True)
