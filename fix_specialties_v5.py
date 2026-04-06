import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# 1. Update Heading
html = html.replace('<h2>Classical Ayurvedic<br>Treatment Methods</h2>', 
                    '<h2 class="spec-main-heading">Authentic Ayurvedic Treatments for Complete Healing</h2>')

# 2. Add 'featured' class to Panchakarma
# We'll use re to target specifically the Panchakarma card
html = re.sub(r'(<div class="spec-card" style="background-image:url\(\'assets/kerala_pizhichil.png\'\)">)', 
              r'\1\n                <div class="spec-badge">Featured Treatment</div>', html)
# Actually, the user said "Make 1 card slightly bigger". I'll add a class.
html = html.replace('<div class="spec-card" style="background-image:url(\'assets/kerala_pizhichil.png\')">',
                    '<div class="spec-card featured" style="background-image:url(\'assets/kerala_pizhichil.png\')">')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# 3. Fix Blog Contrast (v3 had typos)
css = re.sub(r'\.blog-body h3 \{[^}]+\}', '.blog-body h3 { font-size: 1.3rem; margin-bottom: 12px; color: var(--accent); }', css)
css = re.sub(r'\.blog-body p \{[^}]+\}', '.blog-body p { font-size: 0.86rem; opacity: 0.85; margin-bottom: 20px; color: var(--cream); line-height: 1.6; }', css)
css = re.sub(r'\.blog-read \{[^}]+\}', '.blog-read {\n    width: 38px; height: 38px; border-radius: 50%; background: var(--accent); display: flex; align-items: center; justify-content: center; color: var(--primary); transition: var(--transition); text-decoration: none; font-size: 0.85rem; }', css)

# Fix Blog Header (Titles and Subtext)
css = re.sub(r'\.blog-header-left h2 \{[^}]+\}', '.blog-header-left h2 {\n    font-size: clamp(2rem, 3.5vw, 3rem);\n    color: var(--white);\n    margin-top: 0;\n}', css)
css = re.sub(r'\.blog-header-right p \{[^}]+\}', '.blog-header-right p {\n    font-size: 0.95rem;\n    line-height: 1.75;\n    color: var(--cream);\n    opacity: 0.8;\n    max-width: 500px;\n}', css)

# 4. Fix Search Input Visibility
css = re.sub(r'\.search-form input \{[^}]+\}', '.search-form input {\n    border: none; outline: none; background: transparent;\n    width: 100%; font-family: "Plus Jakarta Sans", sans-serif;\n    color: var(--white); font-size: 1rem;\n}', css)

# 5. Specialties Enhancement: Hover, Featured, Mobile
spec_css = """
/* ===== SPECIALTIES ENHANCEMENT ===== */
.spec-main-heading { font-size: clamp(2rem, 4vw, 3.2rem) !important; color: var(--white); margin-bottom: 20px; }

.spec-card {
    position: relative;
    border-radius: 18px;
    overflow: hidden;
    cursor: pointer;
    background-size: 100%;
    background-position: center;
    transition: background-size 0.6s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.4s ease, box-shadow 0.4s ease;
}

.spec-card:hover {
    background-size: 110%;
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.spec-card::after {
    content: "Explore ➔";
    position: absolute;
    bottom: 20px;
    right: 20px;
    background: var(--accent);
    color: var(--primary);
    padding: 6px 14px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 50px;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
    z-index: 5;
}

.spec-card:hover::after {
    opacity: 1;
    transform: translateY(0);
}

.spec-card.featured {
    transform: scale(1.05);
    z-index: 10;
    border: 1px solid rgba(212, 178, 140, 0.35);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}
.spec-card.featured:hover { transform: scale(1.08) translateY(-8px); }

.spec-card.featured .spec-badge {
    position: absolute;
    top: 20px; left: 20px;
    background: var(--accent);
    color: var(--primary);
    padding: 6px 15px;
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    border-radius: 50px;
    z-index: 5;
}

/* Mobile responsive Specialties */
@media (max-width: 768px) {
    .spec-cards {
        display: grid;
        grid-template-columns: 1fr;
        gap: 24px;
    }
    .spec-card.featured { transform: scale(1); }
    .spec-card.featured:hover { transform: translateY(-5px); }
    .spec-card-overlay { background: rgba(6,30,30,0.65); } /* Stronger mobile overlay */
}
"""
css += spec_css

with open(css_path, 'w') as f:
    f.write(css)

print("Specialties enhancement and contrast fixes applied.")
