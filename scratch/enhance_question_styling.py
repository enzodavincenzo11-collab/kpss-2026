import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. style.css içinde .question-text'e white-space: pre-line ekle
with open(r'c:\Users\oktay\Desktop\kpss\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'(\.question-text\s*\{[^}]*?)(\})',
    r'\1  white-space: pre-line;\n}',
    css,
    count=1
)

# Altı çizili etiketinin parlamasını ve net görünmesini sağla
u_enhance = """
/* Altı Çizili Sorularda Parlayan Vurgulu Stil */
u {
  text-decoration: underline !important;
  text-decoration-color: #38bdf8 !important;
  text-decoration-thickness: 3px !important;
  text-underline-offset: 4px !important;
  font-weight: 800 !important;
  color: #7dd3fc !important;
  background: rgba(56, 189, 248, 0.1) !important;
  padding: 1px 4px !important;
  border-radius: 4px !important;
}
"""
if "/* Altı Çizili Sorularda Parlayan" not in css:
    css += "\n" + u_enhance

with open(r'c:\Users\oktay\Desktop\kpss\style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css güncellendi (pre-line ve vurgulu <u> eklendi).")

# 2. index.html ve sw.js cache buster v=7
with open(r'c:\Users\oktay\Desktop\kpss\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'data\.js(\?v=\d+)?', 'data.js?v=7', html)
html = re.sub(r'app\.js(\?v=\d+)?', 'app.js?v=7', html)
html = re.sub(r'style\.css(\?v=\d+)?', 'style.css?v=7', html)

with open(r'c:\Users\oktay\Desktop\kpss\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open(r'c:\Users\oktay\Desktop\kpss\sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'kpss-v\d+', 'kpss-v7', sw)
with open(r'c:\Users\oktay\Desktop\kpss\sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print("Cache versiyonu v=7 yapıldı.")
