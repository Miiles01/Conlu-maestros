import os
import re

css_code = """
/* INTELIGENCIAS GRID CARDS */
.intelligences-grid-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  max-width: 1000px;
  margin: 3rem auto 0;
}
.int-card {
  background: white;
  border-radius: 20px 20px 12px 12px;
  border: 2px solid var(--c);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 30px 15px 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
  text-align: center;
}
.int-card:hover {
  transform: translateY(-5px);
}
.int-icon {
  color: var(--c);
  margin-bottom: 12px;
}
.int-num {
  color: var(--c);
  font-weight: 800;
  font-size: 1.1rem;
  margin-bottom: 4px;
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
  }
  .int-icon {
    transform: scale(0.85);
    margin-bottom: 8px;
  }
  .int-name {
    font-size: 0.85rem;
  }
}
"""

html_code = """
          <div class="intelligences-grid-cards gs-reveal-up">
            <!-- 1 -->
            <div class="int-card" style="--c: #6c5ce7;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>
              <div class="int-num">1</div>
              <div class="int-name">Lingüística</div>
            </div>
            <!-- 2 -->
            <div class="int-card" style="--c: #fd79a8;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg></div>
              <div class="int-num">2</div>
              <div class="int-name">Emocional</div>
            </div>
            <!-- 3 -->
            <div class="int-card" style="--c: #d63031;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
              <div class="int-num">3</div>
              <div class="int-name">Intrapersonal</div>
            </div>
            <!-- 4 -->
            <div class="int-card" style="--c: #e17055;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
              <div class="int-num">4</div>
              <div class="int-name">Interpersonal</div>
            </div>
            <!-- 5 -->
            <div class="int-card" style="--c: #fdcb6e;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
              <div class="int-num">5</div>
              <div class="int-name">Colaborativa</div>
            </div>
            <!-- 6 -->
            <div class="int-card" style="--c: #f1c40f;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1.3.5 2.6 1.5 3.5.8.8 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg></div>
              <div class="int-num">6</div>
              <div class="int-name">Creativa</div>
            </div>
            <!-- 7 -->
            <div class="int-card" style="--c: #00b894;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 22l10-10"/></svg></div>
              <div class="int-num">7</div>
              <div class="int-name">Naturalista</div>
            </div>
            <!-- 8 -->
            <div class="int-card" style="--c: #27ae60;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg></div>
              <div class="int-num">8</div>
              <div class="int-name">Lógico Matemática</div>
            </div>
            <!-- 9 -->
            <div class="int-card" style="--c: #00cec9;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg></div>
              <div class="int-num">9</div>
              <div class="int-name">Viso Espacial</div>
            </div>
            <!-- 10 -->
            <div class="int-card" style="--c: #0984e3;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg></div>
              <div class="int-num">10</div>
              <div class="int-name">Musical</div>
            </div>
            <!-- 11 -->
            <div class="int-card" style="--c: #5B6AAB;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="1"/><path d="m9 20 3-6 3 6"/><path d="m6 8 6 2 6-2"/><path d="M12 10v4"/></svg></div>
              <div class="int-num">11</div>
              <div class="int-name">Corporal</div>
            </div>
            <!-- 12 -->
            <div class="int-card" style="--c: #303273;">
              <div class="int-icon"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12c-2-2.67-4-4-6-4a4 4 0 1 0 0 8c2 0 4-1.33 6-4Zm0 0c2 2.67 4 4 6 4a4 4 0 0 0 0-8c-2 0-4 1.33-6 4Z"/></svg></div>
              <div class="int-num">12</div>
              <div class="int-name">Existencial</div>
            </div>
          </div>
"""

# Append CSS
css_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/style.css'
with open(css_path, 'a') as f:
    f.write(css_code)

# Update HTML
html_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/index.html'
with open(html_path, 'r') as f:
    content = f.read()

# Make section available on mobile (remove desktop-only)
content = content.replace('<section class="methodology section desktop-only" id="metodologia" data-theme="dark">', '<section class="methodology section" id="metodologia" data-theme="dark">')

# Replace the img tag with the new grid
pattern = r'<img src="\./img/inteligencias-explicacion\.png".*?>'
content = re.sub(pattern, html_code, content, count=1)

with open(html_path, 'w') as f:
    f.write(content)

print("Updated HTML and CSS for intelligences cards.")
