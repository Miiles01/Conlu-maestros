import os
import re
import glob

# Change all EFA624 to FCC160
color_map = {
    '#EFA624': '#FCC160',
    '#efa624': '#FCC160',
}

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content
    for old_color, new_color in color_map.items():
        pattern = re.compile(re.escape(old_color), re.IGNORECASE)
        new_content = pattern.sub(new_color, new_content)
        
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes in {filepath}")

base_dir = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/public/img'

svgs = []
svgs.extend(glob.glob(os.path.join(base_dir, 'hero*.svg')))
svgs.extend(glob.glob(os.path.join(base_dir, 'hero-mobile-decor', '*.svg')))

for svg in svgs:
    process_file(svg)
