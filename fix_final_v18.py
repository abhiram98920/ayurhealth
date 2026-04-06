import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# 1. Fix Mobile Hero Overlap (Increase trust bar gap and pin scroll lower)
mobile_overlap_fix = """
    /* Fix Mobile Hero Overlap: Increase trust bar margin and pin scroll indicator lower */
    .hero-trust { 
        margin-bottom: 180px !important; 
        font-size: 0.65rem !important; 
        gap: 12px !important;
    }
    .hero-scroll-indicator {
        bottom: 30px !important;
        transform: translateX(-50%) scale(0.9) !important;
    }
"""

# Re-apply or append to mobile media query
# I'll update the existing section I added
if '/* Fix Mobile Hero Tagline: Push content down' in css:
    css = re.sub(r'/\* Fix Mobile Hero Tagline:.*?}', 
                 '/* Fix Mobile Hero Tagline + Overlap */\\n    .hero { padding-top: 180px !important; min-height: 85vh !important; }\\n' + mobile_overlap_fix, 
                 css, flags=re.S)
else:
    # Fallback: append to the first media query (max-width: 768px)
    css = re.sub(r'@media\s*\(max-width:\s*768px\)\s*\{', '@media (max-width: 768px) {\n' + mobile_overlap_fix, css, count=1)

with open(css_path, 'w') as f:
    f.write(css)

print("Final adjustments: Fixed hero entrust/scroll overlap and tagline spacing.")
