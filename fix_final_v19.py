import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# Refine Mobile Hero Layout: Use relative positioning to LIFT the trust bar away from the scroll indicator
mobile_lift_fix = """
    /* Refine Mobile Hero: Manually lift trust bar and tagline */
    .hero { 
        padding-top: 150px !important; 
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        padding-bottom: 80px !important;
    }
    .hero-content {
        margin-top: 20px !important;
    }
    .hero-trust { 
        position: relative !important;
        top: -60px !important; /* Lifted up significantly */
        font-size: 0.62rem !important; 
        margin-bottom: 0 !important;
        z-index: 10 !important;
    }
    .hero-scroll-indicator {
        bottom: 20px !important;
        z-index: 5 !important;
    }
"""

# Update the mobile media query section
if '/* Fix Mobile Hero Tagline + Overlap */' in css:
    css = re.sub(r'/\* Fix Mobile Hero Tagline \+ Overlap \*/.*?}', 
                 '/* Fix Mobile Hero Tagline + Lifted Trust Bar */\\n' + mobile_lift_fix, 
                 css, flags=re.S)
else:
    # Append to the first mobile media query
    css = re.sub(r'@media\s*\(max-width:\s*768px\)\s*\{', '@media (max-width: 768px) {\n' + mobile_lift_fix, css, count=1)

with open(css_path, 'w') as f:
    f.write(css)

print("Final adjustments: Manually lifted the Trust Bar on mobile for absolute clearance.")
