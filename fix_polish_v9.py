import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# Manual mapping for specialty cards to be safer than greedy regex
spec_mapping = {
    '<h3>Panchakarma</h3>': '<div class="spec-card featured" onclick="openEnquiry(\'Panchakarma\')"',
    '<h3>Abhyanga</h3>': '<div class="spec-card" onclick="openEnquiry(\'Abhyanga\')"',
    '<h3>Shirodhara</h3>': '<div class="spec-card" onclick="openEnquiry(\'Shirodhara\')"',
    '<h3>Swedana</h3>': '<div class="spec-card" onclick="openEnquiry(\'Swedana\')"',
    '<h3>Herbal Medicine</h3>': '<div class="spec-card" onclick="openEnquiry(\'Herbal Medicine\')"',
    '<h3>Diet &amp; Lifestyle</h3>': '<div class="spec-card" onclick="openEnquiry(\'Diet & Lifestyle\')"'
}

for heading, replacement in spec_mapping.items():
    # Find the nearest <div class="spec-card before this heading
    # This is tricky without a proper parser, but we know the structure.
    # We'll just replace the tags directly since we know they are unique in context.
    pass

# Refined approach: split by spec-card and process blocks
parts = re.split(r'(<div class="spec-card.*?>)', html)
new_html = []
for p in parts:
    if 'class="spec-card' in p:
        # We'll attach the onclick in the next iteration when we see the <h3>
        current_card_tag = p
        continue
    if '<h3>' in p:
        name_match = re.search(r'<h3>(.*?)</h3>', p)
        if name_match:
            name = name_match.group(1).replace('&amp;', '&')
            current_card_tag = current_card_tag.replace('<div class="spec-card', f'<div class="spec-card" onclick="openEnquiry(\'{name}\')"')
            new_html.append(current_card_tag)
    new_html.append(p)

# Since the above logic is also a bit complex, let's just do direct replacements for the known 6 cards
html = html.replace('<div class="spec-card featured"', '<div class="spec-card featured" onclick="openEnquiry(\'Panchakarma\')"')
html = html.replace('<div class="spec-card" style="background-image:url(\'assets/kerala_abhyangam.png\')">', '<div class="spec-card" onclick="openEnquiry(\'Abhyanga\')" style="background-image:url(\'assets/kerala_abhyangam.png\')">')
html = html.replace('<div class="spec-card" style="background-image:url(\'assets/kerala_shirodhara.png\')">', '<div class="spec-card" onclick="openEnquiry(\'Shirodhara\')" style="background-image:url(\'assets/kerala_shirodhara.png\')">')
html = html.replace('<div class="spec-card" style="background-image:url(\'assets/kerala_swedana.png\')">', '<div class="spec-card" onclick="openEnquiry(\'Swedana\')" style="background-image:url(\'assets/kerala_swedana.png\')">')
html = html.replace('<div class="spec-card" style="background-image:url(\'assets/kerala_herbs.png\')">', '<div class="spec-card" onclick="openEnquiry(\'Herbal Medicine\')" style="background-image:url(\'assets/kerala_herbs.png\')">')
html = html.replace('<div class="spec-card" style="background-image:url(\'assets/kerala_diet_lifestyle.png\')">', '<div class="spec-card" onclick="openEnquiry(\'Diet & Lifestyle\')" style="background-image:url(\'assets/kerala_diet_lifestyle.png\')">')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# Re-apply CSS fixes because the previous script might have failed partially
if 'content: "Book Now ➔";' not in css:
    css = css.replace('content: "Explore ➔";', 'content: "Book Now ➔";')

if 'padding-top: 100px;' not in css:
    css = css.replace('.packages-section {\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);', 
                      '.packages-section {\n    background: linear-gradient(to bottom, #0b3d3d, #061e1e);\n    padding-top: 100px;')

with open(css_path, 'w') as f:
    f.write(css)

print("Polish fixes (Curated Programs space + Specialty Book Now) applied successfully.")
