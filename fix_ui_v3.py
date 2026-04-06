import re
import os
import shutil

brain_dir = "/Users/admin/.gemini/antigravity/brain/666241b6-5597-476e-bde7-d76141f4a232/"
assets_dir = "/Users/admin/Desktop/ayurhealth copy/assets/"

# 1. Copy new images
new_files = {
    "kerala_podi_kizhi_1775504568031.png": "kerala_podi_kizhi.png",
    "kerala_naranga_kizhi_1775504585941.png": "kerala_naranga_kizhi.png",
    "kerala_njavara_kizhi_1775504604104.png": "kerala_njavara_kizhi.png",
    "kerala_udwarthanam_1775504620013.png": "kerala_udwarthanam.png",
}

for src, dst in new_files.items():
    if os.path.exists(brain_dir + src):
        shutil.copy(brain_dir + src, assets_dir + dst)
        print(f"Copied {dst}")

# 2. Update style.css
with open("/Users/admin/Desktop/ayurhealth copy/css/style.css", "r") as f:
    css = f.read()

# Fix search icon color on scroll
css = css.replace("#main-header.scrolled .search-toggle { color: var(--primary); }", 
                  "#main-header.scrolled .search-toggle { color: var(--accent); }")

# Better Search Form Style
css = re.sub(r'\.search-form \{[^}]+\}', """
.search-form {
    position: absolute; right: 0; top: 150%;
    background: rgba(11, 61, 61, 0.98);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(212, 178, 140, 0.3);
    border-radius: 40px;
    padding: 6px 6px 6px 24px;
    display: flex; align-items: center;
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    transform: translateY(15px);
    opacity: 0; pointer-events: none;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    width: 320px; z-index: 1000;
}
""", css)

# Fix Blog Section Background
css = css.replace("background: var(--cream);", "background: var(--primary);")
# Fix Blog Text Colors (approximate since cream variable might be used elsewhere)
blog_text_fixes = """
.blog-section .section-tag { color: var(--accent); }
.blog-section h2 { color: var(--white); }
.blog-section .blog-sub { color: rgba(255,255,255,0.7); }
.blog-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); }
.blog-card-body h3 { color: var(--white); }
.blog-card-body p { color: rgba(255,255,255,0.6); }
.blog-card-footer { border-top: 1px solid rgba(255,255,255,0.08); color: rgba(255,255,255,0.45); }
"""
css += blog_text_fixes

with open("/Users/admin/Desktop/ayurhealth copy/css/style.css", "w") as f:
    f.write(css)

# 3. Update index.html
with open("/Users/admin/Desktop/ayurhealth copy/index.html", "r") as f:
    html = f.read()

# Fix Scroll Persistence
html = html.replace("window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 60));",
                  "const checkScroll = () => header.classList.toggle('scrolled', window.scrollY > 60);\n        window.addEventListener('scroll', checkScroll);\n        checkScroll();")

# Assign Unique Images
# Ela Kizhi stays kerala_kizhi_massage
html = html.replace('alt="Podi Kizhi">\n                    <img src="assets/kerala_kizhi_massage.png"', 'alt="Podi Kizhi">\n                    <img src="assets/kerala_podi_kizhi.png"') # Wait, alt is usually in the tag
# Let's use re for robustness
html = re.sub(r'src="assets/kerala_kizhi_massage.png" alt="Podi Kizhi"', 'src="assets/kerala_podi_kizhi.png" alt="Podi Kizhi"', html)
html = re.sub(r'src="assets/kerala_kizhi_massage.png" alt="Naranga Kizhi"', 'src="assets/kerala_naranga_kizhi.png" alt="Naranga Kizhi"', html)
html = re.sub(r'src="assets/kerala_kizhi_massage.png" alt="Njavara Kizhi"', 'src="assets/kerala_njavara_kizhi.png" alt="Njavara Kizhi"', html)
html = re.sub(r'src="assets/kerala_herbs.png" alt="Udwarthanam"', 'src="assets/kerala_udwarthanam.png" alt="Udwarthanam"', html)
# Tharpanam can use consultation or herbs for now as I missed generating it
html = re.sub(r'src="assets/kerala_herbs.png" alt="Tharpanam', 'src="assets/kerala_consultation.png" alt="Tharpanam', html)

with open("/Users/admin/Desktop/ayurhealth copy/index.html", "w") as f:
    f.write(html)

print("UI Fixes applied.")
