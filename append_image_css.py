import os

css_append = """
/* Imagen explicativa de las 12 inteligencias (reemplaza la rueda animada) */
.intelligences-explainer-img {
  display: block;
  width: 100%;
  max-width: 1100px;
  margin: 3rem auto 0;
  border-radius: var(--radius-lg);
}

@media (max-width: 767px) {
  .intelligences-explainer-img {
    margin-top: 2rem;
    border-radius: var(--radius-md);
  }
}
"""

filepath = '/Users/miileshorton/Desktop/Archivos_Landing_Local/jaselu-landing-maestros/style.css'
with open(filepath, 'a') as f:
    f.write(css_append)
print("Appended class to style.css")
