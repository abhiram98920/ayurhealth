import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# 1. Fix Mobile Hero Tagline (Overlap under logo)
mobile_hero_spacing = """
    /* Fix Mobile Hero Tagline: Push content down to avoid logo overlap */
    .hero { padding-top: 160px !important; min-height: 80vh !important; }
    .hero-tagline { margin-top: 0 !important; }
"""
css = re.sub(r'@media\s*\(max-width:\s*768px\)\s*\{', '@media (max-width: 768px) {\n' + mobile_hero_spacing, css, count=1)

# 2. Fix Desktop Sticky Widgets (Move to Right + Glass Design)
desktop_widgets_glass = """
/* ===== STICKY WIDGETS DESKTOP (RIGHT + GLASS) ===== */
@media (min-width: 769px) {
    .sticky-widgets {
        position: fixed;
        right: 0; /* Move to right */
        left: auto;
        top: 50%;
        transform: translateY(-50%);
        z-index: 9991;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .sticky-widgets .widget {
        background: rgba(11, 61, 61, 0.4); /* Glass base */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        color: var(--white);
        width: 55px;
        height: 55px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-right: none;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        overflow: hidden;
        border-radius: 12px 0 0 12px; /* Curves on the left */
        box-shadow: -5px 5px 15px rgba(0,0,0,0.2);
    }
    .sticky-widgets .widget i {
        font-size: 1.4rem;
        min-width: 55px;
        text-align: center;
        transition: transform 0.3s;
    }
    .sticky-widgets .widget span {
        max-width: 0;
        white-space: nowrap;
        opacity: 0;
        transition: all 0.3s;
        font-size: 0.9rem;
        font-weight: 600;
        padding-left: 0;
    }
    .sticky-widgets .widget:hover {
        width: 180px;
        background: rgba(212, 178, 140, 0.9); /* Accent glass on hover */
        color: var(--primary);
        border-color: var(--accent);
    }
    .sticky-widgets .widget:hover i { color: var(--primary); transform: scale(1.1); }
    .sticky-widgets .widget:hover span {
        max-width: 120px;
        opacity: 1;
        padding-left: 10px;
        padding-right: 20px;
    }
    
    /* Specific hover colors for glass effect */
    .sticky-widgets .widget.wa:hover { background: rgba(37, 211, 102, 0.9); color: white; }
    .sticky-widgets .widget.wa:hover i { color: white; }
    .sticky-widgets .widget.insta:hover { background: rgba(225, 48, 108, 0.8); color: white; }
    .sticky-widgets .widget.insta:hover i { color: white; }
}
"""

# Remove old desktop widgets CSS and append new one
css = re.sub(r'/\* ===== STICKY WIDGETS DESKTOP ===== \*/.*?}\n}', '', css, flags=re.DOTALL)
css += desktop_widgets_glass

with open(css_path, 'w') as f:
    f.write(css)

print("Final adjustments (Mobile Hero + Desktop Glass Sidebar) applied.")
