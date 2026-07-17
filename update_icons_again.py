import re

html_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/index.html'

with open(html_path, 'r') as f:
    content = f.read()

# 1. Update Creativa
idea_svg = '<svg viewBox="0 0 32 32" stroke="currentColor" fill="none" stroke-width="2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"><rect x="13" y="23" width="6" height="4"/><path d="M24,12c0-4.7-4.1-8.5-8.9-7.9 c-3.6,0.4-6.5,3.3-7,6.9c-0.4,2.9,0.8,5.5,2.8,7.2c1.4,1.2,2.2,2.9,2.2,4.6V23h6v-0.2c0-1.8,0.9-3.5,2.3-4.8 C22.9,16.5,24,14.4,24,12z"/><line x1="27" y1="13" x2="30" y2="13"/><line x1="2" y1="13" x2="5" y2="13"/><line x1="23.8" y1="20.8" x2="25.9" y2="22.9"/><line x1="6.1" y1="3.1" x2="8.2" y2="5.2"/><line x1="8.2" y1="20.8" x2="6.1" y2="22.9"/><line x1="25.9" y1="3.1" x2="23.8" y2="5.2"/><path d="M18,27c0,1.1-0.9,2-2,2s-2-0.9-2-2H18z" fill="currentColor" stroke="none"/></svg>'
content = re.sub(
    r'<div class="int-icon"><svg[^>]*>.*?<\/svg><\/div>\s*<div class="int-num">6<\/div>\s*<div class="int-name">Creativa<\/div>',
    f'<div class="int-icon">{idea_svg}</div>\\n              <div class="int-num">6</div>\\n              <div class="int-name">Creativa</div>',
    content,
    flags=re.DOTALL
)

# 2. Update Interpersonal (use 2 people icon)
interpersonal_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.25"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
content = re.sub(
    r'<div class="int-icon"><svg[^>]*>.*?<\/svg><\/div>\s*<div class="int-num">4<\/div>\s*<div class="int-name">Interpersonal<\/div>',
    f'<div class="int-icon">{interpersonal_svg}</div>\\n              <div class="int-num">4</div>\\n              <div class="int-name">Interpersonal</div>',
    content,
    flags=re.DOTALL
)

with open(html_path, 'w') as f:
    f.write(content)

# 3. Make icons larger in style.css
css_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/style.css'
with open(css_path, 'r') as f:
    css_content = f.read()

# Make icon wrapper larger: from 32px to 42px
css_content = re.sub(
    r'\.int-icon \{\n  width: 32px;\n  height: 32px;',
    '.int-icon {\\n  width: 42px;\\n  height: 42px;',
    css_content
)

with open(css_path, 'w') as f:
    f.write(css_content)

print("Updated HTML and CSS for Icons.")
