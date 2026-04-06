import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# 1. Update Mobile Buttons: Standardize width to 100% for all top-level section buttons
# Targeting hero, about, packages, blog, and general section CTAs
mobile_button_standard = """
    /* Standardize main section buttons to full width */
    .hero-btns, .view-all-wrap { 
        width: 100%; 
        display: flex; 
        flex-direction: column; 
        gap: 15px; 
    }
    .hero-btns a, .about-text .btn-primary, .view-all-wrap .btn-primary, .view-all-wrap a.btn-primary { 
        width: 100% !important; 
        display: block !important; 
        text-align: center !important; 
        margin: 0 !important;
    }
    
    /* Fix Specialty Button Overlay: hide the absolute cue and add room or static placement */
    .spec-card::after { display: none !important; }
    .spec-card { padding-bottom: 25px; } /* Ensure text doesn't hit the bottom edge */
"""

# Insert into the @media (max-width: 768px) block or create a new clear one at the end
css += f"\n\n@media (max-width: 768px) {{\n{mobile_button_standard}\n}}\n"

with open(css_path, 'w') as f:
    f.write(css)

print("Mobile button standardization and specialty fix applied.")
