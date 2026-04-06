import re
import os

# Update index.html
with open("/Users/admin/Desktop/ayurhealth copy/index.html", "r") as f:
    html = f.read()

# Replace inline style background-images
replacements = {
    "1591228127791-8e2eaef098d3.jpg": "kerala_pizhichil.png",
    "kerala_clinic.png": "kerala_abhyangam.png", # Abhyanga card
    "1616394584738-fc6e612e71b9.jpg": "kerala_shirodhara.png",
    "1540555700478-4be289fbecef.jpg": "kerala_swedana.png",
    "1505576399279-565b52d4ac71.jpg": "kerala_herbs.png",
    "1498837167922-ddd27525d352.jpg": "kerala_diet_lifestyle.png",
    "1522337660859-02fbefca4702.jpg": "kerala_shiro_abhyangam.png",
    "1518611012118-696072aa579a.jpg": "kerala_facial.png",
    "1555252333-9f8e92e65df9.jpg": "kerala_abhyangam.png",
    "1519415943484-9fa1873496d4.jpg": "kerala_facial.png",
    "1584515933487-779824d29309.jpg": "kerala_clinic.png"
}

for k, v in replacements.items():
    html = html.replace(f"url('assets/{k}')", f"url('assets/{v}')")
    html = html.replace(f'src="assets/{k}"', f'src="assets/{v}"')

with open("/Users/admin/Desktop/ayurhealth copy/index.html", "w") as f:
    f.write(html)

# Update build_pages_v2.py with more mappings to ensure all internal pages are authentic
with open("/tmp/build_pages_v2.py", "r") as f:
    builder = f.read()

builder_replacements = {
    "1540555700478-4be289fbecef.jpg": "kerala_swedana.png",
    "1552693673-1bf958298935.jpg": "kerala_herbs.png",
    "1498837167922-ddd27525d352.jpg": "kerala_diet_lifestyle.png",
    "1519415943484-9fa1873496d4.jpg": "kerala_clinic.png",
    "1584515933487-779824d29309.jpg": "kerala_swedana.png",
    "1600334089648-b0d9d3028eb2.jpg": "kerala_abhyangam.png",
    "1555252333-9f8e92e65df9.jpg": "kerala_abhyangam.png",
    "1544367567-0f2fcb009e0b.jpg": "kerala_shirodhara.png",
    "1616394584738-fc6e612e71b9.jpg": "kerala_facial.png",
    "1621252179027-94459d278660.jpg": "kerala_herbs.png",
    "1505576399279-565b52d4ac71.jpg": "kerala_consultation.png",
    "1518611012118-696072aa579a.jpg": "kerala_facial.png",
    "1522337660859-02fbefca4702.jpg": "kerala_shiro_abhyangam.png"
}

for k, v in builder_replacements.items():
    builder = builder.replace(k, v)

with open("/tmp/build_pages_v2.py", "w") as f:
    f.write(builder)

print("Replacement complete.")
