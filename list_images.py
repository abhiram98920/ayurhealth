import re

def extract(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    matches = re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', content)
    print(f"--- {filepath} ---")
    for m in matches:
        img_tag = m.group(0)
        src = m.group(1)
        # Try to find alt or class name or surrounding context
        alt_match = re.search(r'alt=["\']([^"\']+)["\']', img_tag)
        alt = alt_match.group(1) if alt_match else 'NO ALT'
        print(f"Src: {src} | Alt: {alt}")
        
    print()

extract("/Users/admin/Desktop/ayurhealth copy/index.html")
extract("/tmp/build_pages_v2.py")
