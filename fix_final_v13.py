import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# Fix duplication of 500+ Patients in Hero
html = html.replace('<span>500+ Patients</span>', '<span>Clinical Excellence</span>')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# Reduce gap above footer (padding of .view-all-wrap)
css = css.replace('padding-bottom: 120px; /* Strong gap under button */', 'padding-bottom: 70px; /* Balanced gap under button */')

# Ensure border to footer is visible (intensified slightly)
css = re.sub(r'border-top: 1px solid rgba\(212, 178, 140, [^)]+\);', 
             'border-top: 1px solid rgba(212, 178, 140, 0.4);', css)

with open(css_path, 'w') as f:
    f.write(css)

print("Final cleanup (duplication + footer gap + border) applied.")
