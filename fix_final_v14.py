import re

html_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(html_path, 'r') as f:
    html = f.read()

# 1. Add Sticky Social Widgets to index.html
social_widgets_html = """
<!-- ===== STICKY CONTACT WIDGETS ===== -->
<div class="sticky-widgets">
    <a href="https://wa.me/971551292579" class="widget wa" target="_blank" aria-label="WhatsApp">
        <i class="fab fa-whatsapp"></i>
        <span>WhatsApp</span>
    </a>
    <a href="tel:0551292579" class="widget call" aria-label="Call Now">
        <i class="fas fa-phone-alt"></i>
        <span>Call Now</span>
    </a>
    <a href="https://instagram.com/ayurhealthdubai" class="widget insta" target="_blank" aria-label="Instagram">
        <i class="fab fa-instagram"></i>
        <span>Instagram</span>
    </a>
</div>
"""
if 'sticky-widgets' not in html:
    html = html.replace('</body>', social_widgets_html + '\n</body>')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# 2. Add Border to Footer and ensure it's visible
# Targeting .site-footer
footer_border_css = '.site-footer {\n    border-top: 1px solid rgba(212, 178, 140, 0.4);'
if '.site-footer {' in css:
    css = re.sub(r'\.site-footer\s*\{', footer_border_css, css)

# 3. Fix Mobile Hero Layout (Overlap fix)
mobile_hero_fix = """
    /* Mobile Hero Fix: Move trust bar up to avoid scroll overlap */
    .hero-trust { 
        margin-bottom: 110px !important; 
        font-size: 0.65rem !important; 
        gap: 10px !important;
    }
    .hero-trust .divider { height: 8px !important; }
    
    /* Sticky Widgets Mobile (Bottom Bar) */
    .sticky-widgets {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 65px;
        background: rgba(11, 61, 61, 0.95);
        backdrop-filter: blur(10px);
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 9999;
        border-top: 1px solid rgba(212, 178, 140, 0.3);
        padding: 0 10px;
    }
    .sticky-widgets .widget {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none;
        color: var(--white);
        font-size: 0.65rem;
        gap: 4px;
    }
    .sticky-widgets .widget i { font-size: 1.2rem; color: var(--accent); }
    .sticky-widgets .widget span { opacity: 0.8; font-weight: 500; }
    
    /* Ensure page content doesn't get hidden by the bottom bar */
    body { padding-bottom: 65px; }
"""

# 4. Sticky Widgets Desktop (Side Menu)
desktop_widgets_css = """
/* ===== STICKY WIDGETS DESKTOP ===== */
@media (min-width: 769px) {
    .sticky-widgets {
        position: fixed;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        z-index: 9991;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .sticky-widgets .widget {
        background: rgba(11, 61, 61, 0.85);
        backdrop-filter: blur(8px);
        color: var(--white);
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        border-right: 2px solid var(--accent);
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        overflow: hidden;
        border-radius: 0 8px 8px 0;
    }
    .sticky-widgets .widget i {
        font-size: 1.3rem;
        min-width: 50px;
        text-align: center;
        transition: color 0.3s;
    }
    .sticky-widgets .widget span {
        max-width: 0;
        white-space: nowrap;
        opacity: 0;
        transition: all 0.3s;
        font-size: 0.85rem;
        font-weight: 600;
        padding-right: 0;
    }
    .sticky-widgets .widget:hover {
        width: 160px;
        background: var(--accent);
        color: var(--primary);
    }
    .sticky-widgets .widget:hover i { color: var(--primary); }
    .sticky-widgets .widget:hover span {
        max-width: 100px;
        opacity: 1;
        padding-right: 15px;
        margin-left: -5px;
    }
    .sticky-widgets .widget.wa:hover { background: #25D366; color: white; }
    .sticky-widgets .widget.wa:hover i { color: white; }
    .sticky-widgets .widget.insta:hover { background: #E1306C; color: white; }
    .sticky-widgets .widget.insta:hover i { color: white; }
}
"""

css += desktop_widgets_css
css = re.sub(r'@media\s*\(max-width:\s*768px\)\s*\{', '@media (max-width: 768px) {\n' + mobile_hero_fix, css)

with open(css_path, 'w') as f:
    f.write(css)

print("Final cleanup (Border + Mobile Hero + Sticky Widgets) applied.")
