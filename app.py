import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import os

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Abbas Ali | AI & Data Science Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== LOAD CSS =====
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ===== LOTTIE LOADER =====
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_ai      = load_lottie("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
lottie_skills  = load_lottie("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_contact = load_lottie("https://assets2.lottiefiles.com/packages/lf20_u25cckyh.json")
lottie_coding  = load_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_edu     = load_lottie("https://assets3.lottiefiles.com/packages/lf20_DMgKk1.json")

# ===== RESUME PDF =====
resume_path = "Abbas_Ali_Resume.pdf"
resume_bytes = open(resume_path, "rb").read() if os.path.exists(resume_path) else b""

# ===== NAVIGATION =====
selected = option_menu(
    menu_title=None,
    options=["Home", "Skills", "Projects", "Education", "Contact"],
    icons=["house-fill", "cpu-fill", "folder2-open", "mortarboard-fill", "envelope-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "10px 20px", "background-color": "rgba(8,11,20,0.97)",
                      "border-bottom": "1px solid rgba(102,126,234,0.2)"},
        "icon": {"color": "#667eea", "font-size": "16px"},
        "nav-link": {
            "font-size": "14px", "font-weight": "500",
            "text-align": "center", "padding": "10px 22px",
            "border-radius": "12px", "color": "#94a3b8",
            "--hover-color": "rgba(102,126,234,0.1)",
            "transition": "all 0.3s ease"
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, #667eea, #764ba2)",
            "color": "white", "font-weight": "600",
            "box-shadow": "0 4px 15px rgba(102,126,234,0.4)"
        },
    }
)

# ═══════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════
if selected == "Home":

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <div class="hero-wrapper">
            <p class="hero-greeting">✦ Welcome to my Portfolio</p>
            <h1 class="hero-name">Abbas Ali<br>Palsaniya</h1>
            <p class="hero-role">Aspiring <span>AI Engineer</span> &amp; <span>Data Scientist</span><span class="cursor"></span></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="about-card">
            <p>
                🚀 Aspiring AI Engineer with a strong interest in <strong style="color:#a5b4fc;">Artificial Intelligence</strong>
                and <strong style="color:#a5b4fc;">Data Science</strong>. Currently upskilling through a
                <strong style="color:#a5b4fc;">Data Science with AI program</strong>, building a solid foundation in
                data analysis, visualization, and programming.<br><br>
                Proficient in <strong style="color:#a5b4fc;">Python, SQL, Power BI, Tableau, Looker Studio,</strong> and
                <strong style="color:#a5b4fc;">Excel</strong>. A quick learner with adaptability and a growth-focused mindset.
                Seeking entry-level opportunities to apply skills, gain practical exposure, and grow with a forward-thinking team.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="social-row">
            <a href="https://www.linkedin.com/in/abbasalip" target="_blank" class="social-btn social-btn-primary">
                💼 LinkedIn
            </a>
            <a href="https://github.com/abbas2407" target="_blank" class="social-btn social-btn-primary">
                💻 GitHub
            </a>
            <a href="mailto:abbas.off24@gmail.com" class="social-btn social-btn-outline">
                📧 Email Me
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if resume_bytes:
            st.download_button(
                label="📄  Download Resume",
                data=resume_bytes,
                file_name="Abbas_Ali_Palsaniya_Resume.pdf",
                mime="application/pdf",
                use_container_width=False
            )

    with col2:
        st.markdown("<div class='lottie-float'>", unsafe_allow_html=True)
        if lottie_coding:
            st_lottie(lottie_coding, height=420, key="hero_anim")
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Stats ──
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Quick Highlights</div>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("2", "ML Projects"),
        ("5+", "Tools & Libraries"),
        ("3+", "Years of Study"),
        ("100%", "Dedication"),
    ]
    for col, (num, label) in zip([c1, c2, c3, c4], stats):
        col.markdown(f"""
        <div class="stat-card">
            <span class="stat-number">{num}</span>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# SKILLS
# ═══════════════════════════════════════════════════
elif selected == "Skills":

    st.markdown("""
    <div class="section-header">
        <div class="section-title">🛠️ Skills & Technologies</div>
        <p class="section-sub">Tools and technologies I work with</p>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        # Programming
        st.markdown("""
        <div class="skill-category-card">
            <div class="skill-cat-title">🐍 Python & Data Libraries</div>
            <div class="skill-item">
                <div class="skill-label"><span>Python</span><span class="skill-pct">85%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:85%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Pandas & NumPy</span><span class="skill-pct">82%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:82%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Matplotlib & Seaborn</span><span class="skill-pct">80%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:80%;"></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ML
        st.markdown("""
        <div class="skill-category-card">
            <div class="skill-cat-title">🤖 Machine Learning</div>
            <div class="skill-item">
                <div class="skill-label"><span>Scikit-learn</span><span class="skill-pct">78%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:78%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Supervised Learning (Classification)</span><span class="skill-pct">75%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:75%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Unsupervised Learning (Clustering / PCA)</span><span class="skill-pct">72%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:72%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>XGBoost & Model Tuning</span><span class="skill-pct">65%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:65%;"></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # BI + SQL
        st.markdown("""
        <div class="skill-category-card">
            <div class="skill-cat-title">📊 BI Tools & SQL</div>
            <div class="skill-item">
                <div class="skill-label"><span>SQL</span><span class="skill-pct">78%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:78%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Power BI (DAX, Dashboards)</span><span class="skill-pct">75%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:75%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Tableau</span><span class="skill-pct">72%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:72%;"></div></div>
            </div>
            <div class="skill-item">
                <div class="skill-label"><span>Google Looker Studio & Excel</span><span class="skill-pct">80%</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:80%;"></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='lottie-float'>", unsafe_allow_html=True)
        if lottie_skills:
            st_lottie(lottie_skills, height=280, key="skills_anim")
        st.markdown("</div>", unsafe_allow_html=True)

        badges = [
            "Python", "SQL", "Pandas", "NumPy", "Matplotlib",
            "Seaborn", "Scikit-learn", "XGBoost", "K-Means",
            "PCA", "Power BI", "Tableau", "Looker Studio",
            "Excel", "VS Code", "PyCharm", "Streamlit"
        ]
        badge_html = '<div class="skill-category-card"><div class="skill-cat-title">🏷️ Tech Stack</div><div class="badge-grid">'
        for b in badges:
            badge_html += f'<span class="badge">{b}</span>'
        badge_html += '</div></div>'
        st.markdown(badge_html, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# PROJECTS
# ═══════════════════════════════════════════════════
elif selected == "Projects":

    st.markdown("""
    <div class="section-header">
        <div class="section-title">🚀 Featured Projects</div>
        <p class="section-sub">End-to-end Machine Learning projects</p>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("<div class='lottie-float'>", unsafe_allow_html=True)
        if lottie_ai:
            st_lottie(lottie_ai, height=260, key="proj_anim")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">🏦 CreditWise Loan System | Loan Approval Prediction</div>
            <div class="project-tags">
                <span class="project-tag">Supervised ML</span>
                <span class="project-tag">Classification</span>
                <span class="project-tag">Python</span>
            </div>
            <div class="project-bullet">Designed and developed a supervised ML-based loan approval prediction system to automate decision-making for a financial institution</div>
            <div class="project-bullet">Analyzed 1000+ loan applications to identify patterns affecting approval rates</div>
            <div class="project-bullet">Engineered features from applicant data including income, credit history, employment status, and loan amount</div>
            <div class="project-bullet">Implemented data cleaning, encoding, and feature scaling to prepare data for modeling</div>
            <div class="project-bullet">Built and compared Logistic Regression, K-Neighbors, and Naive Bayes classifiers to select the best-performing model</div>
            <div class="techstack-row">
                <b>Tech Stack:</b>
                <span>Python</span> | <span>Pandas</span> | <span>NumPy</span> | <span>Scikit-learn</span> | <span>Matplotlib</span> | <span>Seaborn</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-title">🛒 SmartCart Clustering System | Customer Segmentation</div>
        <div class="project-tags">
            <span class="project-tag">Unsupervised ML</span>
            <span class="project-tag">Clustering</span>
            <span class="project-tag">PCA</span>
            <span class="project-tag">Python</span>
        </div>
        <div class="project-bullet">Designed and developed an unsupervised ML-based customer segmentation system to automate behavioural profiling for a growing e-commerce platform</div>
        <div class="project-bullet">Analyzed 2240+ customer records across 22 attributes including demographics, purchase behaviour, and engagement metrics</div>
        <div class="project-bullet">Engineered features from transactional data including spending patterns, purchase frequency, recency, and channel preferences</div>
        <div class="project-bullet">Implemented data cleaning, label encoding, and feature scaling to handle mixed data types and outliers in income and spending variables</div>
        <div class="project-bullet">Built and compared K-Means and Hierarchical Clustering models using Elbow Method and Silhouette Score for optimal cluster selection</div>
        <div class="project-bullet">Applied PCA for dimensionality reduction, improving cluster visualisation and reducing noise in high-dimensional data</div>
        <div class="project-bullet">Segmented customers into distinct behavioural groups enabling personalised marketing strategies and targeted customer retention campaigns</div>
        <div class="techstack-row">
            <b>Tech Stack:</b>
            <span>Python</span> | <span>Pandas</span> | <span>NumPy</span> | <span>Scikit-learn</span> | <span>Matplotlib</span> | <span>Seaborn</span> | <span>PCA</span> | <span>K-Means</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# EDUCATION
# ═══════════════════════════════════════════════════
elif selected == "Education":

    st.markdown("""
    <div class="section-header">
        <div class="section-title">🎓 Education</div>
        <p class="section-sub">Academic background & qualifications</p>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="edu-card">
            <div class="edu-degree">Bachelor of Technology (B.Tech) in Data Science</div>
            <div class="edu-school">Pallavi Engineering College</div>
            <div class="edu-meta">
                <span>📅 Nov 2021 — Jul 2025</span>
                <span>📍 Hyderabad, India</span>
                <span class="edu-gpa">GPA: 6.5</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="edu-card">
            <div class="edu-degree">Intermediate — MPC (Mathematics, Physics, Chemistry)</div>
            <div class="edu-school">Sri Gayatri Junior College</div>
            <div class="edu-meta">
                <span>📅 Jun 2019 — Mar 2021</span>
                <span>📍 Hyderabad, India</span>
                <span class="edu-gpa">GPA: 5.9</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="edu-card">
            <div class="edu-degree">Secondary School Certificate (SSC)</div>
            <div class="edu-school">Donald Memorial High School</div>
            <div class="edu-meta">
                <span>📅 Jan 2019</span>
                <span>📍 Hyderabad, India</span>
                <span class="edu-gpa">GPA: 8.9</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Traits
        st.markdown("""
        <div class="skill-category-card" style="margin-top:1.5rem;">
            <div class="skill-cat-title">🌟 What I Bring</div>
            <div class="badge-grid">
                <span class="badge">🎯 Problem Solver</span>
                <span class="badge">📚 Quick Learner</span>
                <span class="badge">🤝 Team Player</span>
                <span class="badge">💡 Analytical Thinker</span>
                <span class="badge">🔄 Adaptable</span>
                <span class="badge">🌱 Growth Mindset</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='lottie-float'>", unsafe_allow_html=True)
        if lottie_edu:
            st_lottie(lottie_edu, height=280, key="edu_anim")
        elif lottie_coding:
            st_lottie(lottie_coding, height=280, key="edu_anim2")
        st.markdown("</div>", unsafe_allow_html=True)

        # Languages
        st.markdown("""
        <div class="skill-category-card">
            <div class="skill-cat-title">🌐 Languages</div>
            <div class="badge-grid">
                <span class="badge">English</span>
                <span class="badge">Hindi</span>
                <span class="badge">Gujarati</span>
                <span class="badge">Telugu</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Currently learning
        st.markdown("""
        <div class="skill-category-card">
            <div class="skill-cat-title">📖 Currently Upskilling</div>
            <div class="badge-grid">
                <span class="badge">Deep Learning</span>
                <span class="badge">NLP</span>
                <span class="badge">TensorFlow</span>
                <span class="badge">AI Engineering</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════
elif selected == "Contact":

    st.markdown("""
    <div class="section-header">
        <div class="section-title">📬 Get In Touch</div>
        <p class="section-sub">Let's connect and build something great together</p>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("<div class='lottie-float'>", unsafe_allow_html=True)
        if lottie_contact:
            st_lottie(lottie_contact, height=240, key="contact_anim")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="contact-card">
            <div class="contact-row">
                <div class="contact-icon">📱</div>
                <div><strong>Phone</strong><br><span style="color:#94a3b8;">+91 9640440779</span></div>
            </div>
            <div class="contact-row">
                <div class="contact-icon">📧</div>
                <div><strong>Email</strong><br><a href="mailto:abbas.off24@gmail.com" class="contact-link">abbas.off24@gmail.com</a></div>
            </div>
            <div class="contact-row">
                <div class="contact-icon">💼</div>
                <div><strong>LinkedIn</strong><br><a href="https://www.linkedin.com/in/abbasalip" target="_blank" class="contact-link">linkedin.com/in/abbasalip</a></div>
            </div>
            <div class="contact-row">
                <div class="contact-icon">💻</div>
                <div><strong>GitHub</strong><br><a href="https://github.com/abbas2407" target="_blank" class="contact-link">github.com/abbas2407</a></div>
            </div>
            <div class="contact-row">
                <div class="contact-icon">📍</div>
                <div><strong>Location</strong><br><span style="color:#94a3b8;">Hyderabad, Telangana, India</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#e2e8f0; margin-bottom:1rem;'>✉️ Send a Message</h3>", unsafe_allow_html=True)
        with st.form("contact_form"):
            name    = st.text_input("Your Name",    placeholder="John Doe")
            email   = st.text_input("Your Email",   placeholder="john@example.com")
            subject = st.text_input("Subject",      placeholder="Opportunity / Collaboration")
            message = st.text_area("Message",       placeholder="Hi Abbas, I'd love to connect...", height=140)
            submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
            if submitted:
                if name and email and message:
                    st.success("✅ Thanks for reaching out! I'll get back to you soon.")
                else:
                    st.error("❌ Please fill in all required fields.")
        st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<div class="footer">
    Made with ❤️ using <span>Streamlit</span> &nbsp;|&nbsp; © 2025 <span>Abbas Ali Palsaniya</span>. All rights reserved.
</div>
""", unsafe_allow_html=True)
