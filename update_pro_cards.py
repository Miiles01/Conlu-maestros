import re
import os

html_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/index.html'
css_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/style.css'

new_css = """/* INTELIGENCIAS GRID CARDS */
.intelligences-grid-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  max-width: 1050px;
  margin: 3rem auto 0;
}
.int-card {
  background: white;
  border-radius: 24px 24px 12px 12px;
  border: 1px solid var(--c);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 30px 15px 25px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
}
.int-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}
.int-icon {
  color: var(--c);
  margin-bottom: 15px;
}
.int-icon svg {
  width: 52px;
  height: 52px;
  stroke-width: 1.25;
}
.int-num {
  color: var(--c);
  font-weight: 800;
  font-size: 1.1rem;
  margin-bottom: 6px;
}
.int-name {
  color: var(--color-deep-blue);
  font-weight: 700;
  font-size: 0.95rem;
  line-height: 1.2;
}
@media (max-width: 991px) {
  .intelligences-grid-cards {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 767px) {
  .intelligences-grid-cards {
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-top: 2rem;
  }
  .int-card {
    padding: 20px 10px 15px;
    border-radius: 18px 18px 10px 10px;
  }
  .int-icon svg {
    width: 44px;
    height: 44px;
  }
  .int-icon {
    margin-bottom: 10px;
  }
  .int-name {
    font-size: 0.85rem;
  }
}"""

new_html = """          <div class="intelligences-grid-cards gs-reveal-up">
            <!-- 1 -->
            <div class="int-card" style="--c: #6c5ce7;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 3 15 9.5 22 10.5 17 15.5 18 22 12 18.5 6 22 7 15.5 2 10.5 9 9.5 12 3"/><path d="M19 4l1 1.5 1.5 1-1.5 1-1 1.5-1-1.5-1.5-1 1.5-1z"/></svg></div>
              <div class="int-num">1</div>
              <div class="int-name">Lingüística</div>
            </div>
            <!-- 2 -->
            <div class="int-card" style="--c: #fd79a8;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M9 11l2 2 4-4"/><path d="M21 18l1 1-1 1-1-1z"/><path d="M4 18l1 1-1 1-1-1z"/></svg></div>
              <div class="int-num">2</div>
              <div class="int-name">Emocional</div>
            </div>
            <!-- 3 -->
            <div class="int-card" style="--c: #d63031;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/><path d="M4 6l1 1-1 1-1-1z"/><path d="M19 13l1 1-1 1-1-1z"/></svg></div>
              <div class="int-num">3</div>
              <div class="int-name">Intrapersonal</div>
            </div>
            <!-- 4 -->
            <div class="int-card" style="--c: #e17055;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/><polygon points="9 15 10 18 9 21 8 18 9 15"/></svg></div>
              <div class="int-num">4</div>
              <div class="int-name">Interpersonal</div>
            </div>
            <!-- 5 -->
            <div class="int-card" style="--c: #fdcb6e;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/><path d="M14 3l1 1-1 1-1-1z"/></svg></div>
              <div class="int-num">5</div>
              <div class="int-name">Colaborativa</div>
            </div>
            <!-- 6 -->
            <div class="int-card" style="--c: #f1c40f;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1.3.5 2.6 1.5 3.5.8.8 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 10v4"/><path d="M10 12l4-2"/><path d="M12 2v2"/><path d="M4 8h2"/><path d="M18 8h2"/></svg></div>
              <div class="int-num">6</div>
              <div class="int-name">Creativa</div>
            </div>
            <!-- 7 -->
            <div class="int-card" style="--c: #00b894;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 22l10-10"/><path d="M12 12l2.5-2.5"/><path d="M8 16l2.5-2.5"/></svg></div>
              <div class="int-num">7</div>
              <div class="int-name">Naturalista</div>
            </div>
            <!-- 8 -->
            <div class="int-card" style="--c: #27ae60;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="8" x="3" y="3" rx="1.5"/><rect width="8" height="8" x="13" y="3" rx="1.5"/><rect width="8" height="8" x="13" y="13" rx="1.5"/><rect width="8" height="8" x="3" y="13" rx="1.5"/><circle cx="7" cy="7" r="1.5"/><path d="M15 7h4"/><path d="M15 17h4M17 15v4"/><path d="M5 17h4M5 15h4"/></svg></div>
              <div class="int-num">8</div>
              <div class="int-name">Lógico Matemática</div>
            </div>
            <!-- 9 -->
            <div class="int-card" style="--c: #00cec9;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/><circle cx="12" cy="12" r="1"/><path d="M12 3v2M12 19v2M5 6l1.5 1.5M19 18l-1.5-1.5M19 6l-1.5 1.5M5 18l1.5-1.5"/></svg></div>
              <div class="int-num">9</div>
              <div class="int-name">Viso Espacial</div>
            </div>
            <!-- 10 -->
            <div class="int-card" style="--c: #0984e3;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/><path d="M13 13l3-3"/><path d="M2 5l1 1-1 1-1-1z"/></svg></div>
              <div class="int-num">10</div>
              <div class="int-name">Musical</div>
            </div>
            <!-- 11 -->
            <div class="int-card" style="--c: #5B6AAB;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><circle cx="14" cy="5" r="2"/><path d="M14 7l-2 5-3-1-3 3"/><path d="M12 12l3 4-2 6"/><path d="M15 16l4-2"/><path d="M12 7H8l-2 3"/><path d="M3 13l1 1-1 1-1-1z"/></svg></div>
              <div class="int-num">11</div>
              <div class="int-name">Corporal</div>
            </div>
            <!-- 12 -->
            <div class="int-card" style="--c: #303273;">
              <div class="int-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12c-2-3.5-4-5-6-5a5 5 0 1 0 0 10c2 0 4-1.5 6-5Zm0 0c2 3.5 4 5 6 5a5 5 0 0 0 0-10c-2 0-4 1.5-6 5Z"/><circle cx="6" cy="12" r="1.5"/><circle cx="18" cy="12" r="1.5"/></svg></div>
              <div class="int-num">12</div>
              <div class="int-name">Existencial</div>
            </div>
          </div>"""

# 1. Update CSS
with open(css_path, 'r') as f:
    css_content = f.read()

css_pattern = re.compile(r'/\* INTELIGENCIAS GRID CARDS \*/.*?@media \(max-width: 767px\) \{.*?\}', re.DOTALL)
if css_pattern.search(css_content):
    css_content = css_pattern.sub(new_css, css_content)
else:
    print("CSS block not found, appending instead.")
    css_content += "\\n" + new_css

with open(css_path, 'w') as f:
    f.write(css_content)

# 2. Update HTML
with open(html_path, 'r') as f:
    html_content = f.read()

html_pattern = re.compile(r'<div class="intelligences-grid-cards gs-reveal-up">.*?</div>\s*<!-- End container -->', re.DOTALL)
replacement = new_html + "\\n        </div> <!-- End container -->"
if html_pattern.search(html_content):
    html_content = html_pattern.sub(replacement, html_content)
else:
    print("HTML block not found.")

with open(html_path, 'w') as f:
    f.write(html_content)

print("Updated HTML and CSS for PRO cards.")
