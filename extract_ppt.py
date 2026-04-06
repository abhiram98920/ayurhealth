import zipfile
import os

def extract_ppt_images(ppt_path, out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    with zipfile.ZipFile(ppt_path, 'r') as zp:
        for info in zp.infolist():
            if info.filename.startswith('ppt/media/'):
                zp.extract(info, out_dir)

extract_ppt_images('ayurhealthppt.pptx', 'extracted_ppt')
