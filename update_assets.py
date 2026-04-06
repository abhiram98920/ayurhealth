import os
import shutil

brain_dir = "/Users/admin/.gemini/antigravity/brain/666241b6-5597-476e-bde7-d76141f4a232/"
assets_dir = "/Users/admin/Desktop/ayurhealth copy/assets/"

files_to_copy = {
    "hero_banner_kerala_1775503082680.png": "kerala_hero.png",
    "shirodhara_kerala_1775503099093.png": "kerala_shirodhara.png",
    "abhyangam_kerala_1775503115923.png": "kerala_abhyangam.png",
    "consultation_kerala_1775503132381.png": "kerala_consultation.png",
    "clinic_exterior_kerala_1775503169685.png": "kerala_clinic.png",
    "swedana_kerala_1775503188506.png": "kerala_swedana.png",
    "herbal_facial_kerala_1775503200943.png": "kerala_facial.png",
    "herbs_medicines_kerala_1775503222138.png": "kerala_herbs.png"
}

# 1. Copy images
for src, dst in files_to_copy.items():
    if os.path.exists(brain_dir + src):
        shutil.copy(brain_dir + src, assets_dir + dst)
        print(f"Copied {dst}")

# 2. Update index.html
with open("/Users/admin/Desktop/ayurhealth copy/index.html", "r") as f:
    html = f.read()

replacements = {
    "1544367567-0f2fcb009e0b.jpg": "kerala_hero.png",
    "1600334089648-b0d9d3028eb2.jpg": "kerala_clinic.png",
}
for k, v in replacements.items():
    html = html.replace(k, v)

with open("/Users/admin/Desktop/ayurhealth copy/index.html", "w") as f:
    f.write(html)

# 3. Update build_pages_v2.py
with open("/tmp/build_pages_v2.py", "r") as f:
    builder = f.read()

builder_replacements = {
    "1540555700478-4be289fbecef.jpg": "kerala_consultation.png",
    "1552693673-1bf958298935.jpg": "kerala_herbs.png",
    "1498837167922-ddd27525d352.jpg": "kerala_abhyangam.png",
    "1519415943484-9fa1873496d4.jpg": "kerala_clinic.png",
    "1584515933487-779824d29309.jpg": "kerala_shirodhara.png",
    "1600334089648-b0d9d3028eb2.jpg": "kerala_abhyangam.png",
    "1555252333-9f8e92e65df9.jpg": "kerala_herbs.png",
    "1544367567-0f2fcb009e0b.jpg": "kerala_shirodhara.png",
    "1584515933487-779824d29309.jpg": "kerala_swedana.png",
    "1616394584738-fc6e612e71b9.jpg": "kerala_facial.png",
    "1621252179027-94459d278660.jpg": "kerala_herbs.png",
    "1505576399279-565b52d4ac71.jpg": "kerala_consultation.png",
    "1518611012118-696072aa579a.jpg": "kerala_facial.png"
}
for k, v in builder_replacements.items():
    builder = builder.replace(k, v)

with open("/tmp/build_pages_v2.py", "w") as f:
    f.write(builder)

print("Replacement complete.")
