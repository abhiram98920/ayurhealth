import re
import os
import shutil

brain_dir = "/Users/admin/.gemini/antigravity/brain/666241b6-5597-476e-bde7-d76141f4a232/"
assets_dir = "/Users/admin/Desktop/ayurhealth copy/assets/"

new_files = {
    "kerala_shiro_abhyangam_1775503554244.png": "kerala_shiro_abhyangam.png",
    "kerala_pada_abhyangam_1775503575132.png": "kerala_pada_abhyangam.png",
    "kerala_kizhi_massage_1775503590258.png": "kerala_kizhi_massage.png",
    "kerala_pizhichil_1775503608813.png": "kerala_pizhichil.png",
    "kerala_diet_lifestyle_1775503630809.png": "kerala_diet_lifestyle.png",
}

for src, dst in new_files.items():
    if os.path.exists(brain_dir + src):
        shutil.copy(brain_dir + src, assets_dir + dst)
        print(f"Copied {dst}")

with open("/Users/admin/Desktop/ayurhealth copy/index.html", "r") as f:
    html = f.read()

alt_mapping = {
    "Panchakarma": "kerala_pizhichil.png",
    "Abhyangam": "kerala_abhyangam.png",
    "Abhyanga": "kerala_abhyangam.png",
    "Shirodhara": "kerala_shirodhara.png",
    "Swedana": "kerala_swedana.png",
    "Herbal Medicine": "kerala_herbs.png",
    "Diet.*Lifestyle": "kerala_diet_lifestyle.png",
    "Shiro Abhyangam": "kerala_shiro_abhyangam.png",
    "Pada Abhyangam": "kerala_pada_abhyangam.png",
    "Ela Kizhi": "kerala_kizhi_massage.png",
    "Podi Kizhi": "kerala_kizhi_massage.png",
    "Naranga Kizhi": "kerala_kizhi_massage.png",
    "Njavara Kizhi": "kerala_kizhi_massage.png",
    "Udwarthanam": "kerala_herbs.png",
    "Pizhichil": "kerala_pizhichil.png",
    "Shirovasti": "kerala_shiro_abhyangam.png",
    "Tharpanam": "kerala_herbs.png",
    "Steam Bath": "kerala_swedana.png",
    "Herbal Facial": "kerala_facial.png",
    "Hair Pack": "kerala_shiro_abhyangam.png",
    "Moroccan Bath": "kerala_swedana.png",
    "Royal Calm": "kerala_shirodhara.png",
    "Go Slim": "kerala_diet_lifestyle.png",
    "Go Detox": "kerala_swedana.png",
    "Go Calm": "kerala_shirodhara.png",
    "Full Panchakarma": "kerala_herbs.png",
    "Mother Care": "kerala_abhyangam.png",
    "Bride / Groom Package": "kerala_facial.png",
    "Little Care": "kerala_clinic.png",
    "Ayurveda Lifestyle": "kerala_diet_lifestyle.png",
    "Detox Science": "kerala_pizhichil.png",
    "Dosha Diet": "kerala_diet_lifestyle.png",
    "Ayurvedic Clinic": "kerala_clinic.png",
    "Ayurvedic Treatment": "kerala_hero.png",
}

for alt, filename in alt_mapping.items():
    # Replace any <img src="something" alt="Alt">
    html = re.sub(r'(<img[^>]*src=)["\'][^"\']+["\']([^>]*alt=["\']' + alt + '["\'])', r'\g<1>"assets/' + filename + '"\g<2>', html)
    # What if alt is before src? <img alt="Alt" src="something">
    html = re.sub(r'(<img[^>]*alt=["\']' + alt + '["\'][^>]*src=)["\'][^"\']+["\']', r'\g<1>"assets/' + filename + '"', html)
    
    # What if it's the Treatment banner with <h3>Panchakarma</h3>? Let's check format.
    # In index.html, the Treatment Methods section uses spec-box inline style backgrounds or img?
    # Wait, the 6 cards in screenshot 1 have icons overlayed, and text underneath.
    
with open("/Users/admin/Desktop/ayurhealth copy/index.html", "w") as f:
    f.write(html)
    
print("Replaced Alts in index.html")
