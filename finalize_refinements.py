import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# Fix "Book Now" in header
html = html.replace('<a href="#enquiry" class="connect-pill">Book Now</a>', 
                    '<a href="javascript:void(0)" onclick="openEnquiry(\'General Booking\')" class="connect-pill">Book Now</a>')

# Fix "Book Consultation" in hero
html = html.replace('<a href="#enquiry" class="btn-primary">Book Consultation</a>', 
                    '<a href="javascript:void(0)" onclick="openEnquiry(\'Consultation\')" class="btn-primary">Book Consultation</a>')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# 1. Global Typography: enforce 2 fonts strictly
# Remove specific font-family overrides for elements that should inherit or follow rule
# We already set body and h1-h6. Let's check for any other 'font-family' strings.
# Replace any font-family that isn't Cormorant Garamond or Plus Jakarta Sans
css = re.sub(r'font-family: [^;\'"]*[\'"]?Inter[\'"]?[^;]*;', 'font-family: "Plus Jakarta Sans", sans-serif;', css)
css = re.sub(r'font-family: [^;\'"]*[\'"]?Roboto[\'"]?[^;]*;', 'font-family: "Plus Jakarta Sans", sans-serif;', css)

# 2. Section Gradients: Replace 'background: var(--primary);' with gradient for sections
# Only targeted sections to avoid breaking small elements
for target in ['.about-section', '.morph-section', '.treatments-section', '.packages-section', '.testimonials-section', '.blog-section']:
    css = re.sub(f'{target} {{[^}}]*background: var\(--primary\);', 
                 f'{target} {{\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);', css)

# 3. About Section Polish: Visual Hierarchy Boost
# More brighter/bolder titles for specialty items
css = re.sub(r'\.specialty-item strong \{', '.specialty-item strong {\n    font-weight: 700;\n    color: var(--white);', css)
# Reduced opacity for description
css = re.sub(r'\.specialty-item p \{', '.specialty-item p {\n    opacity: 0.5;\n    font-size: 0.8rem;', css)
# Row spacing already increased in update_about_v4.py

# 4. Badge Refinement: smaller, shadow
css = re.sub(r'\.about-badge \{', '.about-badge {\n    transform: scale(0.9);\n    box-shadow: 0 10px 20px rgba(0,0,0,0.3);', css)

with open(css_path, 'w') as f:
    f.write(css)

print("Final UI/UX refinements complete.")
