import re
import os

html_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/index.html'
css_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/style.css'
js_path = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/main.js'

# --- 1. Update HTML ---
new_html = """          <div class="video-container gs-reveal-up">
            <!-- Desktop/tablet: video horizontal de YouTube, pausado hasta dar clic -->
            <div class="video-facade demo-video-desktop" data-video-id="Kq7Aj7Qd5Ec">
              <img src="https://img.youtube.com/vi/Kq7Aj7Qd5Ec/maxresdefault.jpg" alt="Video demo" loading="lazy">
              <button class="play-circle" aria-label="Reproducir video">
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
              </button>
            </div>
            <!-- Mobile: video vertical local, pausado hasta dar clic -->
            <div class="video-facade-local demo-video-mobile">
              <video preload="metadata" playsinline src="./videos/institute-2-1-optimized.mp4#t=0.1"></video>
              <button class="play-circle" aria-label="Reproducir video">
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
              </button>
            </div>
          </div>"""

with open(html_path, 'r') as f:
    html_content = f.read()

# Replace the video container
html_pattern = re.compile(r'<div class="video-container gs-reveal-up">.*?</div>\s*</div>', re.DOTALL)
if html_pattern.search(html_content):
    html_content = html_pattern.sub(new_html + "\\n        </div>", html_content)
else:
    print("HTML block not found.")

with open(html_path, 'w') as f:
    f.write(html_content)


# --- 2. Update CSS ---
new_css = """
/* Fachada de video: imagen pausada + círculo verde con play blanco */
.video-facade,
.video-facade-local {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  cursor: pointer;
  background: var(--color-deep-blue);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.video-facade {
  aspect-ratio: 16 / 9;
}

.video-facade-local {
  aspect-ratio: 9 / 16;
  max-width: 380px;
  margin: 0 auto;
}

.video-facade img,
.video-facade iframe,
.video-facade-local video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border: 0;
  display: block;
}

.play-circle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 84px;
  height: 84px;
  border: none;
  border-radius: 50%;
  background: var(--color-lime-green);
  color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 2;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
  transition: transform 0.25s ease;
}

.play-circle svg {
  width: 36px;
  height: 36px;
  margin-left: 4px;
}

.play-circle:hover {
  transform: translate(-50%, -50%) scale(1.08);
}

.is-playing .play-circle {
  display: none;
}
"""

with open(css_path, 'a') as f:
    f.write(new_css)


# --- 3. Update JS ---
new_js = """

// Fachadas de video: círculo verde + play blanco; al clic reproducen CON sonido y controles
document.querySelectorAll('.video-facade[data-video-id]').forEach(facade => {
  facade.addEventListener('click', () => {
    const id = facade.getAttribute('data-video-id');
    facade.innerHTML = `<iframe src="https://www.youtube.com/embed/${id}?autoplay=1&controls=1&rel=0&modestbranding=1&playsinline=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>`;
    facade.classList.add('is-playing');
  }, { once: true });
});

document.querySelectorAll('.video-facade-local').forEach(facade => {
  const video = facade.querySelector('video');
  if (!video) return;
  facade.addEventListener('click', () => {
    video.muted = false;
    video.volume = 1;
    video.setAttribute('controls', '');
    video.play();
    facade.classList.add('is-playing');
  }, { once: true });
});
"""

with open(js_path, 'a') as f:
    f.write(new_js)

print("Updated HTML, CSS, and JS for interactive video facades.")
