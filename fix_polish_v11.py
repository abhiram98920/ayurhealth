import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# Increase gap under View All Packages to 150px for extra breathing room
css = css.replace('padding-bottom: 100px; /* Increased gap at bottom of section */', 'padding-bottom: 150px; /* Extra generous gap for clinical feel */')

with open(css_path, 'w') as f:
    f.write(css)

print("Final polish: Ultra-generous gap applied under View All Packages button.")
