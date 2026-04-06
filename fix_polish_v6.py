import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# 1. Badge Visibility Fix: Add padding to the container to prevent clipping
css = css.replace('.package-grid {', '.package-grid {\n    padding-top: 20px; /* Room for badges */')

# 2. Gap after Buttons (Bottom of section)
# Currently: .view-all-wrap { display: flex; justify-content: center; margin-top: 45px; }
css = css.replace('.view-all-wrap {', '.view-all-wrap {\n    padding-bottom: 60px; /* Gap at bottom of section */')

# 3. Footer Border Fix
css = css.replace('.site-footer {', '.site-footer {\n    border-top: 1px solid rgba(212, 178, 140, 0.15);')

# 4. Curated Programs Heading Refinement (from User request "Curated Programs")
# Redefine the Packages Heading from "Our Healing Packages" to "Curated Programs"
with open(html_path, 'r') as f:
    html = f.read()

html = html.replace('<h2>Our Healing Packages</h2>', '<h2>Curated Programs</h2>')
html = html.replace('<h2>Our Programs</h2>', '<h2>Curated Programs</h2>') # Backup catch-all

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'w') as f:
    f.write(css)

print("Polishing fixes (badge, gap, footer, curated programs) applied.")
