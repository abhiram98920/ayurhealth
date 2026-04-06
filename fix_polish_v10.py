import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# 1. Add more gap under View All Packages
# We target the .view-all-wrap inside .packages-section or generally
# Looking at the previous turn, I added padding-bottom: 60px to .view-all-wrap
# I'll increase it to 100px for a more pronounced gap.
css = css.replace('padding-bottom: 60px; /* Gap at bottom of section */', 'padding-bottom: 100px; /* Increased gap at bottom of section */')

# 2. Add border on top side of the footer (ensure it's visible)
# I added border-top: 1px solid rgba(212, 178, 140, 0.15); previously
# I'll make it slightly more opaque for better visibility.
css = css.replace('border-top: 1px solid rgba(212, 178, 140, 0.15);', 'border-top: 1px solid rgba(212, 178, 140, 0.25);')

with open(css_path, 'w') as f:
    f.write(css)

print("Final polish (more bottom gap + footer border) applied.")
