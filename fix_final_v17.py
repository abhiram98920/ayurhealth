import re

css_path = "/Users/admin/Desktop/ayurhealth copy/css/style.css"

with open(css_path, 'r') as f:
    css = f.read()

# Refine Desktop Sticky Widgets (Right-anchored, row-reverse)
desktop_widgets_refined = """
/* ===== STICKY WIDGETS DESKTOP (REFINED EXPAND) ===== */
@media (min-width: 769px) {
    .sticky-widgets {
        position: fixed;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        z-index: 9991;
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: flex-end;
    }
    .sticky-widgets .widget {
        background: rgba(11, 61, 61, 0.45);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        color: var(--white);
        width: 55px;
        height: 55px;
        display: flex;
        flex-direction: row-reverse; /* Keep icon at the right edge */
        align-items: center;
        text-decoration: none;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-right: none;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        overflow: hidden;
        border-radius: 12px 0 0 12px;
        box-shadow: -5px 5px 15px rgba(0,0,0,0.2);
    }
    .sticky-widgets .widget i {
        font-size: 1.4rem;
        min-width: 55px; /* Exact match with collapsed width */
        height: 55px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.3s;
    }
    .sticky-widgets .widget span {
        max-width: 0;
        white-space: nowrap;
        opacity: 0;
        transition: all 0.3s ease;
        font-size: 0.95rem;
        font-weight: 600;
        overflow: hidden;
    }
    .sticky-widgets .widget:hover {
        width: 180px;
        background: rgba(212, 178, 140, 0.95);
        color: var(--primary);
        border-color: var(--accent);
    }
    .sticky-widgets .widget:hover i { transform: scale(1.1); }
    .sticky-widgets .widget:hover span {
        max-width: 120px;
        opacity: 1;
        padding-right: 10px; /* Space from icon */
    }
    .sticky-widgets .widget.wa:hover { background: rgba(37, 211, 102, 0.95); color: white; }
    .sticky-widgets .widget.insta:hover { background: rgba(225, 48, 108, 0.95); color: white; }
}
"""

# Replace the previous desktop widgets block
# Use a more flexible regex to find the block
css = re.sub(r'/\* ===== STICKY WIDGETS DESKTOP \(RIGHT \+ GLASS\) \*/.*?}\n}', '', css, flags=re.DOTALL)
css += desktop_widgets_refined

with open(css_path, 'w') as f:
    f.write(css)

print("Final adjustments: Refined sticky widget expand animation.")
