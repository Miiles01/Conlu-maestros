import os
import re
import glob

# Palette mapping
color_map = {
    '#9DC423': '#303273', # Green -> Azul Conlú
    '#9dc423': '#303273',
    '#EF7E81': '#7184BD', # Pink -> Azul Claro
    '#ef7e81': '#7184BD',
    '#F5B2B3': '#5B6AAB', # Light Pink -> Azul Suave
    '#f5b2b3': '#5B6AAB',
    '#85D4DA': '#33B8C2', # Light Cyan -> Cian
    '#85d4da': '#33B8C2',
    '#62CAD1': '#33B8C2', # Medium Cyan -> Cian
    '#62cad1': '#33B8C2',
    # Ensure existing good colors stay the same just in case, but we don't need to list them
}

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content
    for old_color, new_color in color_map.items():
        # Case insensitive replacement for hex codes
        pattern = re.compile(re.escape(old_color), re.IGNORECASE)
        new_content = pattern.sub(new_color, new_content)
        
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes in {filepath}")

base_dir = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/public/img'

# Find all SVGs
svgs = []
svgs.extend(glob.glob(os.path.join(base_dir, 'hero*.svg')))
svgs.extend(glob.glob(os.path.join(base_dir, 'hero-mobile-decor', '*.svg')))

for svg in svgs:
    process_file(svg)
