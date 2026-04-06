import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# Fix the button container in index.html to use a class and remove restrictive inline styles
html = html.replace('<div style="text-align: center; margin-top: 50px;">\n            <a href="packages.html" class="btn-primary" style="display:inline-block; text-decoration:none;">View All Packages</a>',
                    '<div class="view-all-wrap">\n            <a href="packages.html" class="btn-primary">View All Packages</a>')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# Ensure .view-all-wrap has both top and a large bottom gap
css = re.sub(r'\.view-all-wrap \{[^}]+\}', 
             '.view-all-wrap {\n    display: flex;\n    justify-content: center;\n    margin-top: 60px;\n    padding-bottom: 120px; /* Strong gap under button */\n}', css)

# Intensify footer border one more time for absolute clarity
css = re.sub(r'border-top: 1px solid rgba\(212, 178, 140, [^)]+\);', 
             'border-top: 1px solid rgba(212, 178, 140, 0.3);', css)

with open(css_path, 'w') as f:
    f.write(css)

print("Polish v12: Fixed HTML structure and applied ultra-generous gaps.")
