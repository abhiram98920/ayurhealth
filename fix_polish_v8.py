import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# 1. Update Specialty Cards: Change text to 'Book Now' and add onclick functionality
# We'll use a regex to match the inner cards and inject onclick
def add_spec_onclick(match):
    name = re.search(r'<h3>(.*?)</h3>', match.group(0)).group(1).replace('&amp;', '&')
    return match.group(0).replace('<div class="spec-card', f'<div class="spec-card" onclick="openEnquiry(\'{name}\')"')

html = re.sub(r'<div class="spec-card.*?>.*?</div>', add_spec_onclick, html, flags=re.DOTALL)

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# 2. Add more space above Curated Programs section
css = css.replace('.packages-section {\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);', 
                  '.packages-section {\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);\n    padding-top: 100px; /* Increased top space */')

# 3. Change 'Explore' label to 'Book Now' on specialty cards
css = css.replace('content: "Explore ➔";', 'content: "Book Now ➔";')

with open(css_path, 'w') as f:
    f.write(css)

print("Polish fixes (Curated Programs space + Specialty Book Now) applied.")
