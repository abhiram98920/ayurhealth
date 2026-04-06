import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

# 1. Update HTML: About Heading + Text
with open(html_path, 'r') as f:
    html = f.read()

# Heading
html = html.replace('<h2>A Clinical Approach<br>To Ancient Medicine</h2>', 
                    '<h2 class="about-heading">Where Ancient Healing Meets Clinical Precision</h2>')

# Paragraph to Micro-lines
micro_lines = """
                <div class="about-microlines">
                    <p>We combine Kerala Ayurveda with modern clinical protocols.</p>
                    <p>Every treatment is tailored to your unique Prakriti.</p>
                    <p>Delivered by certified Ayurvedic doctors.</p>
                </div>
"""
p_pattern = r'<p>At Ayur Health, we integrate the rich heritage of Kerala Ayurveda with rigorous medical protocols\. Every treatment is individually designed following a thorough constitutional assessment \(<em>Prakriti</em> evaluation\) by our qualified Vaidyas\.</p>'
html = re.sub(p_pattern, micro_lines, html)

with open(html_path, 'w') as f:
    f.write(html)

# 2. Update CSS
with open(css_path, 'r') as f:
    css = f.read()

# Global Typography Enforcement
css = re.sub(r'h1, h2, h3 \{[^}]+\}', 'h1, h2, h3, h4, h5, h6 {\n    font-family: "Cormorant Garamond", serif;\n    font-weight: 300;\n    line-height: 1.1;\n}', css)

# Background Gradients for Sections
css = css.replace('.about-section {\n    background: var(--primary);', 
                  '.about-section {\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);')
css = css.replace('.morph-section {\n    background: var(--primary);', 
                  '.morph-section {\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);')

# Micro-lines Styling
css += """
.about-microlines {
    margin-bottom: 35px;
}
.about-microlines p {
    font-size: 1.05rem;
    margin-bottom: 12px;
    opacity: 0.85;
    position: relative;
    padding-left: 20px;
}
.about-microlines p::before {
    content: "•";
    position: absolute;
    left: 0;
    color: var(--accent);
}
"""

# Feature List Hierarchy
css = re.sub(r'\.specialty-item i \{[^}]+\}', 
             '.specialty-item i {\n    font-size: 1.35rem;\n    color: var(--accent);\n    margin-top: 5px;\n}', css)
css = re.sub(r'\.specialty-item strong \{[^}]+\}', 
             '.specialty-item strong {\n    display: block;\n    font-size: 1rem;\n    color: var(--white);\n    margin-bottom: 4px;\n    letter-spacing: 0.5px;\n}', css)
css = re.sub(r'\.specialty-item p \{[^}]+\}', 
             '.specialty-item p {\n    font-size: 0.82rem;\n    opacity: 0.55;\n    line-height: 1.5;\n}', css)
css = css.replace('.specialty-grid {\n    display: grid;\n    grid-template-columns: 1fr 1fr;\n    gap: 20px;\n    margin-bottom: 40px;\n}', 
                  '.specialty-grid {\n    display: grid;\n    grid-template-columns: 1fr 1fr;\n    gap: 32px 24px;\n    margin-bottom: 48px;\n}')

# Image Card Enhancement
css = re.sub(r'\.about-img-wrap \{[^}]+\}', """
.about-img-wrap {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
    transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.about-img-wrap:hover {
    transform: scale(1.03);
}
.about-img-wrap::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(11,61,61,0.4), transparent);
    pointer-events: none;
}
""", css)

# Badge Refinement
css = re.sub(r'\.about-badge \{[^}]+\}', """
.about-badge {
    position: absolute;
    bottom: 25px;
    left: 25px;
    background: rgba(212, 178, 140, 0.95);
    color: var(--primary);
    padding: 8px 18px;
    border-radius: 50px;
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    z-index: 2;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.2);
}
""", css)

# Modal Form Premium Styling
css = re.sub(r'\.modal-box \{[^}]+\}', """
.modal-box {
    background: #0b3d3d;
    background: linear-gradient(145deg, #0b3d3d, #061e1e);
    width: 95%;
    max-width: 500px;
    padding: 50px;
    border-radius: 24px;
    position: relative;
    transform: translateY(30px);
    transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
    box-shadow: 0 30px 60px rgba(0,0,0,0.5);
    border: 1px solid rgba(212, 178, 140, 0.15);
}
""", css)

# Mobile UX Fixes
css += """
@media (max-width: 768px) {
    .about-heading { font-size: 2.2rem !important; line-height: 1.2; }
    .specialty-grid { grid-template-columns: 1fr; gap: 20px; }
    .about-img-wrap { height: 320px; }
    .about-img-wrap img { height: 100%; object-fit: cover; }
    .about-text .btn-primary { width: 100%; display: block; text-align: center; }
}
"""

with open(css_path, 'w') as f:
    f.write(css)

print("About section and UI refinements applied.")
